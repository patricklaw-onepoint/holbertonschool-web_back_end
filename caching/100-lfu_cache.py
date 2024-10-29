#!/usr/bin/env python3
""" Caching module
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) caching"""

    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """Add to cache"""
        if not key or not item:
            return

        freq_copy = dict.copy(self.frequency)

        self.frequency[key] += 1
        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            min_freq_key = min(freq_copy, key=freq_copy.get)
            self.frequency.pop(min_freq_key, None)
            self.cache_data.pop(min_freq_key, None)
            print(f"DISCARD: {min_freq_key}")

    def get(self, key):
        """Get from cache linked to key"""
        if key is None:
            return None

        value = self.cache_data.get(key)

        if value is not None:
            self.frequency[key] += 1

        return value
