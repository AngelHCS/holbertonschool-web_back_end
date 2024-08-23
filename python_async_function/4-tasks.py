#!/usr/bin/env python3

""" sets python3 interpreter"""

import asyncio
from typing import List

""" importing libraries"""


async def wait_random(max_delay: int) -> float:
    """ func comment"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ func comment"""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ func comment """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
