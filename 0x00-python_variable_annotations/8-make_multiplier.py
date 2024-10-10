#!/usr/bin/env python3
"""Returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a function that
    multiplies a float by this multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the given value by the outer multiplier.
        """
        return value * multiplier
    return multiplier_function
