from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, Country, response_for


class SerpsOverviewSelect(str, Enum):
    ahrefs_rank = "ahrefs_rank"
    backlinks = "backlinks"
    domain_rating = "domain_rating"
    keywords = "keywords"
    position = "position"
    refdomains = "refdomains"
    title = "title"
    top_keyword = "top_keyword"
    top_keyword_volume = "top_keyword_volume"
    traffic = "traffic"
    type = "type"
    paid_top = "paid_top"
    update_date = "update_date"
    url = "url"
    url_rating = "url_rating"
    value = "value"

    def __str__(self):
        return self.value


# I'm not sure I understand how this differs from the others
class SerpsOverviewRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/keywords-explorer/serp-overview")
    _obj_name: str = PrivateAttr("positions")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[SerpsOverviewSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    country: Country = Field(
        ...,
        title="Country",
        description="The country to get data for.",
    )
    keyword: str | None = Field(
        None,
        title="Keyword",
        description="A keywords to show metrics for.",
    )


@response_for(SerpsOverviewRequest)
class SerpsOverviewResponse(BaseResponse):
    ahrefs_rank: int | None = Field(
        None,
        title="Ahrefs Rank",
        description="The strength of a domain's backlink profile compared to the other websites in our database, with rank #1 being the strongest.",
    )
    backlinks: int | None = Field(
        None,
        title="Backlinks",
        description="The total number of links from other websites pointing to a search result.",
    )
    domain_rating: float | None = Field(
        None,
        description=(
            "The strength of your target's backlink profile compared to the "
            "other websites in our database on a 100-point logarithmic scale."
        ),
    )
    keywords: str | None = Field(
        None,
        title="Keywords",
        description="The total number of keywords that a search result ranks for in the top 100 organic positions.",
    )
    position: int | None = Field(
        None,
        title="Position",
        description="The position of the search result in SERP.",
    )
    refdomains: int | None = Field(
        None,
        title="Referring Domains",
        description="(5 units) The total number of unique domains linking to a search result.",
    )
    traffic: int | None = Field(
        None,
        title="Traffic",
        description="The title of a ranking page.",
    )
    top_keyword: str | None = Field(
        None,
        title="Top Keyword",
        description="The keyword that brings the most organic traffic to a search result.",
    )
    top_keyword_volume: int | None = Field(
        None,
        title="Top Keyword Volume",
        description="(10 units) An estimation of the average monthly number of searches for the top keyword over the latest known 12 months of data.",
    )
    traffic: int | None = Field(
        None,
        title="Traffic",
        description="(10 units) An estimation of the monthly organic search traffic that a result gets from all the keywords that it ranks for.",
    )
    # Could be an enum
    type: List[str] | None = Field(
        None,
        title="Type",
        description="The kind of the position: organic, paid, or a SERP feature.",
    )
    update_date: DatetimeType | None = Field(
        None,
        title="Update Date",
        description="The date when we checked search engine results for a keyword.",
    )
    url: str | None = Field(
        None,
        title="URL",
        description="The URL of a ranking page.",
    )
    url_rating: float | None = Field(
        None,
        title="URL Rating",
        description="The strength of a URL's backlink profile compared to the other URLs in our database on a 100-point logarithmic scale.",
    )
    value: int | None = Field(
        None,
        title="Value",
        description="(10 units) The estimated value of a page’s monthly organic search traffic.",
    )
