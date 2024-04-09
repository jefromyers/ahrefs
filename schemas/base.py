from datetime import date as DateType
from enum import Enum
from typing import Dict, Generic, Type, TypeVar

from pydantic import BaseModel, Field, PrivateAttr

APIRequest = TypeVar("APIRequest", bound="BaseRequest")

RESPONSE_CLASS_MAP = {}


class TopPagesSelect(str, Enum):
    keywords = "keywords"
    keywords_diff = "keywords_diff"
    keywords_diff_percent = "keywords_diff_percent"
    keywords_merged = "keywords_merged"
    keywords_prev = "keywords_prev"
    raw_url = "raw_url"
    raw_url_prev = "raw_url_prev"
    sum_traffic = "sum_traffic"
    sum_traffic_merged = "sum_traffic_merged"
    sum_traffic_prev = "sum_traffic_prev"
    top_keyword = "top_keyword"
    top_keyword_best_position = "top_keyword_best_position"
    top_keyword_best_position_diff = "top_keyword_best_position_diff"
    top_keyword_best_position_kind = "top_keyword_best_position_kind"
    top_keyword_best_position_kind_prev = "top_keyword_best_position_kind_prev"
    top_keyword_best_position_prev = "top_keyword_best_position_prev"
    top_keyword_best_position_title = "top_keyword_best_position_title"
    top_keyword_best_position_title_prev = "top_keyword_best_position_title_prev"
    top_keyword_country = "top_keyword_country"
    top_keyword_country_prev = "top_keyword_country_prev"
    top_keyword_prev = "top_keyword_prev"
    top_keyword_volume = "top_keyword_volume"
    top_keyword_volume_prev = "top_keyword_volume_prev"
    traffic_diff = "traffic_diff"
    traffic_diff_percent = "traffic_diff_percent"
    url = "url"
    url_prev = "url_prev"
    value = "value"
    value_diff = "value_diff"
    value_diff_percent = "value_diff_percent"
    value_merged = "value_merged"
    value_prev = "value_prev"

    def __str__(self):
        return self.value


class OrganicKeywordsSelect(str, Enum):
    best_position = "best_position"
    best_position_diff = "best_position_diff"
    best_position_has_thumbnail = "best_position_has_thumbnail"
    best_position_has_thumbnail_prev = "best_position_has_thumbnail_prev"
    best_position_has_video = "best_position_has_video"
    best_position_has_video_prev = "best_position_has_video_prev"
    best_position_kind = "best_position_kind"
    best_position_kind_merged = "best_position_kind_merged"
    best_position_kind_prev = "best_position_kind_prev"
    best_position_prev = "best_position_prev"
    best_position_set = "best_position_set"
    best_position_set_prev = "best_position_set_prev"
    best_position_url = "best_position_url"
    best_position_url_prev = "best_position_url_prev"
    cpc = "cpc"
    cpc_merged = "cpc_merged"
    cpc_prev = "cpc_prev"
    is_best_position_set_top_11_50 = "is_best_position_set_top_11_50"
    is_best_position_set_top_11_50_prev = "is_best_position_set_top_11_50_prev"
    is_best_position_set_top_3 = "is_best_position_set_top_3"
    is_best_position_set_top_3_prev = "is_best_position_set_top_3_prev"
    is_best_position_set_top_4_10 = "is_best_position_set_top_4_10"
    is_best_position_set_top_4_10_prev = "is_best_position_set_top_4_10_prev"
    keyword = "keyword"
    keyword_difficulty = "keyword_difficulty"
    keyword_difficulty_merged = "keyword_difficulty_merged"
    keyword_difficulty_prev = "keyword_difficulty_prev"
    keyword_merged = "keyword_merged"
    keyword_prev = "keyword_prev"
    language = "language"
    language_prev = "language_prev"
    last_update = "last_update"
    last_update_prev = "last_update_prev"
    serp_features = "serp_features"
    serp_features_count = "serp_features_count"
    serp_features_count_prev = "serp_features_count_prev"
    serp_features_merged = "serp_features_merged"
    serp_features_prev = "serp_features_prev"
    serp_target_main_positions_count = "serp_target_main_positions_count"
    serp_target_main_positions_count_prev = "serp_target_main_positions_count_prev"
    serp_target_positions_count = "serp_target_positions_count"
    serp_target_positions_count_prev = "serp_target_positions_count_prev"
    status = "status"
    sum_paid_traffic = "sum_paid_traffic"
    sum_traffic = "sum_traffic"
    sum_traffic_merged = "sum_traffic_merged"
    sum_traffic_prev = "sum_traffic_prev"
    volume = "volume"
    volume_merged = "volume_merged"
    volume_prev = "volume_prev"
    words = "words"
    words_merged = "words_merged"
    words_prev = "words_prev"

    def __str__(self):
        return self.value


