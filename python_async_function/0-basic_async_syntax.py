#!/usr/bin/env python3

""" setting interpreter to use """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """ function that waits, max of 10 """

    random.seed(47)
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

    """ returns the delay between the start and finish """

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
