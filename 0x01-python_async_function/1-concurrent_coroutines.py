#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Takes in 2 int arguments (in this order): n and max_delay

    Returns a list of all the delays (float values)
    """

    delays = []  # List to store the delays

    # A list of coroutines to run concurrently
    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
