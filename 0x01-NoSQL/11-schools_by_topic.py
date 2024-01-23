#!/usr/bin/env python3
"""queries a collection"""


def schools_by_topic(mongo_collection, topic):
    """ Finds school with specific topic """
    found = mongo_collection.find({'topics': topic})
    return list(found)
