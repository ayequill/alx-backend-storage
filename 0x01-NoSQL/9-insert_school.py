#!/usr/bin/env python3
"""module that inserts a doc in school"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a doc in collection """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
