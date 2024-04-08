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
    AD = "Andorra"
    AE = "United Arab Emirates"
    AF = "Afghanistan"
    AG = "Antigua and Barbuda"
    AI = "Anguilla"
    AL = "Albania"
    AM = "Armenia"
    AO = "Angola"
    AQ = "Antarctica"
    AR = "Argentina"
    AS = "American Samoa"
    AT = "Austria"
    AU = "Australia"
    AW = "Aruba"
    AX = "Åland Islands"
    AZ = "Azerbaijan"
    BA = "Bosnia and Herzegovina"
    BB = "Barbados"
    BD = "Bangladesh"
    BE = "Belgium"
    BF = "Burkina Faso"
    BG = "Bulgaria"
    BH = "Bahrain"
    BI = "Burundi"
    BJ = "Benin"
    BL = "Saint Barthélemy"
    BM = "Bermuda"
    BN = "Brunei Darussalam"
    BO = "Bolivia, Plurinational State of"
    BQ = "Bonaire, Sint Eustatius and Saba"
    BR = "Brazil"
    BS = "Bahamas"
    BT = "Bhutan"
    BV = "Bouvet Island"
    BW = "Botswana"
    BY = "Belarus"
    BZ = "Belize"
    CA = "Canada"
    CC = "Cocos (Keeling) Islands"
    CD = "Congo, Democratic Republic of the"
    CF = "Central African Republic"
    CG = "Congo"
    CH = "Switzerland"
    CI = "Côte d'Ivoire"
    CK = "Cook Islands"
    CL = "Chile"
    CM = "Cameroon"
    CN = "China"
    CO = "Colombia"
    CR = "Costa Rica"
    CU = "Cuba"
    CV = "Cabo Verde"
    CW = "Curaçao"
    CX = "Christmas Island"
    CY = "Cyprus"
    CZ = "Czechia"
    DE = "Germany"
    DJ = "Djibouti"
    DK = "Denmark"
    DM = "Dominica"
    DO = "Dominican Republic"
    DZ = "Algeria"
    EC = "Ecuador"
    EE = "Estonia"
    EG = "Egypt"
    EH = "Western Sahara"
    ER = "Eritrea"
    ES = "Spain"
    ET = "Ethiopia"
    FI = "Finland"
    FJ = "Fiji"
    FK = "Falkland Islands (Malvinas)"
    FM = "Micronesia, Federated States of"
    FO = "Faroe Islands"
    FR = "France"
    GA = "Gabon"
    GB = "United Kingdom of Great Britain and Northern Ireland"
    GD = "Grenada"
    GE = "Georgia"
    GF = "French Guiana"
    GG = "Guernsey"
    GH = "Ghana"
    GI = "Gibraltar"
    GL = "Greenland"
    GM = "Gambia"
    GN = "Guinea"
    GP = "Guadeloupe"
    GQ = "Equatorial Guinea"
    GR = "Greece"
    GS = "South Georgia and the South Sandwich Islands"
    GT = "Guatemala"
    GU = "Guam"
    GW = "Guinea-Bissau"
    GY = "Guyana"
    HK = "Hong Kong"
    HM = "Heard Island and McDonald Islands"
    HN = "Honduras"
    HR = "Croatia"
    HT = "Haiti"
    HU = "Hungary"
    ID = "Indonesia"
    IE = "Ireland"
    IL = "Israel"
    IM = "Isle of Man"
    IN = "India"
    IO = "British Indian Ocean Territory"
    IQ = "Iraq"
    IR = "Iran, Islamic Republic of"
    IS = "Iceland"
    IT = "Italy"
    JE = "Jersey"
    JM = "Jamaica"
    JO = "Jordan"
    JP = "Japan"
    KE = "Kenya"
    KG = "Kyrgyzstan"
    KH = "Cambodia"
    KI = "Kiribati"
    KM = "Comoros"
    KN = "Saint Kitts and Nevis"
    KP = "Korea, Democratic People's Republic of"
    KR = "Korea, Republic of"
    KW = "Kuwait"
    KY = "Cayman Islands"
    KZ = "Kazakhstan"
    LA = "Lao People's Democratic Republic"
    LB = "Lebanon"
    LC = "Saint Lucia"
    LI = "Liechtenstein"
    LK = "Sri Lanka"
    LR = "Liberia"
    LS = "Lesotho"
    LT = "Lithuania"
    LU = "Luxembourg"
    LV = "Latvia"
    LY = "Libya"
    MA = "Morocco"
    MC = "Monaco"
    MD = "Moldova, Republic of"
    ME = "Montenegro"
    MF = "Saint Martin (French part)"
    MG = "Madagascar"
    MH = "Marshall Islands"
    MK = "North Macedonia"
    ML = "Mali"
    MM = "Myanmar"
    MN = "Mongolia"
    MO = "Macao"
    MP = "Northern Mariana Islands"
    MQ = "Martinique"
    MR = "Mauritania"
    MS = "Montserrat"
    MT = "Malta"
    MU = "Mauritius"
    MV = "Maldives"
    MW = "Malawi"
    MX = "Mexico"
    MY = "Malaysia"
    MZ = "Mozambique"
    NA = "Namibia"
    NC = "New Caledonia"
    NE = "Niger"
    NF = "Norfolk Island"
    NG = "Nigeria"
    NI = "Nicaragua"
    NL = "Netherlands, Kingdom of the"
    NO = "Norway"
    NP = "Nepal"
    NR = "Nauru"
    NU = "Niue"
    NZ = "New Zealand"
    OM = "Oman"
    PA = "Panama"
    PE = "Peru"
    PF = "French Polynesia"
    PG = "Papua New Guinea"
    PH = "Philippines"
    PK = "Pakistan"
    PL = "Poland"
    PM = "Saint Pierre and Miquelon"
    PN = "Pitcairn"
    PR = "Puerto Rico"
    PS = "Palestine, State of"
    PT = "Portugal"
    PW = "Palau"
    PY = "Paraguay"
    QA = "Qatar"
    RE = "Réunion"
    RO = "Romania"
    RS = "Serbia"
    RU = "Russian Federation"
    RW = "Rwanda"
    SA = "Saudi Arabia"
    SB = "Solomon Islands"
    SC = "Seychelles"
    SD = "Sudan"
    SE = "Sweden"
    SG = "Singapore"
    SH = "Saint Helena, Ascension and Tristan da Cunha"
    SI = "Slovenia"
    SJ = "Svalbard and Jan Mayen"
    SK = "Slovakia"
    SL = "Sierra Leone"
    SM = "San Marino"
    SN = "Senegal"
    SO = "Somalia"
    SR = "Suriname"
    SS = "South Sudan"
    ST = "Sao Tome and Principe"
    SV = "El Salvador"
    SX = "Sint Maarten (Dutch part)"
    SY = "Syrian Arab Republic"
    SZ = "Eswatini"
    TC = "Turks and Caicos Islands"
    TD = "Chad"
    TF = "French Southern Territories"
    TG = "Togo"
    TH = "Thailand"
    TJ = "Tajikistan"
    TK = "Tokelau"
    TL = "Timor-Leste"
    TM = "Turkmenistan"
    TN = "Tunisia"
    TO = "Tonga"
    TR = "Türkiye"
    TT = "Trinidad and Tobago"
    TV = "Tuvalu"
    TW = "Taiwan, Province of China"
    TZ = "Tanzania, United Republic of"
    UA = "Ukraine"
    UG = "Uganda"
    UM = "United States Minor Outlying Islands"
    US = "United States of America"
    UY = "Uruguay"
    UZ = "Uzbekistan"
    VA = "Holy See"
    VC = "Saint Vincent and the Grenadines"
    VE = "Venezuela, Bolivarian Republic of"
    VG = "Virgin Islands (British)"
    VI = "Virgin Islands (U.S.)"
    VN = "Viet Nam"
    VU = "Vanuatu"
    WF = "Wallis and Futuna"
    WS = "Samoa"
    YE = "Yemen"
    YT = "Mayotte"
    ZA = "South Africa"
    ZM = "Zambia"
    ZW = "Zimbabwe"

    @property
    def code(self):
        return self.name.lower()

    def __str__(self):
        return self.code

    @classmethod
    def get_country_name(cls, code):
        return cls[code].value


def response_for(req_type: APIRequest):
    def dec(resp_klass: Type[BaseResponse]):
        RESPONSE_CLASS_MAP[req_type] = resp_klass
        return resp_klass

    return dec


class BaseRequest(BaseModel):
    retry: int = Field(0, description="The number of retries")
    cache: bool = Field(True, description="Whether to cache the response")

    # API specific fields
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
