#!/usr/bin/env python3
from typing import Union, Tuple

"""importing functions from typing"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Defines a function, K as a string,V as int or float returns tuple"""
    return (k, float(v ** 2))
