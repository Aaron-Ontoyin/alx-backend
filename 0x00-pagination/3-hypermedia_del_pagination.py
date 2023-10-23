#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary of:
            - index: the current start index of the return page.
            That is the index of the first item in the current page.
            For example if requesting page 3 with page_size 20,
            and no data was removed from the dataset,
            the current index should be 60.
            - next_index: the next index to query with. That should
            be the index of the first item after the last item on
            the current page.
            - page_size: the current page size
            - data: the actual page of the dataset
        """
        assert type(index) is int
        assert index >= 0 and index < len(self.dataset())
        data_dict = {
            "index": index,
            "data": [
                self.indexed_dataset()[i]
                for i in range(index, index + page_size)
                ],
            "page_size": page_size,
            "next_index": index + page_size
        }
        return data_dict
