from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    RequestMode,
    VolumeMode,
    response_for,
)


class MetricsByCountryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/metrics-by-country")
    _obj_name: str = PrivateAttr("metrics")
    limit: int | None = Field(
        0, title="Limit", description="The number of results to return."
    )
    # Required fields
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
