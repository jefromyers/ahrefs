from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import Dict, List

from pydantic import Field, PrivateAttr

from schemas.base import (
    Aggregation,
    AllBacklinksSelect,
    BaseRequest,
    BaseResponse,
    BrokenRedirectReason,
    DiscoveredStatus,
    DropReason,
    LinkType,
    LostReason,
    RequestMode,
    TldClassSource,
    TldClassTarget,
    response_for,
)


class AllBacklinksRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/all-backlinks")
    _obj_name: str = PrivateAttr("backlinks")
    aggregation: Aggregation = Field(
        Aggregation.similar_links, description="The backlinks grouping mode."
    )
    # TODO MISSING: Add history enum
    limit: int = Field(1_000, description="The number of results to return.")
    mode: RequestMode = Field(
        RequestMode.subdomains,
        title="Mode",
        description=(
            "The scope of the search based on the target you entered. `exact`, `prefix`, `domain`, `subdomains`"
        ),
    )
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    order_by: int | None = Field(
        None,
        description="A column to order results by. See response schema for valid column identifiers.",
    )

    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    timeout: int | None = Field(
        None, description="A manual timeout duration in seconds."
    )
    # TODO MISSING: Add where filtering
    select: List[AllBacklinksSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")

    def make_params(self) -> Dict[str, str]:
        params = super().dict(exclude={"retry", "cache"})
        if "select" in params and isinstance(params["select"], list):
            params["select"] = ",".join([str(item) for item in params["select"]])

        filtered_params = {k: v for k, v in params.items() if v is not None}
        return filtered_params


# TODO: There seem to be AllBacklinksSelect that are not in the response schema, need to double check
@response_for(AllBacklinksRequest)
class AllBacklinksResponse(BaseResponse):
    ahrefs_rank_source: int | None = Field(
        None,
        title="Ahrefs Rank Source",
        description=(
            "The strength of the referring domain's backlink profile compared to "
            "the other websites in our database, with rank #1 being the strongest."
        ),
    )
    ahrefs_rank_target: int | None = Field(
        None,
        title="Ahrefs Rank Target",
        description=(
            "The strength of the target domain's backlink profile compared to the other "
            "websites in our database, with rank #1 being the strongest."
        ),
    )
    alt: str | None = Field(None, description="The alt attribute of the link.")
    anchor: str | None = Field(
        None, description="The clickable words in a link that point to a URL"
    )
    broken_redirect_new_target: str | None = Field(
        None,
        title="Broken Redirect New Target",
        description="The new destination of a modified redirect.",
    )
    broken_redirect_reason: BrokenRedirectReason | None = Field(
        None,
        title="Broken Redirect Reason",
        description="The reason the redirect was considered broken during the last crawl.",
    )

    broken_redirect_source: str | None = Field(
        None,
        title="Broken Redirect Source",
        description=(
            "The redirecting URL that was modified, causing "
            "the redirect to become broken."
        ),
    )
    class_c: int | None = Field(
        None,
        title="Class C",
        description=(
            "(5 units) The number of unique class_c subnets linking to "
            "the referring page."
        ),
    )
    discovered_status: DiscoveredStatus | None = Field(
        None,
        title="Discovered Status",
        description=(
            "The reason the link was discovered during the last crawl: "
            "the page was crawled for the first time, the link was added to "
            "the page, or the link re-appeared after being removed."
        ),
    )
    domain_rating_source: float | None = Field(
        None,
        title="Domain Rating Source",
        description=(
            "The strength of the referring domain's backlink profile compared "
            "to the others in our database on a 100-point scale."
        ),
    )
    domain_rating_target: float | None = Field(
        None,
        title="Domain Rating Target",
        description=(
            "The strength of the referring domain's backlink profile compared "
            "to the others in our database on a 100-point scale."
        ),
    )
    drop_reason: DropReason | None = Field(
        None,
        title="Drop Reason",
        description="The reason we removed the link from our index.",
    )
    encoding: str | None = Field(
        None,
        title="Encoding",
        description="The character set encoding of the referring page HTML.",
    )
    first_seen: DateType | None = Field(
        None,
        title="First Seen",
        description="The date the referring page URL was first discovered.",
    )
    first_seen_link: DateType | None = Field(
        None,
        title="First Seen Link",
        description=(
            "The date we first found a backlink to your target on a "
            "given referring page."
        ),
    )
    http_code: int | None = Field(
        None,
        title="HTTP Code",
        description=(
            "The return code from HTTP protocol returned during the "
            "referring page crawl."
        ),
    )
    http_crawl: bool | None = Field(
        None,
        title="HTTP Crawl",
        description=(
            "The link was discovered without executing "
            "javascript and rendering the page."
        ),
    )
    ip_source: str | None = Field(
        None, title="IP Source", description="The referring domain IP address."
    )
    is_alternate: bool | None = Field(
        None,
        title="Is Alternate",
        description="The link with the rel=`alternate` attribute.",
    )
    is_canonical: bool | None = Field(
        None,
        title="Is Canonical",
        description="The link with the rel=`canonical` attribute.",
    )
    is_content: bool | None = Field(
        None,
        title="Is Content",
        description="The link was found in the biggest piece of content on the page.",
    )
    is_dofollow: bool | None = Field(
        None,
        title="Is Dofollow",
        description="The link has no special nofollow attribute.",
    )
    is_form: bool | None = Field(
        None,
        title="Is Form",
        description="The link was found in a form HTML tag.",
    )
    is_frame: bool | None = Field(
        None,
        title="Is Frame",
        description="The link was found in an iframe HTML tag.",
    )
    is_image: bool | None = Field(
        None,
        title="Is Image",
        description="The link is a regular link that has an image inside their href attribute.",
    )
    is_lost: bool | None = Field(
        None,
        title="Is Lost",
        description="The link currently does not exist anymore.",
    )
    is_new: bool | None = Field(
        None,
        title="Is New",
        description="The link was discovered on the last crawl.",
    )
    is_nofollow: bool | None = Field(
        None,
        title="Is Nofollow",
        description="The link or the referring page has the nofollow attribute set.",
    )
    is_redirect: bool | None = Field(
        None,
        title="Is Redirect",
        description="The link pointing to your target via a redirect.",
    )
    is_redirect_lost: bool | None = Field(
        None,
        title="Is Redirect Lost",
        description="The redirected link currently does not exist anymore.",
    )
    is_root_source: bool | None = Field(
        None,
        title="Is Root Source",
        description="The referring domain name is a root domain name.",
    )
    is_root_target: bool | None = Field(
        None,
        title="Is Root Target",
        description="The target domain name is a root domain name.",
    )
    is_rss: bool | None = Field(
        None,
        title="Is Rss",
        description="The link was found in an RSS feed.",
    )
    is_sponsored: bool | None = Field(
        None,
        title="Is Sponsored",
        description="The link has the Sponsored attribute set in the referring page HTML.",
    )
    is_text: bool | None = Field(
        None,
        title="Is Text",
        description="The link is a standard href hyperlink.",
    )
    is_ugc: bool | None = Field(
        None,
        title="Is User Generated Content",
        description="The link has the User Generated Content attribute set in the referring page HTML.",
    )
    js_crawl: bool | None = Field(
        None,
        title="JS Crawl",
        description="The link was discovered by executing javascript and rendering the page.",
    )
    languages: List[str] | None = Field(
        None,
        title="Languages",
        description=(
            "The languages listed in the referring page metadata or detected "
            "by the crawler to appear in the HTML."
        ),
    )
    last_seen: DatetimeType | None = Field(
        None,
        title="Last Seen",
        description="The date we discovered that the link was lost.",
    )
    last_visited: DatetimeType | None = Field(
        None,
        title="Last Visited",
        description="The date we last verified a live link to your target page.",
    )
    link_group_count: int | None = Field(
        None,
        title="Link Group Count",
        description=(
            "The number of backlinks that were grouped together based on the aggregation "
            "parameter. This field cannot be used with aggregation 'all'."
        ),
    )
    link_type: LinkType | None = Field(
        None,
        title="Link Type",
        description="The kind of the backlink.",
    )
    linked_domains_source_domain: int | None = Field(
        None,
        title="Linked Domains Source Domain",
        description="The number of unique root domains linked from the referring domain.",
    )
    linked_domains_source_page: int | None = Field(
        None,
        title="Linked Domains Source Page",
        description="The number of unique root domains linked from the referring page.",
    )
    linked_domains_target_domain: int | None = Field(
        None,
        title="Linked Domains Target Domain",
        description="The number of unique root domains linked from the target domain.",
    )
    links_external: int | None = Field(
        None,
        title="Links External",
        description="The number of external links from the referring page.",
    )
    links_internal: int | None = Field(
        None,
        title="Links Internal",
        description="The number of internal links from the referring page.",
    )
    lost_reason: LostReason | None = Field(
        None,
        title="Lost Reason",
        description="The reason the link was lost during the last crawl.",
    )
    name_source: str | None = Field(
        None,
        title="Name Source",
        description="The complete referring domain name, including subdomains.",
    )
    name_target: str | None = Field(
        None,
        title="Name Target",
        description="The complete target domain name, including subdomains.",
    )
    noindex: bool | None = Field(
        None,
        title="Noindex",
        description="The referring page has the noindex meta attribute.",
    )
    page_size: int | None = Field(
        None,
        title="Page Size",
        description="The size in bytes of the referring page content.",
    )
    port_source: int | None = Field(
        None,
        title="Port Source",
        description="The network port of the referring page URL.",
    )
    port_target: int | None = Field(
        None,
        title="Port Target",
        description="The network port of the target page URL.",
    )
    positions: int | None = Field(
        None,
        title="Positions",
        description="The number of keywords that the referring page ranks for in the top 100 positions.",
    )
    powered_by: List[str] | None = Field(
        None,
        title="Powered By",
        description="Web technologies used to build and serve the referring page content.",
    )
    redirect_code: int | None = Field(
        None,
        title="Redirect Code",
        description="The HTTP status code of a referring page pointing to your target via a redirect.",
    )
    redirect_kind: List[int] | None = Field(
        None,
        title="Redirect Kind",
        description="The HTTP status codes returned by the target redirecting URL or redirect chain.",
    )
    refdomains_source: int | None = Field(
        None,
        title="Referring Domains Source",
        description="(5 units) The number of unique referring domains linking to the referring page.",
    )
    refdomains_source_domain: int | None = Field(
        None,
        title="Referring Domains Source Domain",
        description="(5 units) The number of unique referring domains linking to the referring domain.",
    )
    refdomains_target_domain: int | None = Field(
        None,
        title="Referring Domains Target Domain",
        description="(5 units) The number of unique referring domains linking to the target domain.",
    )
    root_name_source: str | None = Field(
        None,
        title="Root Name Source",
        description="The root domain name of the referring domain, not including subdomains.",
    )
    root_name_target: str | None = Field(
        None,
        title="Root Name Target",
        description="The root domain name of the target domain, not including subdomains.",
    )
    snippet_left: str | None = Field(
        None,
        title="Snippet Left",
        description="The snippet of text appearing just before the link.",
    )
    snippet_right: str | None = Field(
        None,
        title="Snippet Right",
        description="The snippet of text appearing just after the link.",
    )
    source_page_author: str | None = Field(
        None,
        title="Source Page Author",
        description="The author of the referring page.",
    )
    title: str | None = Field(
        None,
        title="Title",
        description="The html title of the referring page.",
    )
    tld_class_source: TldClassSource | None = Field(
        None,
        title="TLD Class Source",
        description="The top level domain class of the referring domain.",
    )
    tld_class_target: TldClassTarget | None = Field(
        None,
        title="TLD Class Target",
        description="The top level domain class of the target domain.",
    )
    traffic: int | None = Field(
        None,
        title="Traffic",
        description="(10 units) The referring page's estimated monthly organic traffic from search.",
    )
    traffic_domain: int | None = Field(
        None,
        title="Traffic Domain",
        description=(
            "(10 units) The referring domain's estimated monthly organic "
            "traffic from search."
        ),
    )
    url_from: str | None = Field(
        None,
        title="URL From",
        description="The URL of the page containing a link to your target.",
    )
    url_from_plain: str | None = Field(
        None,
        title="URL From Plain",
        description="he referring page URL optimized for use as a filter.",
    )
    url_rating_source: float | None = Field(
        None,
        title="URL Rating Source",
        description=(
            "The strength of the referring page's backlink profile compared "
            "to the others in our database on a 100-point scale."
        ),
    )
    url_redirect: List[str] | None = Field(
        None,
        title="URL Redirect",
        description="The target redirecting URL or redirect chain.",
    )
    url_to: str | None = Field(
        None,
        title="URL To",
        description="The URL the backlink points to.",
    )
    url_to_plain: str | None = Field(
        None,
        title="URL To Plain",
        description="The target page URL optimized for use as a filter.",
    )
