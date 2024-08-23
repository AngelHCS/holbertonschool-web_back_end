#!/usr/bin/env python3

""" sets python3 interpreter"""

from typing import Callable

""" imports Callable function from typing library """


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function to make multiplier takes float as arg"""

    def multiplier_function(x: float) -> float:
        """ Multiplier function """

        return x * multiplier
    return multiplier_function
