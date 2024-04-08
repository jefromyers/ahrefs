from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class PageHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/pages-history")
    _obj_name: str = PrivateAttr("pages")
    # Required fields
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(PageHistoryRequest)
class PageHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    pages: int = Field(
        ...,
        title="Pages",
        description=(
            "The total number of pages from a target ranking in the top 100 "
            "organic search results."
        ),
    )
