#!/usr/bin/env python3

""" Sets interpreter to python3 """

from typing import Union, List


""" imports typing library """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ defines function that works with List"""
    return sum(mxd_lst)
