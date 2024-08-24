#!/usr/bin/env python3


""" sets it to use the Python 3 interpreter"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """ comprehesion func to return list of float """

    return [num async for num in async_generator()]
