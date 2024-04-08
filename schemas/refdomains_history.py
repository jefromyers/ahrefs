from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    HistoryGrouping,
    RequestMode,
    response_for,
)


class RefDomainHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/refdomains-history")
    _obj_name: str = PrivateAttr("refdomains")
    # Required fields
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(RefDomainHistoryRequest)
class RefDomainHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    refdomains: int = Field(
        ...,
        title="Referring Domains",
        description="(5 units) The total number of unique domains linking to your target.",
    )
