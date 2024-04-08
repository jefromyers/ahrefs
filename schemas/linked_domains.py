from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class LinkedDomainsSelect(str, Enum):
    dofollow_linked_domains = "dofollow_linked_domains"
    dofollow_links = "dofollow_links"
    dofollow_refdomains = "dofollow_refdomains"
    domain = "domain"
    domain_rating = "domain_rating"
    first_seen = "first_seen"
    is_root_domain = "is_root_domain"
    linked_domain_traffic = "linked_domain_traffic"
    linked_pages = "linked_pages"
    links_from_target = "links_from_target"

    def __str__(self):
        return self.value


class LinkedDomainsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/linkeddomains")
    _obj_name: str = PrivateAttr("linkeddomains")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[LinkedDomainsSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(LinkedDomainsRequest)
class LinkedDomainsResponse(BaseResponse):
    dofollow_linked_domains: int | None = Field(
        None,
        title="Dofollow Linked Domains",
        description="The number of unique root domains with dofollow links linked from the linked domain.",
    )
    dofollow_links: int | None = Field(
        None,
        title="Dofollow Links",
        description="The number of links from your target to the linked domain that don’t have the “nofollow” attribute.",
    )
    dofollow_refdomains: int | None = Field(
        None,
        title="Dofollow Refdomains",
        description="(5 units) The number of unique domains with dofollow links to the linked domain.",
    )
    domain: str | None = Field(
        None,
        title="Domain",
        description="A linked domain that has at least one link from your target.",
    )
    domain_rating: float | None = Field(
        None,
        title="Domain Rating",
        description="The strength of a domain's backlink profile compared to the others in our database on a 100-point scale.",
        ge=-3.402823669209385e38,
        le=3.402823669209385e38,
    )
    first_seen: DatetimeType | None = Field(
        None,
        title="First Seen",
        description="The date we first found a link to the linked domain from your target.",
    )
    is_root_domain: bool | None = Field(
        None,
        title="Is Root Domain",
        description="The domain name is a root domain name.",
    )
    linked_domain_traffic: int | None = Field(
        None,
        title="Linked Domain Traffic",
        description="(10 units) The linked domain’s estimated monthly organic traffic from search",
    )
    linked_pages: int | None = Field(
        None,
        title="Linked Pages",
        description="The number of the domain's pages linked from your target.",
    )
    links_from_target: int | None = Field(
        None,
        title="Links From Target",
        description="The number of links to the linked domain from your target.",
    )
