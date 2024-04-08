from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class BestByExternalLinksSelect(str, Enum):
    dofollow_to_target = "dofollow_to_target"
    first_seen_link = "first_seen_link"
    http_code_target = "http_code_target"
    last_seen = "last_seen"
    last_visited_source = "last_visited_source"
    last_visited_target = "last_visited_target"
    links_to_target = "links_to_target"
    lost_links_to_target = "lost_links_to_target"
    new_links_to_target = "new_links_to_target"
    nofollow_to_target = "nofollow_to_target"
    redirects_to_target = "redirects_to_target"
    refdomains_target = "refdomains_target"
    target_redirect = "target_redirect"
    title_target = "title_target"
    top_domain_rating_source = "top_domain_rating_source"
    url_rating_target = "url_rating_target"
    url_to = "url_to"
    url_to_plain = "url_to_plain"

    def __str__(self):
        return self.value


class BestByExternalLinksRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/best-by-external-links")
    _obj_name: str = PrivateAttr("pages")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[BestByExternalLinksSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(BestByExternalLinksRequest)
class BestByExternalLinksResponse(BaseResponse):
    dofollow_to_target: int | None = Field(
        None,
        title="Dofollow To Target",
        description="The number of links to your target page that don’t have the “nofollow” attribute.",
    )
    first_seen_link: DatetimeType | None = Field(
        None,
        title="First Seen Link",
        description="The date we first found a link to your target.",
    )
    http_code_target: int | None = Field(
        None,
        title="HTTP Code Target",
        description="The return code from HTTP protocol returned during the target page crawl.",
    )
    languages_target: List[str] | None = Field(
        None,
        title="Languages Target",
        description="The languages listed in the target page metadata or detected by the crawler to appear in the HTML.",
    )
    powered_by_target: List[str] | None = Field(
        None,
        title="Powered By Target",
        description="Web technologies used to build and serve the target page content.",
    )
    last_seen: DatetimeType | None = Field(
        None,
        title="Last Seen",
        description="The date your target page lost its last live link.",
    )
    last_visited_source: DatetimeType | None = Field(
        None,
        title="Last Visited Source",
        description="The date we last verified a live link to your target page.",
    )
    last_visited_target: DatetimeType | None = Field(
        None,
        title="Last Visited Target",
        description="The date we last crawled your target page.",
    )
    links_to_target: int | None = Field(
        None,
        title="Links To Target",
        description="The number of inbound backlinks the target page has.",
    )
    lost_links_to_target: int | None = Field(
        None,
        title="Lost Links To Target",
        description="The number of backlinks lost during the selected time period.",
    )
    new_links_to_target: int | None = Field(
        None,
        title="New Links To Target",
        description="The number of new backlinks found during the selected time period.",
    )
    nofollow_to_target: int | None = Field(
        None,
        title="Nofollow To Target",
        description="The number of links to your target page that have the “nofollow” attribute.",
    )
    redirects_to_target: int | None = Field(
        None,
        title="Redirects To Target",
        description="The number of inbound redirects to your target page.",
    )
    refdomains_target: int | None = Field(
        None,
        title="Refdomains Target",
        description="(5 units) The number of unique referring domains linking to the target page.",
    )
    target_redirect: str | None = Field(
        None, title="Target Redirect", description="The target's redirect if any."
    )
    title_target: str | None = Field(
        None, title="Title Target", description="The html title of the target page."
    )
    top_domain_rating_source: float | None = Field(
        None,
        title="Top Domain Rating Source",
        description="The highest Domain Rating (DR) counted out of all referring domains. DR shows the strength of a website’s backlink profile compared to the others in our database on a 100-point scale.",
        ge=-3.402823669209385e38,
        le=3.402823669209385e38,
    )
    url_rating_target: float | None = Field(
        None,
        title="Url Rating Target",
        description="The strength of the target page's backlink profile compared to the others in our database on a 100-point scale.",
        ge=-3.402823669209385e38,
        le=3.402823669209385e38,
    )
    url_to: str | None = Field(
        None, title="Url To", description="The URL the backlink points to."
    )
    url_to_plain: str | None = Field(
        None,
        title="Url To Plain",
        description="The target page URL optimized for use as a filter.",
    )
