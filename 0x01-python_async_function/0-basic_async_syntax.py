#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument (max_delay) and
waits for a random delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """
    Takes in an integer argument (max_delay) and waits for a random
    delay between 0 and max_delay (inclusive)

    Returns the random delay
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
