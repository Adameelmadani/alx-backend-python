#!/usr/bin/env python3
"""
This is our module
"""
from typing import List
"""
This is our typing module
"""


def sum_list(input_list: List[float]) -> float:
    """
    This is our sum_list
    """
    i: float
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
