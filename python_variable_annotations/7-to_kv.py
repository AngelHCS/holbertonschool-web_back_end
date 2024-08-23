#!/usr/bin/env python3

""" sets python3 interpreter """

from typing import Union, Tuple

""" importing functions from typing """


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Defines function, trying to fix this for documentation check """
    return (k, float(v ** 2))
