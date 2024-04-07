from unittest.mock import MagicMock, patch

import pytest
from httpx import Response

from cache import Cache


def test_cache_set_get():
    cache = Cache()
    key = "this_is_a_key"
    value = Response(
        status_code=200,
        content=b'{"message": "Im not sure smoke tests are a good idea"}',
    )
    cache.set(key, value)
    assert cache.get(key) == value
