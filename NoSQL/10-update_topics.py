#!/usr/bin/env python3

""" Sets python3 interpreter """


def update_topics(mongo_collection, name, topics):
    """ Updates topic depending on name """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result.modified_count
