#!/usr/bin/env python3
""" Caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""

    def __init__(self):
        super().__init__()
        self.cache = []

    def put(self, key, item):
        """Add to cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = self.cache.pop(-2)
            self.cache_data.pop(discard_key)
            print(f"DISCARD: {discard_key}")

    def get(self, key):
        """Get from cache linked to key"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
