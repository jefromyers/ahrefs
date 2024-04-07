from contextlib import contextmanager
from dataclasses import dataclass
from typing import Dict

from httpx import Client, HTTPStatusError, RequestError, Response

from cache import Cache
from schemas.base import RESPONSE_CLASS_MAP, APIRequest, BaseResponse


class FailedRetryException(Exception):
    ...


@dataclass
class AhrefsAPI:
    client: Client
    API: str
    TIMEOUT: int
    cache: Cache = Cache()

    def _get_cached_resp(
        self, endpoint: str, params: Dict[str, str]
    ) -> Response | None:
        key = self.cache.create_key(endpoint, params)
        return self.cache.get(key)

    def _cache_resp(self, endpoint: str, params: Dict[str, str], response: Response):
        key = self.cache.create_key(endpoint, params)
        self.cache.set(key, response)

    def get(self, req: APIRequest) -> Response:
        url = f"{self.API}{req._endpoint}"
        params = req.make_params()

        if req.cache:
            cached = self._get_cached_resp(req._endpoint, params)
            if cached:
                return cached

        for attempt in range(req.retry + 1):
            try:
                resp = self.client.get(url, params=params, timeout=self.TIMEOUT)
                resp.raise_for_status()
                if req.cache:
                    self._cache_resp(req._endpoint, params, resp)
                return resp
            except (HTTPStatusError, RequestError) as e:
                if attempt == req.retry:
                    more_info = ""
                    if resp and resp.text:
                        more_info = f" - {resp.text}"
                    raise FailedRetryException(
                        f"Failed to get response after {req.retry} retries {more_info}"
                    ) from e

    def request(
        self, req: APIRequest
    ) -> BaseResponse[APIRequest] | list[BaseResponse[APIRequest]]:
        resp = self.get(req)
        resp_klass = RESPONSE_CLASS_MAP.get(type(req))
        if not resp_klass:
            raise ValueError(f"Unknown request type: {req}")

        obj = resp.json()[req._obj_name]
        elapsed = resp.elapsed.total_seconds()

        if isinstance(obj, list):
            return [resp_klass(**item, request=req, elapsed=elapsed) for item in obj]
        else:
            return resp_klass(**obj, request=req, elapsed=elapsed)

    @classmethod
    @contextmanager
    def connect(
        cls,
        token: str | None = None,
        API: str = "https://api.ahrefs.com",
        TIMEOUT: int = 20,
        **kwargs,
    ):
        headers = {
            "User-Agent": "AhrefsAPI",
            "Authorization": f"Bearer {token}" if token else "",
            "Content-Type": "application/json",
        }
        kwargs.setdefault("headers", headers)
        kwargs.setdefault("http2", True)
        kwargs.setdefault("timeout", TIMEOUT)

        with Client(**kwargs) as client:
            yield cls(client=client, API=API, TIMEOUT=TIMEOUT)
