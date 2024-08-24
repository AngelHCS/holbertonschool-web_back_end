#!/usr/bin/env python3

"""Sets python3 interpreter """


def insert_school(mongo_collection, **kwargs):
    """inserts a new file, takes kwargs as input """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
