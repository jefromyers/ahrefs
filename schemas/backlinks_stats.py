from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class BacklinksStatsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/backlinks-stats")
    _obj_name: str = PrivateAttr("metrics")
    date: DateType = Field(
        ..., description="A date to report metrics on in YYYY-MM-DD format."
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )


@response_for(BacklinksStatsRequest)
class BacklinksStatsResponse(BaseResponse):
    live: int = Field(
        ...,
        title="Live Backlinks",
        description="The total number of links from other websites pointing to your target.",
    )
    all_time: int = Field(
        ...,
        title="All Time Backlinks",
        description="The total number of links from other websites pointing to your target for all time.",
    )
    live_refdomains: int = Field(
        ...,
        title="Live Referring Domains",
        description="The total number of unique domains linking to your target.",
    )
    all_time_refdomains: int = Field(
        ...,
        title="All Time Referring Domains",
        description="The total number of unique domains linking to your target for all time.",
    )
