#!/usr/bin/env python3
import asyncio
from typing import List
import random

# intro comment


async def wait_random(max_delay: int = 10) -> float:

    # Function comment

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:

    # Function comment

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