class AnchorsSelect(str, Enum):
    anchor = "anchor"
    dofollow_links = "dofollow_links"
    first_seen = "first_seen"
    last_seen = "last_seen"
    links_to_target = "links_to_target"
    lost_links = "lost_links"
    new_links = "new_links"
    refdomains = "refdomains"
    refpages = "refpages"
    top_domain_rating = "top_domain_rating"

    def __str__(self):
        return self.value


class RefdomainsSelect(str, Enum):
    dofollow_linked_domains = "dofollow_linked_domains"
    dofollow_links = "dofollow_links"
    dofollow_refdomains = "dofollow_refdomains"
    domain = "domain"
    domain_rating = "domain_rating"
    first_seen = "first_seen"
    ip_source = "ip_source"
    is_root_domain = "is_root_domain"
    last_seen = "last_seen"
    links_to_target = "links_to_target"
    lost_links = "lost_links"
    new_links = "new_links"
    positions_source_domain = "positions_source_domain"
    traffic_domain = "traffic_domain"

    def __str__(self):
        return self.value


class BacklinksSelect(str, Enum):
    ahrefs_rank_source = "ahrefs_rank_source"
    ahrefs_rank_target = "ahrefs_rank_target"
    alt = "alt"
    anchor = "anchor"
    broken_redirect_new_target = "broken_redirect_new_target"
    broken_redirect_reason = "broken_redirect_reason"
    broken_redirect_source = "broken_redirect_source"
    class_c = "class_c"
    discovered_status = "discovered_status"
    domain_rating_source = "domain_rating_source"
    domain_rating_target = "domain_rating_target"
    drop_reason = "drop_reason"
    encoding = "encoding"
    first_seen = "first_seen"
    first_seen_link = "first_seen_link"
    http_code = "http_code"
    http_crawl = "http_crawl"
    ip_source = "ip_source"
    is_alternate = "is_alternate"
    is_canonical = "is_canonical"
    is_content = "is_content"
    is_dofollow = "is_dofollow"
    is_form = "is_form"
    is_frame = "is_frame"
    is_image = "is_image"
    is_lost = "is_lost"
    is_new = "is_new"
    is_nofollow = "is_nofollow"
    is_redirect = "is_redirect"
    is_redirect_lost = "is_redirect_lost"
    is_root_source = "is_root_source"
    is_root_target = "is_root_target"
    is_rss = "is_rss"
    is_sponsored = "is_sponsored"
    is_text = "is_text"
    is_ugc = "is_ugc"
    js_crawl = "js_crawl"
    languages = "languages"
    last_seen = "last_seen"
    last_visited = "last_visited"
    link_group_count = "link_group_count"
    link_type = "link_type"
    linked_domains_source_domain = "linked_domains_source_domain"
    linked_domains_source_page = "linked_domains_source_page"
    linked_domains_target_domain = "linked_domains_target_domain"
    links_external = "links_external"
    links_internal = "links_internal"
    lost_reason = "lost_reason"
    name_source = "name_source"
    name_target = "name_target"
    noindex = "noindex"
    page_size = "page_size"
    port_source = "port_source"
    port_target = "port_target"
    positions = "positions"
    powered_by = "powered_by"
    redirect_code = "redirect_code"
    redirect_kind = "redirect_kind"
    refdomains_source = "refdomains_source"
    refdomains_source_domain = "refdomains_source_domain"
    refdomains_target_domain = "refdomains_target_domain"
    root_name_source = "root_name_source"
    root_name_target = "root_name_target"
    snippet_left = "snippet_left"
    snippet_right = "snippet_right"
    source_page_author = "source_page_author"
    page_title = "title"
    tld_class_source = "tld_class_source"
    tld_class_target = "tld_class_target"
    traffic = "traffic"
    traffic_domain = "traffic_domain"
    url_from = "url_from"
    url_from_plain = "url_from_plain"
    url_rating_source = "url_rating_source"
    url_redirect = "url_redirect"
    url_to = "url_to"
    url_to_plain = "url_to_plain"

    def __str__(self):
        return self.value


