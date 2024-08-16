#!/usr/bin/env python3
import asyncio
import random

# intro comment


async def wait_random(max_delay: int = 10) -> float:

    # def function

    random.seed(47)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

    # What it does

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
