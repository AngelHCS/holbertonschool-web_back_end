#!/usr/bin/env python3
""" Sets python3 interpreter """


def schools_by_topic(mongo_collection, topic):
    """ Lists the school using topici as arg """
    all_documents = mongo_collection.find({"topics": topic})
    list_of_documents = list(all_documents)

    return list_of_documents
