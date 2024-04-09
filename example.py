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

        # Backlinks Stats
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
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} Referring Domains: {hist.refdomains}")

        # Domain Rating History
        # request = DomainRatingHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
        # )
        # results = api.request(request)
        # for hist in results:
        #     print(f"Date: {hist.date} Domain Rating: {hist.domain_rating}")

        # Url Rating History
        # target = "https://citationlabs.com/blog/"
        # request = UrlRatingHistoryRequest(
        #     target=target,
        #     date_from=datetime(2024, 1, 1),
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
        # target = "https://citationlabs.com/"
        # request = AllBacklinksRequest(
        #     target=target,
        #     select=[BacklinksSelect.anchor, BacklinksSelect.url_from],
        #     limit=10,
        # )
        # result = api.request(request)
        # for backlink in result:
        #     print(f"URL: {backlink.anchor} Referring Page: {backlink.url_from}")

        # Broken Backlinks
        # target = "https://citationlabs.com/"
        # request = BrokenBacklinksRequest(
        #     target=target,
        #     select=[BacklinksSelect.anchor, BacklinksSelect.url_from],
        #     limit=10,
        # )
        # result = api.request(request)
        # for backlink in result:
        #     print(f"URL: {backlink.anchor} Referring Page: {backlink.url_from}")

        # Broken Backlinks
        # target = "https://citationlabs.com/"
        # request = RefdomainsRequest(
        #     target=target,
        #     select=[RefdomainsSelect.domain, RefdomainsSelect.domain_rating],
        #     limit=10,
        # )
        # result = api.request(request)
        # for refdomain in result:
        #     print(
        #         f"Domain: {refdomain.domain} Domain Rating: {refdomain.domain_rating}"
        #     )

        # Anchors
        # target = "https://citationlabs.com/"
        # request = AnchorsRequest(
        #     target=target,
        #     select=[AnchorsSelect.anchor, AnchorsSelect.top_domain_rating],
        #     limit=10,
        # )
        # result = api.request(request)
        # for anchor in result:
        #     print(f"Anchor: {anchor.anchor} Count: {anchor.top_domain_rating}")

        # This could be a convenience method.
        # api.anchors(target=target, select="", limit=10)

        # Organic Keywords
        # target = "https://citationlabs.com/"
        # request = OrganicKeywordsRequest(
        #     target=target,
        #     country=CountryCode.US,
        #     date=f"{datetime.today():%Y-%m-%d}",
        #     select=[
        #         OrganicKeywordsSelect.keyword,
        #         OrganicKeywordsSelect.volume,
        #         OrganicKeywordsSelect.cpc,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(
        #         f"Keyword: {keyword.keyword} Volume: {keyword.volume} CPC: {keyword.cpc}"
        #     )

        # Top Pages
        # target = "https://citationlabs.com/"
        # request = TopPagesRequest(
        #     target=target,
        #     date=f"{datetime.today():%Y-%m-%d}",
        #     select=[
        #         TopPagesSelect.raw_url,
        #         TopPagesSelect.sum_traffic,
        #         TopPagesSelect.keywords,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(
        #         f"Page: {page.raw_url} Traffic: {page.sum_traffic} Keywords: {page.keywords}"
        #     )

        # Paid Pages
        # target = "https://ahrefs.com/"
        # request = PaidPagesRequest(
        #     target=target,
        #     date=f"{datetime.today():%Y-%m-%d}",
        #     select=[
        #         PaidPagesSelect.keywords,
        #         PaidPagesSelect.sum_traffic,
        #         PaidPagesSelect.top_keyword_best_position,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(
        #         f"Top: {page.top_keyword_best_position} Traffic: {page.sum_traffic} Keywords: {page.keywords}"
        #     )

        # Best By External Links
        # target = "https://citationlabs.com/"
        # request = BestByExternalLinksRequest(
        #     target=target,
        #     select=[
        #         BestByExternalLinksSelect.url_to,
        #         BestByExternalLinksSelect.new_links_to_target,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(f"URL: {page.url_to} New Links: {page.new_links_to_target}")

        # Best By Internal Links
        # target = "https://citationlabs.com/"
        # request = BestByInternalLinksRequest(
        #     target=target,
        #     select=[
        #         BestByInternalLinksSelect.url_to,
        #         BestByInternalLinksSelect.links_to_target,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(f"URL: {page.url_to} Links: {page.links_to_target}")

        # Linked Domains
        # target = "https://citationlabs.com/"
        # request = LinkedDomainsRequest(
        #     target=target,
        #     select=[LinkedDomainsSelect.dofollow_links, LinkedDomainsSelect.domain],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(f"Domain: {page.domain} Links: {page.dofollow_links}")

        # Outgoing External Anchors
        # target = "https://citationlabs.com/"
        # request = OutgoingExternalAnchorsRequest(
        #     target=target,
        #     select=[
        #         OutgoingExternalAnchorsSelect.anchor,
        #         OutgoingExternalAnchorsSelect.dofollow_links,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(f"Anchor: {page.anchor} Links: {page.dofollow_links}")

        # Outgoing Internal Anchors
        # target = "https://citationlabs.com/"
        # request = OutgoingInternalAnchorsRequest(
        #     target=target,
        #     select=[
        #         OutgoingInternalAnchorsSelect.anchor,
        #         OutgoingInternalAnchorsSelect.dofollow_links,
        #     ],
        #     limit=10,
        # )
        # results = api.request(request)
        # for page in results:
        #     print(f"Anchor: {page.anchor} Links: {page.dofollow_links}")

        # Keyword Overview
        # request = KeywordOverviewRequest(
        #     select=[
        #         KeywordOverviewSelect.keyword,
        #         KeywordOverviewSelect.volume,
        #         KeywordOverviewSelect.difficulty,
        #     ],
        #     country=Country.US,
        #     keywords="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(
        #         f"Keyword: {keyword.keyword} Volume: {keyword.volume} Difficulty: {keyword.difficulty}"
        #     )

        # Volume History
        # request = VolumeHistoryRequest(
        #     country=Country.US,
        #     keyword="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(f"Date: {keyword.date} Volume: {keyword.volume}")

        # Volume By Country
        # request = VolumeByCountryRequest(
        #     keyword="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(f"Date: {keyword.country} Volume: {keyword.volume}")

        # Matching Terms
        # request = MatchingTermsRequest(
        #     select=[MatchingTermsSelect.keyword, MatchingTermsSelect.cpc],
        #     country=Country.US,
        #     keywords="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(f"Keyword: {keyword.keyword} CPC: {keyword.cpc}")
        #

        # Related Terms
        # request = RelatedTermsRequest(
        #     select=[RelatedTermsSelect.keyword, RelatedTermsSelect.cpc],
        #     country=Country.US,
        #     keywords="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(f"Keyword: {keyword.keyword} CPC: {keyword.cpc}")

        # Search suggestions
        # request = SearchSuggestionsRequest(
        #     select=[RelatedTermsSelect.keyword, RelatedTermsSelect.cpc],
        #     country=Country.US,
        #     keywords="seo",
        # )
        # results = api.request(request)
        # for keyword in results:
        #     print(f"Keyword: {keyword.keyword} CPC: {keyword.cpc}")

        request = LimitsAndUsageRequest()
        result = api.request(request)
        print(result)

        ...
