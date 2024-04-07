from hashlib import md5


# Dead simple cache implementation. This should only persist for the duration
# of a series of requests and is not intended to be used as a long-term cache.
# One reasonable enhancement would be to add a TTL to the cache entries or LRU
# functionality so it doesn't unbounded.
class Cache:
    def __init__(self):
        self.store = {}

    def get(self, key):
        return self.store.get(key)

    def set(self, key, value):
        self.store[key] = value

    def delete(self, key):
        del self.store[key]

    def create_key(self, endpoint: str, params: dict):
        return f"{endpoint}:{md5(str(params).encode()).hexdigest()}"
