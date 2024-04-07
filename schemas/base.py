from typing import Dict, Generic, Type, TypeVar

from pydantic import BaseModel, Field, PrivateAttr

APIRequest = TypeVar("APIRequest", bound="BaseRequest")

RESPONSE_CLASS_MAP = {}


def response_for(req_type: APIRequest):
    def dec(resp_klass: Type[BaseResponse]):
        RESPONSE_CLASS_MAP[req_type] = resp_klass
        return resp_klass

    return dec


class BaseRequest(BaseModel):
    retry: int = Field(0, description="The number of retries")
    cache: bool = Field(True, description="Whether to cache the response")

    def make_params(self) -> Dict[str, str]:
        return self.dict(exclude={"retry", "cache"})


class BaseResponse(BaseModel, Generic[APIRequest]):
    request: APIRequest = Field(..., description="The request object")
    elapsed: float = Field(..., description="The time taken to process the request")
