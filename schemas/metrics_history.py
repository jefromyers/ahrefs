from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class MetricsHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/metrics-history")
    _obj_name: str = PrivateAttr("metrics")
    # Required fields
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")


@response_for(MetricsHistoryRequest)
class MetricsHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    org_traffic: int = Field(
        ...,
        title="Organic Traffic",
        description=(
            "(10 units) The estimated number of monthly visitors that your "
            "target gets from organic search."
        ),
    )
    paid_traffic: int = Field(
        ...,
        title="Paid Traffic",
        description=(
            "(10 units) The estimated number of monthly visitors that your "
            "target gets from paid search."
        ),
    )
    org_cost: int | None = Field(
        ...,
        title="Organic Cost",
        description=(
            "(10 units) The estimated cost of your target's monthly "
            "organic search traffic."
        ),
    )
    paid_cost: int | None = Field(
        ...,
        title="Paid Cost",
        description=(
            "(10 units) The estimated cost of your target's monthly "
            "paid search traffic."
        ),
    )
