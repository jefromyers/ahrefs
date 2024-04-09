from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, Country, response_for


class RelatedTermsSelect(str, Enum):
    cpc = "cpc"
    cps = "cps"
    difficulty = "difficulty"
    first_seen = "first_seen"
    global_volume = "global_volume"
    keyword = "keyword"
    parent_topic = "parent_topic"
    serp_features = "serp_features"
    serp_last_update = "serp_last_update"
    traffic_potential = "traffic_potential"
    volume = "volume"

    def __str__(self):
        return self.value


class RelatedTermsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/keywords-explorer/related-terms")
    _obj_name: str = PrivateAttr("keywords")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    select: List[RelatedTermsSelect] = Field(
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
    keywords: str | None = Field(
        None,
        title="Keywords",
        description="A comma-separated list of keywords to show metrics for.",
    )


@response_for(RelatedTermsRequest)
class RelatedTermsResponse(BaseResponse):
    cpc: int | None = Field(
        None,
        title="CPC",
        description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in cents.",
    )
    cps: float | None = Field(
        None,
        title="CPS",
        description="Clicks Per Search (or CPS) is the ratio of Clicks to Keyword Search volume. It shows how many different search results get clicked, on average, when people search for the target keyword in a given country.",
    )
    difficulty: int | None = Field(
        None,
        title="Difficulty",
        description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.",
    )
    first_seen: DatetimeType | None = Field(
        None,
        title="First Seen",
        description="The date when we first checked search engine results for a keyword.",
    )
    global_volume: int | None = Field(
        None,
        title="Global Volume",
        description="(10 units) How many times per month, on average, people search for the target keyword across all countries in our database.",
    )
    keyword: str | None = Field(
        None,
        title="Keyword",
        description="Keyword",
    )
    parent_topic: str | None = Field(
        None,
        title="Parent Topic",
        description="Parent Topic determines if you can rank for your target keyword while targeting a more general topic on your page instead. To identify the Parent Topic, we take the #1 ranking page for your keyword and find the keyword responsible for sending the most traffic to that page.",
    )
    serps_feature: str | None = Field(
        None,
        title="SERP Feature",
        description="The enriched results on a search engine results page (SERP) that are not traditional organic results.",
    )
    serp_last_updated: DatetimeType | None = Field(
        None,
        title="SERP Last Updated",
        description="The date when we last checked search engine results for a keyword.",
    )
    traffic_potential: int | None = Field(
        None,
        title="Traffic Potential",
        description="(10 units) The sum of organic traffic that the #1 ranking page for your target keyword receives from all the keywords that it ranks for.",
    )
    volume: int | None = Field(
        None,
        title="Volume",
        description="(10 units) An estimation of the average monthly number of searches for a keyword over the latest known 12 months of data.",
    )
