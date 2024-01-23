#!/usr/bin/env python3
"""module finds all docs in a collection"""


def list_all(mongo_collection):
    """ Queries and returns all docs in a collection"""
    cursor = mongo_collection.find()
    return list(cursor)
