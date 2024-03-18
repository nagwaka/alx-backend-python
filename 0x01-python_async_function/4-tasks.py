#!/usr/bin/env python3
"""
Take the code from wait_n and alters it into a new function task_wait_n
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alters it into a new
    function task_wait_n
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
