#!/usr/bin/env python3
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """ Queries and returns all docs in a collection"""
    cursor: Cursor = mongo_collection.find({})
    return list(cursor)
