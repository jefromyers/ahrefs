from datetime import date as DateType
from typing import Dict, List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, TopPagesSelect, response_for


class TopPagesRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/top-pages")
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
    select: List[TopPagesSelect] = Field(
        ...,
        title="Select",
        description=(
            "A comma-separated list of columns to return. See response schema "
            "for valid column identifiers."
        ),
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(TopPagesRequest)
class TopPagesResponse(BaseResponse):
    keywords: int | None = Field(
        None,
        title="Keywords",
        description="The total number of keywords that your target ranks for in the top 100 organic search results.",
    )
    keywords_diff: int | None = Field(
        None,
        title="Keywords Diff",
        description="The change in keywords between your selected dates.",
    )
    keywords_diff_percent: int | None = Field(
        None,
        title="Keywords Diff Percent",
        description="The change in keywords between your selected dates, in percents.",
    )
    keywords_merged: int | None = Field(
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
        description="The status of a page: the new page that just started to rank (left), the lost page that disappeared from search results (right), or no change (both).",
    )
    sum_traffic: int | None = Field(
        None,
        title="Sum Traffic",
        description="(10 units) An estimation of the monthly organic search traffic that a page gets from all the keywords that it ranks for.",
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
    top_keyword: str | None = Field(
        None,
        title="Top Keyword",
        description="The keyword that brings the most organic traffic to a page.",
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
    top_keyword_best_position_kind: str | None = Field(
        None,
        title="Top Keyword Best Position Kind",
        description="The kind of the top position: organic, paid or a SERP feature.",
    )
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
    top_keyword_country: str | None = Field(
        None,
        title="Top Keyword Country",
        description="The country in which a page ranks for its top keyword.",
    )
    top_keyword_country_prev: str | None = Field(
        None,
        title="Top Keyword Country Prev",
        description="The country in which a page ranks for its top keyword on the comparison date.",
    )
    top_keyword_prev: str | None = Field(
        None,
        title="Top Keyword Prev",
        description="The keyword that brings the most organic traffic to a page on the comparison date.",
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
        description="(10 units) The estimated value of a page's monthly organic search traffic, in cents.",
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
