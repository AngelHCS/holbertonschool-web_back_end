#!/usr/bin/env python3

""" setting python3 interpreter """


import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:

    """ generator function, num between 0-10 """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
