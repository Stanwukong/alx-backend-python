#!/usr/bin/env python3
"""Returns a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and a number v (int or float), and returns a tuple
    where the first element is k, and the second element is the square of
    v as a float.
    """
    return (k, float(v ** 2))
