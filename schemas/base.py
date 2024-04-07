from enum import Enum
from typing import Dict, Generic, Type, TypeVar

from pydantic import BaseModel, Field, PrivateAttr

APIRequest = TypeVar("APIRequest", bound="BaseRequest")

RESPONSE_CLASS_MAP = {}


class AllBacklinksSelect(str, Enum):
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


class CountryCode(str, Enum):
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

    def make_params(self) -> Dict[str, str]:
        params = self.dict(exclude={"retry", "cache"})
        filtered_params = {k: v for k, v in params.items() if v is not None}
        return filtered_params


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
