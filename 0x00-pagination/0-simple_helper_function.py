#!/usr/bin/env python3
"""0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a size-two tuple with a start index and an end index that represent the range of indexes that should be returned in a list for those specific pagination criteria.
    parameter
        @page: the page number that is currently displayed; @page_size: the quantity of elements on a page
    return: a two-sized tuple with a start index and an end index

    """
    return ((page - 1) * page_size, page * page_size)
