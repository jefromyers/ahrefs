from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, Country, response_for


class VolumeHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/keywords-explorer/volume-history")
    _obj_name: str = PrivateAttr("metrics")
    # Required fields
    country: Country = Field(
        ...,
        title="Country",
        description="The country to get data for.",
    )
    keyword: str = Field(
        ...,
        title="Keyword",
        description="A keywords to show metrics for.",
    )


@response_for(VolumeHistoryRequest)
class VolumeHistoryResponse(BaseResponse):
    date: DateType = Field(
        ...,
        title="Date",
        description="The date of the metric.",
    )
    volume: int = Field(
        ...,
        title="Volume",
        description="An estimation of the number of searches for a keyword over a given month.",
    )
