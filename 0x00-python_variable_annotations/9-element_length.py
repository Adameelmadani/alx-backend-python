#!/usr/bin/env python3
"""
This is our module
"""
from typing import
"""
This is typing module
"""


def element_length(lst: Iterable[Sequence[int]]) -> List[Tuple[Sequence[int], int]]:
    i: Sequence[int]
    return [(i, len(i)) for i in lst]
