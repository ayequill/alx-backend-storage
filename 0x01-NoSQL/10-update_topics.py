#!/usr/bin/env python3
"""Updates a document"""


def update_topics(mongo_collection, name, topics):
    """ Function that updates a doc with topics """
    mongo_collection.update_many({'name': name}, {
        '$set': {
            'topics': topics
        }
    })
