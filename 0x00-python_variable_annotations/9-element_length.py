#!/usr/bin/env python3
"""
annotate the function element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return a list of tuples containing elements from lst
    along with their lengths
    """
    return [(i, len(i)) for i in lst]
