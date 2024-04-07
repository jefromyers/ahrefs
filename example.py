from datetime import datetime
from pathlib import Path

from client.ahrefs_api import AhrefsAPI
from schemas import *


def get_token() -> str:
    data_dir = Path("data")
    path = data_dir / "ahrefs_token"
    token = path.read_text().strip()
    return token


if __name__ == "__main__":
    token = get_token()

    target = "ahrefs.com"
    with AhrefsAPI.connect(token=token) as api:
        request = DomainRatingRequest(target=target, date=f"{datetime.now():%Y-%m-%d}")
        result = api.request(request)
        print(f"Domain Rating : {result.domain_rating}")
        print(f"Ahrefs Rank   : {result.ahrefs_rank}")
        print(f"Request       : {result.request}")
        print(f"Seconds       : {result.elapsed}")
