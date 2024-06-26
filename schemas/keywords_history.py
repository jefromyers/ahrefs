from datetime import date as DateType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class SelectMode(str, Enum):
    date = "date"
    top3 = "top3"
    top4_10 = "top4_10"
    top11_plus = "top11_plus"

    def __str__(self):
        return self.value


class KeywordsHistoryRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/keywords-history")
    _obj_name: str = PrivateAttr("keywords")
    # Response specific fields
    select: List[SelectMode] = Field(
        [SelectMode.date, SelectMode.top3, SelectMode.top4_10, SelectMode.top11_plus],
        title="Select",
        description=(
            "The scope of the search based on the target you entered. "
            "`date`, `top3`, `top4-10`, `top11-plus`"
        ),
    )
    # Required fields
    date_from: DateType = Field(
        ...,
        title="Date From",
        description="The start date of the historical period in YYYY-MM-DD format.",
    )
    target: str = Field(..., description="The target of the search: a domain or a URL.")

    def dict(self, **kwargs) -> dict:
        d = super().dict(**kwargs)
        if "select" in d and isinstance(d["select"], list):
            d["select"] = ",".join([str(item) for item in d["select"]])
        return d


@response_for(KeywordsHistoryRequest)
class KeywordsHistoryResponse(BaseResponse):
    date: DateType = Field(..., title="Date", description="Date of the metric.")
    top11_20: int | None = Field(
        None,
        title="Top 11-20",
        description=(
            "The total number of keywords that your target ranks for in the top 11-20 "
            "organic search results."
        ),
    )
    top11_plus: int | None = Field(
        None,
        title="Top 11+",
        description=(
            "The total number of keywords that your target ranks for in the "
            "top 11+ organic search results."
        ),
    )
    top21_50: int | None = Field(
        None,
        title="Top 21-50",
        description=(
            "The total number of keywords that your target ranks for in the top 21-50 "
            "organic search results."
        ),
    )
    top3: int | None = Field(
        None,
        title="Top 3",
        description=(
            "The total number of keywords that your target ranks for "
            "in the top 3 organic search results."
        ),
    )
    top4_10: int | None = Field(
        None,
        title="Top 4-10",
        description=(
            "The total number of keywords that your target ranks for in the top 4-10 "
            "organic search results."
        ),
    )
    top51_plus: int | None = Field(
        None,
        title="Top 51+",
        description=(
            "The total number of keywords that your target ranks for in the "
            "top 51+ organic search results."
        ),
    )
