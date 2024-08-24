#!/usr/bin/env python3

""" Sets python3 interpreter """


def list_all(mongo_collection):
    """ list_all function, lists the mongo collection."""
    all_documents = mongo_collection.find()
    list_of_documents = list(all_documents)

    return list_of_documents
