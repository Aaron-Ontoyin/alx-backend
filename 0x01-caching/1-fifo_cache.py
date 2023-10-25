#!/usr/bin/env python3
"""FIFO caching"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class"""

    # def __init__(self):
    #     """Initialize"""
    #     super().__init__()
    #     self.queue = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    first_in = self.cache_data.keys()[-1]
                    del self.cache_data[first_in]
                    print(f"DISCARD: {first_in}")
                    # popped = self.queue.popitem(last=False)
                    # print(f"DISCARD: {popped[0]}")
                    # del self.cache_data[popped[0]]
            # self.cache_data[key] = item
            # self.queue[key] = 1


    def get(self, key):
        """Get the associated value of key"""
        return self.cache_data.get(key)