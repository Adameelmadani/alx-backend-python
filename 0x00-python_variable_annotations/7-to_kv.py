#!/usr/bin/env python3
"""
This is our module
"""
from typing import Union, Tuple
"""
This is typing module
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This is our kv function
    """
    f: float = float(v * v)
    t: Tuple[str, float] = (k, f)
    return t
