#!/usr/bin/env python3
"""
This is our module
"""
from typing import Callable
"""
This is our typing module
"""

    
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This is our multiplier func
    """
    def multiply(a: float) -> float:
        """
        This is multiply function callable one
        """
        f: float = a * multiplier
        return f
    return multiply
