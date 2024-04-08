from datetime import date as DateType

from pydantic import Field, PrivateAttr

from schemas.base import BaseRequest, BaseResponse, response_for


class DomainRatingRequest(BaseRequest):
    _endpoint: str = PrivateAttr("/v3/site-explorer/domain-rating")
    _obj_name: str = PrivateAttr("domain_rating")

    # Required fields
    date: DateType | None = Field(
        ..., description="A date to report metrics on in YYYY-MM-DD format."
    )
    target: str | None = Field(
        ..., description="The target of the search: a domain or a URL."
    )


@response_for(DomainRatingRequest)
class DomainRatingResponse(BaseResponse):
    domain_rating: float = Field(
        ...,
        description=(
            "The strength of your target's backlink profile compared to the "
            "other websites in our database on a 100-point logarithmic scale."
        ),
    )
    ahrefs_rank: int | None = Field(
        ...,
        description=(
            "The strength of your target's backlink profile compared to "
            "the other websites in our database, with rank #1 being the strongest."
        ),
    )