class BrokenRedirectReason(str, Enum):
    droppedmanual = "droppedmanual"
    droppedtooold = "droppedtooold"
    dropped = "dropped"
    codechanged = "codechanged"
    nxdomain = "nxdomain"
    robotsdisallowed = "robotsdisallowed"
    curlerror = "curlerror"
    invalidtarget = "invalidtarget"
    nomorecanonical = "nomorecanonical"
    isnowparked = "isnowparked"
    targetchanged = "targetchanged"


class DiscoveredStatus(str, Enum):
    pagefound = "pagefound"
    linkfound = "linkfound"
    linkrestored = "linkrestored"


class DropReason(str, Enum):
    manual = "manual"
    noratingunused = "noratingunused"
    notop = "notop"
    tooold = "tooold"
    oldunavailable = "oldunavailable"
    rescursive = "recursive"
    duplicate = "duplicate"
    nxdomain = "nxdomain"
    malformed = "malformed"
    blockedport = "blockedport"
    disallowed = "disallowed"
    unlinked = "unlinked"


class LinkType(str, Enum):
    redirect = "redirect"
    frame = "frame"
    text = "text"
    form = "form"
    canonical = "canonical"
    alternate = "alternate"
    rss = "rss"
    image = "image"


class Aggregation(str, Enum):
    similar_links = "similar_links"
    one_per_domain = "1_per_domain"
    all = "all"

    def __str__(self):
        return self.value


class TldClassSource(str, Enum):
    gov = "gov"
    edu = "edu"
    normal = "normal"


class TldClassTarget(str, Enum):
    gov = "gov"
    edu = "edu"
    normal = "normal"


class LostReason(str, Enum):
    removedfromhtml = "removedfromhtml"
    notcanonical = "notcanonical"
    noindex = "noindex"
    pageredirected = "pageredirected"
    pageerror = "pageerror"
    lostredirect = "lostredirect"
    notfound = "notfound"


class RequestMode(str, Enum):
    exact = "exact"
    prefix = "prefix"
    domain = "domain"
    subdomains = "subdomains"

    def __str__(self):
        return self.value


class VolumeMode(str, Enum):
    monthly = "monthly"
    average = "average"

    def __str__(self):
        return self.value


