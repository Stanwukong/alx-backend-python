#!/usr/bin/env python3
"""Returns the sum of a list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
       Calculates the sum of a list of floats.
    """
    sum: float = 0
    for num in input_list:
        sum += num

    return sum
