#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """LFU caching class"""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.lfu = dict()

    def evict(self):
        """Evict the least frequently used item in the cache (LFU)."""
        if self.lfu and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu = sorted(self.lfu.items(), key=lambda x: x[1])[0][0]
            del self.cache_data[lfu]
            print(f"DISCARD: {lfu}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            self.evict()
            self.cache_data[key] = item

    def get(self, key):
        """Get the associated value of key."""
        if key in self.lfu.keys():
            self.lfu[key] = 1
        else:
            self.lfu[key] += 1
        return self.cache_data.get(key)
