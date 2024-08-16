#!/usr/bin/env python3
from typing import Callable

""" imports Callable function from typing library"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    #comment here

    def multiplier_function(x: float) -> float:
        #comment

        return x * multiplier
    return multiplier_function
