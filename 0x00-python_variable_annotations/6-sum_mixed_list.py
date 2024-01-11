#!/usr/bin/env python3
"""
This is our module
"""
from typing import Union, List
"""
This is typing module
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This is our sum mixed func
    """
    sum: float = 0
    i: int
    for i in range(0, len(mxd_lst)):
        sum += float(mxd_lst[i])
    return sum
