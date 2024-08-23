#!/usr/bin/env python3

""" Setting interpreter """

import asyncio
import random


async def wait_random(max_delay: int) -> float:

    """ Wait_Random function max delay being an int """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:

    """ Wait function """

    return asyncio.create_task(wait_random(max_delay))
