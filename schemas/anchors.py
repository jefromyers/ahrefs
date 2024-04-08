from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import Dict, List

from pydantic import Field, PrivateAttr

from schemas.base import (
    AnchorsSelect,
    BaseRequest,
    BaseResponse,
    RequestMode,
    response_for,
)


class AnchorsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/anchors")
    _obj_name: str = PrivateAttr("anchors")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[AnchorsSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(AnchorsRequest)
class AnchorsResponse(BaseResponse):
    anchor: str | None = Field(
        None,
        title="Anchor",
        description="The clickable words in a link that point to a URL.",
    )
    dofollow_links: int | None = Field(
        None,
        title="Dofollow Links",
        description="The number of links with a given anchor to your target that don’t have the “nofollow” attribute.",
    )
    first_seen: DatetimeType | None = Field(
        None,
        title="First Seen",
        description="The date we first found a backlink to your target from the referring domain.",
    )
    last_seen: DatetimeType | None = Field(
        None,
        title="Last Seen",
        description="The date your target lost its last live backlink for the referring domain.",
    )
    links_to_target: int | None = Field(
        None,
        title="Links to Target",
        description="The number of backlinks from the referring domain to your target.",
    )
    lost_links: int | None = Field(
        None,
        title="Lost Links",
        description="The number of backlinks lost from the referring domain for the selected time period.",
    )
    new_links: int | None = Field(
        None,
        title="New Links",
        description="The number of new backlinks found from the referring domain for the selected time period.",
    )
    refdomains: int | None = Field(
        None,
        title="Referring Domains",
        description="(5 units) The number of unique domains linking to your target with a given anchor.",
    )
    top_domain_rating: float | None = Field(
        None,
        title="Top Domain Rating",
        description="The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.",
    )
