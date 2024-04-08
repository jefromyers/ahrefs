from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import Dict, List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, RefdomainsSelect, response_for


class RefdomainsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/refdomains")
    _obj_name: str = PrivateAttr("refdomains")
    # TODO MISSING: Add history filtering
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[RefdomainsSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(RefdomainsRequest)
class RefdomainsResponse(BaseResponse):
    dofollow_linked_domains: int | None = Field(
        None,
        title="Dofollow Linked Domains",
        description=(
            "The number of unique root domains with dofollow links "
            "linked from the referring domain."
        ),
    )
    dofollow_links: int | None = Field(
        None,
        title="Dofollow Links",
        description="The number of links from the referring domain to your target that don't have the “nofollow” attribute.",
    )

    dofollow_refdomains: int | None = Field(
        None,
        title="Dofollow Referring Domains",
        description="(5 units) The number of unique domains with dofollow links to the referring domain.",
    )
    domain: str | None = Field(
        None,
        title="Domain",
        description="A referring domain that has at least one link to your target.",
    )

    domain_rating: float | None = Field(
        None,
        title="Domain Rating",
        description="The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.",
    )

    first_seen: DatetimeType | None = Field(
        None,
        title="First Seen",
        description="The date we first found a backlink to your target from the referring domain.",
    )

    ip_source: str | None = Field(
        None, title="IP Source", description="The referring domain IP address."
    )
    is_root_domain: bool | None = Field(
        None,
        title="Is Root Domain",
        description="The domain name is a root domain name.",
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

    positions_source_domain: int | None = Field(
        None,
        title="Positions Source Domain",
        description="The number of keywords that the referring domain ranks for in the top 100 positions.",
    )

    traffic_domain: int | None = Field(
        None,
        title="Traffic Domain",
        description="(10 units) The referring domain's estimated monthly organic traffic from search.",
    )
