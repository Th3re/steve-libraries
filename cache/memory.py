import time
import logging

from .cache import Cache

LOG = logging.getLogger(__name__)


class MemoryAccessCache(Cache):
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl):
        expiration_date = time.time() + ttl
        self.cache[key] = value, expiration_date

    def get(self, key):
        value, expiration_date = self.cache.get(key, (None, None))
        if value:
            if expiration_date - time.time() <= 0:
                LOG.debug(f'Value \"{value}\" for \"{key}\" key has expired, deleting it')
                del self.cache[key]
                return
            else:
                LOG.debug(f'Using cached value \"{value}\" for key \"{key}\"')
        return value
