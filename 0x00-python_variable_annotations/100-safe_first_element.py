#!/usr/bin/env python3
"""
Augments code with the correct duck-typed annotations
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:

    """
    return the first element of the sequence lst if
    it's not empty,otherwise returns None
    """
    if lst:
        return lst[0]
    else:
        return None
