#!/usr/bin/env python3
import asyncio
import time
from typing import List
import random

# intro comment


async def wait_random(max_delay: int) -> float:

    # function comment

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:

    # function comment

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays


def measure_time(n: int, max_delay: int) -> float:

    # function comment

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
