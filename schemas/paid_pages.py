from datetime import date as DateType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class PaidPagesSelect(str, Enum):
    ads_count = "ads_count"
    ads_count_diff = "ads_count_diff"
    ads_count_prev = "ads_count_prev"
    keywords = "keywords"
    keywords_diff = "keywords_diff"
    keywords_diff_percent = "keywords_diff_percent"
    keywords_merged = "keywords_merged"
    keywords_prev = "keywords_prev"
    raw_url = "raw_url"
    raw_url_prev = "raw_url_prev"
    status = "status"
    sum_traffic = "sum_traffic"
    sum_traffic_merged = "sum_traffic_merged"
    sum_traffic_prev = "sum_traffic_prev"
    top_keyword = "top_keyword"
    top_keyword_best_position = "top_keyword_best_position"
    top_keyword_best_position_diff = "top_keyword_best_position_diff"
    top_keyword_best_position_kind = "top_keyword_best_position_kind"
    top_keyword_best_position_kind_prev = "top_keyword_best_position_kind_prev"
    top_keyword_best_position_prev = "top_keyword_best_position_prev"
    top_keyword_best_position_title = "top_keyword_best_position_title"
    top_keyword_best_position_title_prev = "top_keyword_best_position_title_prev"
    top_keyword_country = "top_keyword_country"
    top_keyword_country_prev = "top_keyword_country_prev"
    top_keyword_prev = "top_keyword_prev"
    top_keyword_volume = "top_keyword_volume"
    top_keyword_volume_prev = "top_keyword_volume_prev"
    traffic_diff = "traffic_diff"
    traffic_diff_percent = "traffic_diff_percent"
    url = "url"
    url_prev = "url_prev"
    value = "value"
    value_diff = "value_diff"
    value_diff_percent = "value_diff_percent"
    value_merged = "value_merged"
    value_prev = "value_prev"

    def __str__(self):
        return self.value


class PaidPagesRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/paid-pages")
    _obj_name: str = PrivateAttr("pages")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    date: DateType = Field(
        ..., description="A date to report metrics on in YYYY-MM-DD format."
    )
    select: List[PaidPagesSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(PaidPagesRequest)
class PaidPagesResponse(BaseResponse):
    ads_count: int | None = Field(
        None, title="Ads Count", description="The number of unique ads with a page."
    )
    ads_count_diff: int | None = Field(
        None,
        title="Ads Count Diff",
        description="The change in ads between your selected dates.",
    )
    ads_count_prev: int | None = Field(
        None,
        title="Ads Count Prev",
        description="The number of ads on the comparison date.",
    )
    keywords: int | None = Field(
        None,
        title="Keywords",
        description="The total number of keywords that your target ranks for in paid search results.",
    )
    keywords_diff: int = Field(
        None,
        title="Keywords Diff",
        description="The change in keywords between your selected dates.",
    )
    keywords_diff_percent: int = Field(
        None,
        title="Keywords Diff Percent",
        description="The change in keywords between your selected dates, in percents.",
    )
    keywords_merged: int = Field(
        None,
        title="Keywords Merged",
        description="The total number of keywords optimized for sorting.",
    )
    keywords_prev: int | None = Field(
        None,
        title="Keywords Prev",
        description="The keyword your target ranks for on the comparison date.",
    )
    raw_url: str = Field(
        None, title="Raw Url", description="The ranking page URL in encoded format."
    )
    raw_url_prev: str | None = Field(
        None,
        title="Raw Url Prev",
        description="The ranking page URL on the comparison date in encoded format.",
    )
    status: str = Field(
        None,
        title="Status",
        description="The status of a page: the new page that just started to rank in paid results (left), the lost page that disappeared from paid results (right), or no change (both).",
    )
    sum_traffic: int | None = Field(
        None,
        title="Sum Traffic",
        description="(10 units) An estimation of the monthly paid search traffic that a page gets from all the keywords that it ranks for.",
    )
    sum_traffic_merged: int = Field(
        None,
        title="Sum Traffic Merged",
        description="(10 units) The paid traffic field optimized for sorting.",
    )
    sum_traffic_prev: int | None = Field(
        None,
        title="Sum Traffic Prev",
        description="(10 units) The paid traffic on the comparison date.",
    )
    top_keyword: str | None = Field(
        None,
        title="Top Keyword",
        description="The keyword that brings the most paid traffic to a page.",
    )
    top_keyword_best_position: int | None = Field(
        None,
        title="Top Keyword Best Position",
        description="The ranking position that a page holds for its top keyword.",
    )
    top_keyword_best_position_diff: int | None = Field(
        None,
        title="Top Keyword Best Position Diff",
        description="The change in the top position between your selected dates.",
    )
    # Could be an Enum?
    top_keyword_best_position_kind: str | None = Field(
        None,
        title="Top Keyword Best Position Kind",
        description="The kind of the top position: organic, paid or a SERP feature.",
    )
    # Could be an Enum?
    top_keyword_best_position_kind_prev: str | None = Field(
        None,
        title="Top Keyword Best Position Kind Prev",
        description="The kind of the top position on the comparison date.",
    )
    top_keyword_best_position_prev: int | None = Field(
        None,
        title="Top Keyword Best Position Prev",
        description="The top position on the comparison date.",
    )
    top_keyword_best_position_title: str | None = Field(
        None,
        title="Top Keyword Best Position Title",
        description="The title displayed for the page in its top keyword's SERP.",
    )
    top_keyword_best_position_title_prev: str | None = Field(
        None,
        title="Top Keyword Best Position Title Prev",
        description="The title displayed for the page in its top keyword's SERP on the comparison date.",
    )
    # Could be an Country Enum?
    top_keyword_country: str | None = Field(
        None,
        title="Top Keyword Country",
        description="The country in which a page ranks for its top keyword.",
    )
    # Could be an Country Enum?
    top_keyword_country_prev: str | None = Field(
        None,
        title="Top Keyword Country Prev",
        description="The country in which a page ranks for its top keyword on the comparison date.",
    )
    top_keyword_prev: str | None = Field(
        None,
        title="Top Keyword Prev",
        description="The keyword that brings the most paid traffic to a page on the comparison date.",
    )
    top_keyword_volume: int | None = Field(
        None,
        title="Top Keyword Volume",
        description="(10 units) An estimation of the average monthly number of searches for the top keyword over the latest month or over the latest known 12 months of data depending on the volume_mode parameter.",
    )
    top_keyword_volume_prev: int | None = Field(
        None,
        title="Top Keyword Volume Prev",
        description="(10 units) The search volume on the comparison date.",
    )
    traffic_diff: int | None = Field(
        None,
        title="Traffic Diff",
        description="The change in traffic between your selected dates.",
    )
    traffic_diff_percent: int | None = Field(
        None,
        title="Traffic Diff Percent",
        description="The change in traffic between your selected dates, in percents.",
    )
    url: str | None = Field(None, title="Url", description="The ranking page URL.")
    url_prev: str | None = Field(
        None,
        title="Url Prev",
        description="The ranking page URL on the comparison date.",
    )
    value: int | None = Field(
        None,
        title="Value",
        description="(10 units) The estimated cost of a page's monthly paid search traffic, in cents.",
    )
    value_diff: int | None = Field(
        None,
        title="Value Diff",
        description="The change in traffic value between your selected dates.",
    )
    value_diff_percent: int | None = Field(
        None,
        title="Value Diff Percent",
        description="The change in traffic value between your selected dates, in percents.",
    )
    value_merged: int | None = Field(
        None,
        title="Value Merged",
        description="(10 units) The traffic value field optimized for sorting.",
    )
    value_prev: int | None = Field(
        None,
        title="Value Prev",
        description="(10 units) The traffic value on the comparison date.",
    )
