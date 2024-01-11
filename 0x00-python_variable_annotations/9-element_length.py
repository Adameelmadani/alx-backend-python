#!/usr/bin/env python3
"""
This is our module
"""
from typing import Sequence, Iterable, Tuple, List
"""
This is typing module
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    i: Sequence
    return [(i, len(i)) for i in lst]
