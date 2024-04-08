from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import Dict, List

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    Country,
    OrganicKeywordsSelect,
    VolumeMode,
    response_for,
)


class OrganicKeywordsRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/organic-keywords")
    _obj_name: str = PrivateAttr("keywords")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    volume_mode: VolumeMode = Field(
        VolumeMode.monthly,
        description="The volume mode to use for the request. Defaults to 'monthly'.",
    )
    # Required fields
    country: Country | None = Field(
        ...,
        title="Country Code",
        description="The country code to use for the request. Defaults to None.",
    )
    date: DateType = Field(
        ..., description="A date to report metrics on in YYYY-MM-DD format."
    )
    select: List[OrganicKeywordsSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


# TODO: NEED TO GO THROUGH AND VARIFY ALL FIELDS ARE PRESENT
@response_for(OrganicKeywordsRequest)
class OrganicKeywordsResponse(BaseResponse):
    best_position: int | None = Field(
        None,
        title="Best Position",
        description="The top position your target ranks for in the organic search results for a keyword.",
    )
    best_position_diff: int | None = Field(
        None,
        title="Best Position Diff",
        description="The change in position between your selected dates.",
    )
    best_position_has_thumbnail: bool | None = Field(
        None,
        title="Best Position Has Thumbnail",
        description="The top position has a thumbnail.",
    )
    best_position_has_thumbnail_prev: bool | None = Field(
        None,
        title="Best Position Has Thumbnail Prev",
        description="The top position has a thumbnail on the comparison date.",
    )
    best_position_has_video: bool | None = Field(
        None,
        title="Best Position Has Video",
        description="The top position has a video.",
    )
    best_position_has_video_prev: bool | None = Field(
        None,
        title="Best Position Has Video Prev",
        description="The top position has a video on the comparison date.",
    )
    # TODO: Would be more useful as an enum?
    best_position_kind: str | None = Field(
        None,
        title="Best Position Kind",
        description="The kind of the top position: organic, paid, or a SERP feature.",
    )
    # TODO: Would be more useful as an enum?
    best_position_kind_merged: str = Field(
        None,
        title="Best Position Kind Merged",
        description="The kind of the top position optimized for sorting.",
    )
    # TODO: Would be more useful as an enum?
    best_position_kind_prev: str | None = Field(
        None,
        title="Best Position Kind Prev",
        description="The kind of the top position on the comparison date.",
    )
    # TODO: Would be more useful as an enum?
    best_position_prev: int | None = Field(
        None,
        title="Best Position Prev",
        description="The top position on the comparison date.",
    )
    # TODO: Would be more useful as an enum?
    best_position_set: str = Field(
        None,
        title="Best Position Set",
        description="The ranking group of the top position.",
    )
    # TODO: Would be more useful as an enum?
    best_position_set_prev: str | None = Field(
        None,
        title="Best Position Set Prev",
        description="The ranking group of the top position on the comparison date.",
    )
    best_position_url: str | None = Field(
        None,
        title="Best Position URL",
        description="The ranking URL in organic search results.",
    )
    best_position_url_prev: str | None = Field(
        None,
        title="Best Position URL Prev",
        description="The ranking URL on the comparison date.",
    )
    cpc: int | None = Field(
        None,
        title="CPC",
        description="Cost Per Click shows the average price that advertisers pay for each ad click in paid search results for a keyword, in cents.",
    )
    cpc_merged: int | None = Field(
        None, title="CPC Merged", description="The CPC field optimized for sorting."
    )
    cpc_prev: int | None = Field(
        None, title="CPC Prev", description="The CPC metric on the comparison date."
    )
    is_best_position_set_top_11_50: bool = Field(
        None,
        title="Is Best Position Set Top 11 50",
        description="The ranking group of the top position is 11-50.",
    )
    is_best_position_set_top_11_50_prev: bool | None = Field(
        None,
        title="Is Best Position Set Top 11 50 Prev",
        description="The ranking group of the top position was 11-50 on the comparison date.",
    )
    is_best_position_set_top_3: bool = Field(
        None,
        title="Is Best Position Set Top 3",
        description="The ranking group of the top position is Top 3.",
    )
    is_best_position_set_top_3_prev: bool | None = Field(
        None,
        title="Is Best Position Set Top 3 Prev",
        description="The ranking group of the top position was Top 3 on the comparison date.",
    )
    is_best_position_set_top_4_10: bool = Field(
        None,
        title="Is Best Position Set Top 4 10",
        description="The ranking group of the top position is 4-10.",
    )
    is_best_position_set_top_4_10_prev: bool | None = Field(
        None,
        title="Is Best Position Set Top 4 10 Prev",
        description="The ranking group of the top position was 4-10 on the comparison date.",
    )
    keyword: str | None = Field(
        None, title="Keyword", description="The keyword your target ranks for."
    )
    keyword_difficulty: int | None = Field(
        None,
        title="Keyword Difficulty",
        description="(10 units) An estimation of how hard it is to rank in the top 10 organic search results for a keyword on a 100-point scale.",
    )
    keyword_difficulty_merged: int | None = Field(
        None,
        title="Keyword Difficulty Merged",
        description="(10 units) The keyword difficulty field optimized for sorting.",
    )
    keyword_difficulty_prev: int | None = Field(
        None,
        title="Keyword Difficulty Prev",
        description="(10 units) The keyword difficulty on the comparison date.",
    )
    keyword_merged: str = Field(
        None,
        title="Keyword Merged",
        description="The keyword field optimized for sorting.",
    )
    keyword_prev: str | None = Field(
        None,
        title="Keyword Prev",
        description="The keyword your target ranks for on the comparison date.",
    )
    language: str = Field(None, title="Language", description="The SERP language.")
    language_prev: str | None = Field(
        None,
        title="Language Prev",
        description="The SERP language on the comparison date.",
    )
    last_update: DatetimeType = Field(
        None,
        title="Last Update",
        description="The date when we last checked search engine results for a keyword.",
    )
    last_update_prev: DatetimeType | None = Field(
        None,
        title="Last Update Prev",
        description="The date when we checked search engine results up to the comparison date.",
    )
    serp_features: List[str] | None = Field(
        None,
        title="SERP Features",
        description="The SERP features that appear in search results for a keyword.",
    )
    serp_features_count_prev: int | None = Field(
        None,
        title="SERP Features Count Prev",
        description="The number of SERP features on the comparison date.",
    )
    serp_target_main_positions_count: int = Field(
        None,
        title="SERP Target Main Positions Count",
        description="The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and Tweets.",
    )
    serp_target_main_positions_count_prev: int | None = Field(
        None,
        title="SERP Target Main Positions Count Prev",
        description="The number of target URLs ranking for a keyword excluding positions in Sitelinks, Top stories, Image packs, and Tweets on the comparison date.",
    )
    serp_features_merged: List[str] | None = Field(
        None,
        title="SERP Features Merged",
        description="The SERP features field optimized for sorting.",
    )

    serp_target_positions_count: int = Field(
        None,
        title="SERP Target Positions Count",
        description="The number of target URLs ranking for a keyword.",
    )
    serp_target_positions_count_prev: int | None = Field(
        None,
        title="SERP Target Positions Count Prev",
        description="The number of target URLs ranking for a keyword on the comparison date.",
    )
    status: str = Field(
        None,
        title="Status",
        description="The status of a page: the new page that just started to rank (left), the lost page that disappeared from search results (right), or no change (both).",
    )
    sum_paid_traffic: int | None = Field(
        None,
        title="Sum Paid Traffic",
        description="(10 units) An estimation of the number of monthly visits that your target gets from paid search for a keyword.",
    )
    sum_traffic: int | None = Field(
        None,
        title="Sum Traffic",
        description="(10 units) An estimation of the number of monthly visitors that your target gets from organic search for a keyword.",
    )
    sum_traffic_merged: int = Field(
        None,
        title="Sum Traffic Merged",
        description="(10 units) The traffic field optimized for sorting.",
    )
    sum_traffic_prev: int | None = Field(
        None,
        title="Sum Traffic Prev",
        description="(10 units) The traffic on the comparison date.",
    )
    volume: int | None = Field(
        None,
        title="Volume",
        description="(10 units) An estimation of the number of searches for a keyword over the latest month.",
    )
    volume_merged: int | None = Field(
        None,
        title="Volume Merged",
        description="(10 units) The search volume field optimized for sorting.",
    )
    volume_prev: int | None = Field(
        None,
        title="Volume Prev",
        description="(10 units) The search volume on the comparison date.",
    )
    words: int | None = Field(
        None, title="Words", description="The number of words in a keyword."
    )
    words_merged: int = Field(
        None,
        title="Words Merged",
        description="The number of words in a keyword optimized for sorting.",
    )
    words_prev: int | None = Field(
        None,
        title="Words Prev",
        description="The number of words in a keyword on the comparison date.",
    )
