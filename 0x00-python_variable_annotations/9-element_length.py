#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence
"""Returns a list of tuples"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
       Takes an iterable of sequences and returns a list of tuples.
       Each tuple contains a sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
