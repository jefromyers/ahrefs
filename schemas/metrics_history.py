from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import (
    BaseRequest,
    BaseResponse,
    CountryCode,
    HistoryGrouping,
    RequestMode,
    VolumeMode,
    response_for,
)


class MetricsHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/metrics-history")
    _obj_name: str = PrivateAttr("metrics")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    country_code: CountryCode | None = Field(
        None,
        title="Country Code",
        description="The country code to use for the request. Defaults to None.",
    )
    date_to: DateType | None = Field(
        None, description="The end date of the historical period in YYYY-MM-DD format."
    )
    history_grouping: HistoryGrouping = Field(
        HistoryGrouping.monthly,
        title="History Grouping",
        description=(
            "The time interval used to group historical data. "
            "`daily`, `weekly`, `monthly`"
        ),
    )
    mode: RequestMode = Field(
        RequestMode.subdomains,
        title="Mode",
        description=(
            "The scope of the search based on the target you entered. "
            "`exact`, `prefix`, `domain`, `subdomains`"
        ),
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    volume_mode: VolumeMode = Field(
        VolumeMode.monthly,
        description="The volume mode to use for the request. Defaults to 'monthly'.",
    )
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )


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
