from datetime import date as DateType
from datetime import datetime as DatetimeType
from enum import Enum
from typing import List

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, Country, response_for


class LimitsAndUsageRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/subscription-info/limits-and-usage")
    _obj_name: str = PrivateAttr("limits_and_usage")


@response_for(LimitsAndUsageRequest)
class LimitsAndUsageResponse(BaseResponse):
    subscription: str = Field(
        ..., title="Subscription", description="Ahrefs subscription plan."
    )
    usage_reset_date: DateType = Field(
        ...,
        title="Usage Reset Date",
        description="Start date of the next billing period when the API units usage will be reset.",
    )
    units_limit_workspace: int = Field(
        ...,
        title="Units Limit Workspace",
        description="Total number of API units available to the workspace.",
    )
    units_usage_workspace: int = Field(
        ...,
        title="Units Usage Workspace",
        description="Number of API units consumed by the workspace in the current billing month.",
    )
    units_limit_api_key: int = Field(
        ...,
        title="Units Limit API Key",
        description="Limit for the number of API units that can be consumed via this API key per billing month (null = unlimited).",
    )
    units_usage_api_key: int = Field(
        ...,
        title="Units Usage API Key",
        description="Number of API units consumed by this API key in the current billing month.",
    )
    api_key_expiration_date: DatetimeType = Field(
        ...,
        title="API Key Expiration Date",
        description="Date on which this API key will expire and stop working.",
    )
