#!/usr/bin/env python3
import asyncio
import random

# Intro comment


async def wait_random(max_delay: int) -> float:

    # func comment

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:

    # func comment

    return asyncio.create_task(wait_random(max_delay))
