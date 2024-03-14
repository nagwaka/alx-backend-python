#!/usr/bin/env python3
"""
Zooms a list by repeating each element a specified number of times
"""

from typing import List, Union


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Zooms a list by repeating each element a specified number of times.

    Args:
        lst: The input list.
        factor: The number of times to repeat each element (default is 2).

    Returns:
        A new list with the zoomed elements.
    """

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)  # Now uses a list as input

zoom_3x = zoom_array(array, 3)  # Use an integer for factor