class HistoryGrouping(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"

    def __str__(self):
        return self.value


class Country(str, Enum):
    AD = "ad"
    AE = "ae"
    AF = "af"
    AG = "ag"
    AI = "ai"
    AL = "al"
    AM = "am"
    AO = "ao"
    AQ = "aq"
    AR = "ar"
    AS = "as"
    AT = "at"
    AU = "au"
    AW = "aw"
    AX = "ax"
    AZ = "az"
    BA = "ba"
    BB = "bb"
    BD = "bd"
    BE = "be"
    BF = "bf"
    BG = "bg"
    BH = "bh"
    BI = "bi"
    BJ = "bj"
    BL = "bl"
    BM = "bm"
    BN = "bn"
    BO = "bo"
    BQ = "bq"
    BR = "br"
    BS = "bs"
    BT = "bt"
    BV = "bv"
    BW = "bw"
    BY = "by"
    BZ = "bz"
    CA = "ca"
    CC = "cc"
    CD = "cd"
    CF = "cf"
    CG = "cg"
    CH = "ch"
    CI = "ci"
    CK = "ck"
    CL = "cl"
    CM = "cm"
    CN = "cn"
    CO = "co"
    CR = "cr"
    CU = "cu"
    CV = "cv"
    CW = "cw"
    CX = "cx"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DJ = "dj"
    DK = "dk"
    DM = "dm"
    DO = "do"
    DZ = "dz"
    EC = "ec"
    EE = "ee"
    EG = "eg"
    EH = "eh"
    ER = "er"
    ES = "es"
    ET = "et"
    FI = "fi"
    FJ = "fj"
    FK = "fk"
    FM = "fm"
    FO = "fo"
    FR = "fr"
    GA = "ga"
    GB = "gb"
    GD = "gd"
    GE = "ge"
    GF = "gf"
    GG = "gg"
    GH = "gh"
    GI = "gi"
    GL = "gl"
    GM = "gm"
    GN = "gn"
    GP = "gp"
    GQ = "gq"
    GR = "gr"
    GS = "gs"
    GT = "gt"
    GU = "gu"
    GW = "gw"
    GY = "gy"
    HK = "hk"
    HM = "hm"
    HN = "hn"
    HR = "hr"
    HT = "ht"
    HU = "hu"
    ID = "id"
    IE = "ie"
    IL = "il"
    IM = "im"
    IN = "in"
    IO = "io"
    IQ = "iq"
    IR = "ir"
    IS = "is"
    IT = "it"
    JE = "je"
    JM = "jm"
    JO = "jo"
    JP = "jp"
    KE = "ke"
    KG = "kg"
    KH = "kh"
    KI = "ki"
    KM = "km"
    KN = "kn"
    KP = "kp"
    KR = "kr"
    KW = "kw"
    KY = "ky"
    KZ = "kz"
    LA = "la"
    LB = "lb"
    LC = "lc"
    LI = "li"
    LK = "lk"
    LR = "lr"
    LS = "ls"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    LY = "ly"
    MA = "ma"
    MC = "mc"
    MD = "md"
    ME = "me"
    MF = "mf"
    MG = "mg"
    MH = "mh"
    MK = "mk"
    ML = "ml"
    MM = "mm"
    MN = "mn"
    MO = "mo"
    MP = "mp"
    MQ = "mq"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MU = "mu"
    MV = "mv"
    MW = "mw"
    MX = "mx"
    MY = "my"
    MZ = "mz"
    NA = "na"
    NC = "nc"
    NE = "ne"
    NF = "nf"
    NG = "ng"
    NI = "ni"
    NL = "nl"
    NO = "no"
    NP = "np"
    NR = "nr"
    NU = "nu"
    NZ = "nz"
    OM = "om"
    PA = "pa"
    PE = "pe"
    PF = "pf"
    PG = "pg"
    PH = "ph"
    PK = "pk"
    PL = "pl"
    PM = "pm"
    PN = "pn"
    PR = "pr"
    PS = "ps"
    PT = "pt"
    PW = "pw"
    PY = "py"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RS = "rs"
    RU = "ru"
    RW = "rw"
    SA = "sa"
    SB = "sb"
    SC = "sc"
    SD = "sd"
    SE = "se"
    SG = "sg"
    SH = "sh"
    SI = "si"
    SJ = "sj"
    SK = "sk"
    SL = "sl"
    SM = "sm"
    SN = "sn"
    SO = "so"
    SR = "sr"
    SS = "ss"
    ST = "st"
    SV = "sv"
    SX = "sx"
    SY = "sy"
    SZ = "sz"
    TC = "tc"
    TD = "td"
    TF = "tf"
    TG = "tg"
    TH = "th"
    TJ = "tj"
    TK = "tk"
    TL = "tl"
    TM = "tm"
    TN = "tn"
    TO = "to"
    TR = "tr"
    TT = "tt"
    TV = "tv"
    TW = "tw"
    TZ = "tz"
    UA = "ua"
    UG = "ug"
    UM = "um"
    US = "us"
    UY = "uy"
    UZ = "uz"
    VA = "va"
    VC = "vc"
    VE = "ve"
    VG = "vg"
    VI = "vi"
    VN = "vn"
    VU = "vu"
    WF = "wf"
    WS = "ws"
    YE = "ye"
    YT = "yt"
    ZA = "za"
    ZM = "zm"
    ZW = "zw"

    def __str__(self):
        return self.value


class SearchEngine(str, Enum):
    google = "google"
    youtube = "youtube"
    amazon = "amazon"
    bing = "bing"
    yahoo = "yahoo"
    yandex = "yandex"
    baidu = "baidu"
    daum = "daum"
    naver = "naver"
    seznam = "seznam"

    def __str__(self):
        return self.value


def response_for(req_type: APIRequest):
    def dec(resp_klass: Type[BaseResponse]):
        RESPONSE_CLASS_MAP[req_type] = resp_klass
        return resp_klass

    return dec


class BaseRequest(BaseModel):
    retry: int = Field(0, description="The number of retries")
    cache: bool = Field(True, description="Whether to cache the response")

    # API specific fields
    top_positions: int | None = Field(
        None,
        title="Top Positions",
        description="The number of top organic SERP positions to return. If not specified, all available positions will be returned.",
    )
    keyword_list_id: int | None = Field(
        None,
        title="Keyword List ID",
        description="The id of an existing keyword list to show metrics for.",
    )
    # Maybe a list would be better?
    keywords: str | None = Field(
        None,
        title="Keywords",
        description="A comma-separated list of keywords to show metrics for.",
    )
    keyword: str | None = Field(
        None,
        title="Keyword",
        description="A keywords to show metrics for.",
    )
    search_engine: SearchEngine | None = Field(
        SearchEngine.google,
        title="Search Engine",
        description="The search engine to get keyword metrics for.",
    )
    # Maybe better as enum?
    match_mode: str | None = Field(
        None,
        title="Match Mode",
        description="Keyword ideas contain the words from your query in any order (terms mode) or in the exact order they are written (phrase mode).",
    )
    # Maybe better as enum?
    terms: str | None = Field(
        None,
        title="Terms",
        description="All keywords ideas or keywords ideas phrased as questions. Expects `all` or `questions`",
    )
    date: DateType | None = Field(
        None, description="A date to report metrics on in YYYY-MM-DD format."
    )
    date_from: DateType | None = Field(
        None,
        description="The volume mode to use for the request. Defaults to 'monthly'.",
    )
    date_to: DateType | None = Field(
        None, description="The end date of the historical period in YYYY-MM-DD format."
    )
    target: str | None = Field(
        None, description="The target of the search: a domain or a URL."
    )
    protocol: str = Field(
        "both",
        description="The protocol to use for the request. Defaults to 'http'.",
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
    country: Country | None = Field(
        None,
        title="Country Code",
        description="The country code to use for the request. Defaults to None.",
    )
    history_grouping: HistoryGrouping | None = Field(
        None,
        title="History Grouping",
        description="The time interval used to group historical data.",
    )
    # Should we default this?
    limit: int | None = Field(
        None, title="Limit", description="The number of results to return."
    )
    offset: int | None = Field(
        None,
        title="Offset",
        description="Returned results will start from the row indicated in the offset value.",
    )
    aggregation: Aggregation | None = Field(
        None, description="The backlinks grouping mode."
    )
    order_by: int | None = Field(
        None,
        description="A column to order results by. See response schema for valid column identifiers.",
    )
    timeout: int | None = Field(
        None, description="A manual timeout duration in seconds."
    )
    date_compared: DateType | None = Field(
        None, description="A date to compare metrics with in YYYY-MM-DD format."
    )
    # TODO: Add missing where
    # TODO: Add missing history

    def make_params(self) -> Dict[str, str]:
        params = self.dict(exclude={"retry", "cache"})
        if "select" in params and isinstance(params["select"], list):
            params["select"] = ",".join([str(item) for item in params["select"]])
        filtered = {k: v for k, v in params.items() if v is not None}
        return filtered


class BaseResponse(BaseModel, Generic[APIRequest]):
    request: APIRequest = Field(..., description="The request object")
    elapsed: float = Field(..., description="The time taken to process the request")
    api_rows: int | None = Field(
        None,
        alias="x_api_rows",
        title="Api Rows",
        description="The number of rows returned",
    )
    api_units_cost_row: int | None = Field(
        None,
        alias="x_api_units_cost_row",
        title="Api Units Cost Row",
        description="The per-row units cost.",
    )
    api_units_cost_total: int | None = Field(
        None,
        alias="x_api_units_cost_total",
        title="Api Units Cost Total",
        description=(
            "The overall units that the request should consume based on the "
            "number of rows and per-row cost."
        ),
    )
    api_units_cost_total_actual: int | None = Field(
        None,
        alias="x_api_units_cost_total_actual",
        title="Api Units Cost Total Actual",
        description="The overall units that the request actually consumed.",
    )
    api_cache: str | None = Field(
        None,
        alias="x_api_cache",
        title="Api Cache",
        description="Whether the request was served from cache.",
    )
