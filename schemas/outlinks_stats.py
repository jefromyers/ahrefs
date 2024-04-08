from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, RequestMode, response_for


class OutlinksStatsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/outlinks-stats")
    _obj_name: str = PrivateAttr("metrics")
    # Required fields
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(OutlinksStatsRequest)
class OutlinksStatsResponse(BaseResponse):
    outgoing_links: int = Field(
        ...,
        title="Outgoing Links",
        description="The number of external links from the target.",
    )
    outgoing_links_dofollow: int = Field(
        ...,
        title="Outgoing Links Dofollow",
        description="The number of external dofollow links from the target.",
    )
    linked_domains: int = Field(
        ...,
        title="Linked Domains",
        description="The number of unique root domains linked from the target.",
    )
    linked_domains_dofollow: int = Field(
        ...,
        title="Linked Domains Dofollow",
        description="The number of unique root domains linked via dofollow links from the target.",
    )
