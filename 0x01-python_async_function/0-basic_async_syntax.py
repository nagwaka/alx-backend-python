#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument (max_delay) and
waits for a random delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Takes in an integer argument (max_delay) and waits for a random
    delay between 0 and max_delay (inclusive)

    Returns the random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
