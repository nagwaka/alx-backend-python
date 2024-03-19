#!/usr/bin/env python3
"""
A coroutine called async_comprehension that takes no arguments.
"""
from typing import List
from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using
    an async comprehensing over
    async_generator
    """

    return [num async for num in async_generator()]
