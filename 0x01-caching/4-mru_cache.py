#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """MRU caching class"""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.mru = []

    def evict(self):
        """Evict the most recently used item in the cache (MRU)."""
        if self.mru and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.mru.pop()
            print(f"DISCARD: {mru}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            self.evict()
            self.cache_data[key] = item

    def get(self, key):
        """Get the associated value of key."""
        if key in self.mru:
            self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data.get(key)
