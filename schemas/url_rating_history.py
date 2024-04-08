from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, HistoryGrouping, response_for


class UrlRatingHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/domain-rating-history")
    _obj_name: str = PrivateAttr("domain_ratings")
    date_to: DateType | None = Field(
        None, description="The end date of the historical period in YYYY-MM-DD format."
    )
    history_grouping: HistoryGrouping = Field(
        HistoryGrouping.monthly,
        title="History Grouping",
        description="The time interval used to group historical data. `daily`, `weekly`, `monthly`",
    )
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(UrlRatingHistoryRequest)
class UrlRatingHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    domain_rating: float = Field(
        ...,
        title="Domain Rating",
        description=(
            "The strength of your target page's backlink profile compared to the "
            "other websites in our database on a 100-point logarithmic scale."
        ),
    )
