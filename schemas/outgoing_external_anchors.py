from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class OutgoingExternalAnchorsSelect(str, Enum):
    anchor = "anchor"
    dofollow_links = "dofollow_links"
    first_seen = "first_seen"
    linked_domains = "linked_domains"
    linked_pages = "linked_pages"
    links_from_target = "links_from_target"

    def __str__(self):
        return self.value


class OutgoingExternalAnchorsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/linked-anchors-external")
    _obj_name: str = PrivateAttr("linkedanchors")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[OutgoingExternalAnchorsSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(OutgoingExternalAnchorsRequest)
class OutgoingExternalAnchorsResponse(BaseResponse):
    anchor: str | None = Field(
        None,
        title="Anchor",
        description="The clickable words in a link that point to a URL.",
    )
    dofollow_links: int | None = Field(
        None,
        title="Dofollow Links",
        description="The number of outbound links with a given anchor from your target that don’t have the “nofollow” attribute.",
    )
    first_seen: DateType | None = Field(
        None,
        title="First Seen",
        description="The date we first found a link with a given anchor on your target.",
    )
    linked_domains: int | None = Field(
        None,
        title="Linked Domains",
        description="The number of unique domains linked from your target with a given anchor.",
    )
    linked_pages: int | None = Field(
        None,
        title="Linked Pages",
        description="The number of unique pages linked from your target with a given anchor.",
    )
    links_from_target: int | None = Field(
        None,
        title="Links From Target",
        description="The number of outbound links your target has with a given anchor.",
    )
