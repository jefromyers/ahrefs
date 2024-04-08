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
        # Domain Rating
        # request = DomainRatingRequest(target=target, date=f"{datetime.now():%Y-%m-%d}")
        # result = api.request(request)
        # print(f"Domain Rating : {result.domain_rating}")
        # print(f"Ahrefs Rank   : {result.ahrefs_rank}")
        # print(f"Request       : {result.request}")
        # print(f"Seconds       : {result.elapsed}")

        # # Backlinks Stats
        # request = BacklinksStatsRequest(
        #     target=target, date=f"{datetime.now():%Y-%m-%d}"
        # )
        # result = api.request(request)
        # print(f"Live Backlinks            : {result.live}")
        # print(f"All Time Backlinks        : {result.all_time}")
        # print(f"Live Referring Domains    : {result.live_refdomains}")
        # print(f"All Time Referring Domains: {result.all_time_refdomains}")
        # print(f"Request                   : {result.request}")
        # print(f"Seconds                   : {result.elapsed}")

        # List Outlinks Stats
        # request = OutlinksStatsRequest(
        #     target=target,
        #     mode=RequestMode.subdomains,
        # )
        # print(request)
        # result = api.request(request)
        # print(f"Outgoing Links            : {result.outgoing_links}")
        # print(f"Outgoing Links Dofollow   : {result.outgoing_links_dofollow}")
        # print(f"Linked Domains            : {result.linked_domains}")
        # print(f"Linked Domains Dofollow   : {result.linked_domains_dofollow}")
        # print(f"Request                   : {result.request}")
        # print(f"Seconds                   : {result.elapsed}")

        # Metrics
        # request = MetricsRequest(
        #     target=target,
        #     date=f"{datetime.now():%Y-%m-%d}",
        #     mode=RequestMode.subdomains,
        #     protocol="both",
        #     volume_mode=VolumeMode.monthly,
        #     country_code=None,
        # )
        # result = api.request(request)
        # print(f"Organic Keywords          : {result.org_keywords}")
        # print(f"Paid Keywords             : {result.paid_keywords}")
        # print(f"Top 3 Organic Keywords    : {result.org_keywords_1_3}")
        # print(f"Organic Traffic           : {result.org_traffic}")
        # print(f"Organic Cost              : {result.org_cost}")
        # print(f"Paid Traffic              : {result.paid_traffic}")
        # print(f"Paid Cost                 : {result.paid_cost}")
        # print(f"Paid Pages                : {result.paid_pages}")
        # print(f"Request                   : {result.request}")
        # print(f"Seconds                   : {result.elapsed}")

        # RefDomains History
        # request = RefDomainHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        #     date_to=datetime(2024, 4, 7),
        #     history_grouping=HistoryGrouping.monthly,
        #     mode=RequestMode.subdomains,
        #     protocol="both",
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} Referring Domains: {hist.refdomains}")

        # Domain Rating History
        # request = DomainRatingHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        #     date_to=datetime(2024, 4, 7),
        #     history_grouping=HistoryGrouping.monthly,
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} Domain Rating: {hist.domain_rating}")

        # Url Rating History
        # target = "https://citationlabs.com/blog/"
        # request = UrlRatingHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        #     date_to=datetime(2024, 4, 7),
        #     history_grouping=HistoryGrouping.monthly,
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} URL Rating: {hist.domain_rating}")

        # Metrics History
        # target = "https://citationlabs.com/"
        # request = MetricsHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        #     date_to=datetime(2024, 4, 7),
        #     history_grouping=HistoryGrouping.monthly,
        #     mode=RequestMode.subdomains,
        #     protocol="both",
        #     volume_mode=VolumeMode.monthly,
        #     country_code=None,
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(
        #         f"Date: {hist.date} Organic Traffic: {hist.org_traffic} Paid Traffic: {hist.paid_traffic}"
        #     )

        # Page History
        # target = "https://citationlabs.com/blog/"
        # request = PageHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        #     date_to=datetime(2024, 4, 7),
        #     history_grouping=HistoryGrouping.monthly,
        #     mode=RequestMode.subdomains,
        #     protocol="both",
        #     volume_mode=VolumeMode.monthly,
        #     country_code=None,
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} Pages: {hist.pages}")

        # Keywords History
        # target = "https://citationlabs.com/"
        # request = KeywordsHistoryRequest(
        #     target=target,
        #     date_from=f"{datetime(2024, 1, 1):%Y-%m-%d}",
        #     date_to=f"{datetime(2024, 4, 7):%Y-%m-%d}",
        #     history_grouping=HistoryGrouping.monthly,
        #     mode=RequestMode.subdomains,
        #     protocol="both",
        #     country_code=None,
        #     select=[
        #         SelectMode.date,
        #         SelectMode.top3,
        #         SelectMode.top4_10,
        #         SelectMode.top11_plus,
        #     ],
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(
        #         f"Date: {hist.date} Top3: {hist.top3} Top4-10: {hist.top4_10} Top11+: {hist.top11_plus}"
        #     )

        # Metrics By Country
        # target = "https://citationlabs.com/"
        # request = MetricsByCountryRequest(
        #     limit=10,
        #     target=target,
        #     date=f"{datetime(2024, 1, 1):%Y-%m-%d}",
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Country: {hist.country} Organic Traffic: {hist.org_traffic}")

        # Pages By Traffic
        # target = "https://citationlabs.com/"
        # request = PagesByTrafficRequest(
        #     target=target,
        #     mode=RequestMode.subdomains,
        #     offset=0,
        #     protocol="both",
        #     volume_mode=VolumeMode.monthly,
        # )
        # result = api.request(request)
        # print(result)

        # All Backlinks
        target = "https://citationlabs.com/"
        request = AllBacklinksRequest(
            target=target,
            select=[AllBacklinksSelect.anchor, AllBacklinksSelect.url_from],
            limit=10,
        )
        result = api.request(request)
        for backlink in result:
            print(f"URL: {backlink.anchor} Referring Page: {backlink.url_from}")
