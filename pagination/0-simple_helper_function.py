#!/usr/bin/env python3

""" sets python3 interpreter """


def index_range(page: int, page_size: int) -> tuple:
    """ Range function """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
