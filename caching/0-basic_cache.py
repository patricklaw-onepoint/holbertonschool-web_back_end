#!/usr/bin/env python3
""" Caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """
        Add to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get from cache linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
