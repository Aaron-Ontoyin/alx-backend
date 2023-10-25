#!/usr/bin/env python3
"""LRU caching"""
from collections import deque
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching class"""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.lru = []
    
    def evict(self):
        """Evict the leaset recently used item in the cache (LRU)."""
        if self.lru and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.lru.pop()
            print(f"DISCARD: {lru}")

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            self.evict()
            self.cache_data[key] = item

    def get(self, key):
        """Get the associated value of key."""
        self.lru.remove(key) if key in self.lru else self.lru.append(key)
        return self.cache_data.get(key)
