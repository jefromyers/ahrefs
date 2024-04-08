from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    CountryCode,
    RequestMode,
    VolumeMode,
    response_for,
)


class PagesByTrafficRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/pages-by-traffic")
    _obj_name: str = PrivateAttr("pages")
    country_code: CountryCode | None = Field(
        None,
        title="Country Code",
        description="The country code to use for the request. Defaults to None.",
    )
    mode: RequestMode = Field(
        RequestMode.subdomains,
        title="Mode",
        description=(
            "The scope of the search based on the target you entered. "
            "`exact`, `prefix`, `domain`, `subdomains`"
        ),
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    volume_mode: VolumeMode = Field(
        VolumeMode.monthly,
        description="The volume mode to use for the request. Defaults to 'monthly'.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(PagesByTrafficRequest)
class PagesByTrafficResponse(BaseResponse):
    range0_pages: int = Field(
        ...,
        title="range0_pages",
        description="The total number of pages with 0 traffic.",
    )
    range100_traffic: int = Field(
        ...,
        title="range100_traffic",
        description="(10 units) The total traffic from pages with 1-100 traffic.",
    )
    range100_pages: int = Field(
        ...,
        title="range100_pages",
        description="The total number of pages with 1-100 traffic.",
    )
    range1k_traffic: int = Field(
        ...,
        title="range1k_traffic",
        description="(10 units) The total traffic from pages with 101-1K traffic.",
    )
    range1k_pages: int = Field(
        ...,
        title="range1k_pages",
        description="The total number of pages with 101-1K traffic.",
    )
    range5k_traffic: int = Field(
        ...,
        title="range5k_traffic",
        description="(10 units) The total traffic from pages with 1K-5K traffic.",
    )
    range5k_pages: int = Field(
        ...,
        title="range5k_pages",
        description="The total number of pages with 1K-5K traffic.",
    )
    range10k_traffic: int = Field(
        ...,
        title="range10k_traffic",
        description="(10 units) The total traffic from pages with 5K-10K traffic.",
    )
    range10k_pages: int = Field(
        ...,
        title="range10k_pages",
        description="The total number of pages with 5K-10K traffic.",
    )
    range10k_plus_traffic: int = Field(
        ...,
        title="range10k_plus_traffic",
        description="(10 units) The total traffic from pages with 10K+ traffic.",
    )
    range10k_plus_pages: int = Field(
        ...,
        title="10K+ traffic",
        description="The total number of pages with 10K+ traffic.",
    )
