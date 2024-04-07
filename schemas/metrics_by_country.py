from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    CountryCode,
    HistoryGrouping,
    RequestMode,
    VolumeMode,
    response_for,
)


class MetricsByCountryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/metrics-by-country")
    _obj_name: str = PrivateAttr("metrics")
    limit: int = Field(
        ..., title="Limit", description="The number of results to return."
    )
    mode: RequestMode = Field(
        RequestMode.subdomains,
        title="Mode",
        description=(
            "The scope of the search based on the target you entered. `exact`, `prefix`, `domain`, `subdomains`"
        ),
    )
    offset: int = Field(
        0,
        title="Offset",
        description="Returned results will start from the row indicated in the offset value.",
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    volume_mode: VolumeMode = Field(
        VolumeMode.monthly,
        description="The volume mode to use for the request. Defaults to 'monthly'.",
    )
    date: DateType = Field(
        ..., description="A date to report metrics on in YYYY-MM-DD format."
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(MetricsByCountryRequest)
class MetricsByCountryResponse(BaseResponse):
    country: str = Field(..., title="Country", description="The country")
    org_keywords: int = Field(
        ...,
        title="Organic Keywords",
        description=(
            "The total number of keywords that your target ranks for in the "
            "top 100 organic search results."
        ),
    )
    paid_keywords: int = Field(
        ...,
        title="Paid Keywords",
        description=(
            "The total number of keywords that your target ranks for in "
            "paid search results."
        ),
    )
    org_keywords_1_3: int = Field(
        ...,
        title="Top 3 Organic Keywords",
        description=(
            "The total number of keywords that your target ranks for in the top 3 "
            "organic search results."
        ),
    )
    org_traffic: int = Field(
        ...,
        title="Organic Traffic",
        description=(
            "The estimated number of monthly visitors that your target gets from "
            "organic search."
        ),
    )
    org_cost: int | None = Field(
        ...,
        title="Organic Cost",
        description="The estimated value of your target's monthly organic search traffic.",
    )
    paid_traffic: int = Field(
        ...,
        title="Paid Traffic",
        description=(
            "The estimated number of monthly visitors that your target gets from paid search."
        ),
    )
    paid_cost: int | None = Field(
        ...,
        title="Paid Cost",
        description="The estimated cost of your target's monthly paid search traffic.",
    )
    paid_pages: int = Field(
        ...,
        title="Paid Pages",
        description="The total number of pages from a target ranking in paid search results.",
    )
