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


class RefDomainHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/refdomains-history")
    _obj_name: str = PrivateAttr("refdomains")
    target: str = Field(..., description="The target of the search: a domain or a URL.")
    date_to: DateType | None = Field(
        None, description="The end date of the historical period in YYYY-MM-DD format."
    )
    history_grouping: HistoryGrouping = Field(
        HistoryGrouping.monthly,
        title="History Grouping",
        description="The time interval used to group historical data. `daily`, `weekly`, `monthly`",
    )
    mode: RequestMode = Field(
        RequestMode.subdomains,
        title="Mode",
        description=(
            "The scope of the search based on the target you entered. `exact`, `prefix`, `domain`, `subdomains`"
        ),
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
    )
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )


@response_for(RefDomainHistoryRequest)
class RefDomainHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    refdomains: int = Field(
        ...,
        title="Referring Domains",
        description="(5 units) The total number of unique domains linking to your target.",
    )