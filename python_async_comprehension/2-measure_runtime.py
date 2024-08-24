#!/usr/bin/env python3

""" uses python3 interpreter """


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ returns function runtime """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.perf_counter()

    return end_time - start_time
