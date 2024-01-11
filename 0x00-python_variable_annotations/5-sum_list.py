#!/usr/bin/env python3
"""
This is our module
"""


def sum_list(input_list: list[float]) -> float:
    """
    This is our sum_list
    """
    i: float
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
