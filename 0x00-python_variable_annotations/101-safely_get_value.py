#!/usr/bin/env python3
"""
adds type annotations to the function
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')  # Define a generic type variable T


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:

    """
    safely retrieve a value from a dictionary with a default value
    if the key is not found
    """

    if key in dct:
        return dct[key]
    else:
        return default
