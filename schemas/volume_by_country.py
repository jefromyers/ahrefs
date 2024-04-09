from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, Country, response_for


class VolumeByCountryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/keywords-explorer/volume-by-country")
    _obj_name: str = PrivateAttr("countries")
    # Defaults
    limit: int = Field(1_000, description="The number of results to return.")
    offset: int | None = Field(
        0,
        description="Returned results will start from the row indicated in the offset value.",
    )
    # Required fields
    keyword: str = Field(
        ...,
        title="Keyword",
        description="A keywords to show metrics for.",
    )


@response_for(VolumeByCountryRequest)
class VolumeByCountryResponse(BaseResponse):
    country: Country = Field(
        ...,
        title="Country",
        description="The country",
    )
    volume: int = Field(
        ...,
        title="Volume",
        description="(10 units) An estimation of the average monthly number of searches for a keyword in a given country.",
    )
