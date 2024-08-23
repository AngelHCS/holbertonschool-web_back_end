#!/usr/bin/env python3

""" Setting interpreter """

import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:

    """ Function """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:

    """ Function """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
