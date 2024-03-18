#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Takes in 2 int arguments (in this order): n and max_delay

    Returns a list of all the delays (float values)
    """

    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
