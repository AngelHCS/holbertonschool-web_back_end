#!/usr/bin/env python3

""" Starting """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """defines function that will annotate with the other main file"""

    return [(i, len(i)) for i in lst]
