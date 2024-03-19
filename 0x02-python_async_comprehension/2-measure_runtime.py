#!/usr/bin/env python3
"""
A coroutine that will execute
async_comprehension four times
in parallel using asyncio.gather
"""
import asyncio
import time
from importlib import import_module

async_comprehension = import_module(
        '1-async_comprehension'
        ).async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four
    times in parallel using
    asyncio.gather
    """

    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()

    return end_time - start_time
