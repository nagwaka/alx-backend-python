#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float by multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
