#!/usr/bin/env python3
""" module finds all docs in a collection"""
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from typing import List


def list_all(mongo_collection: Collection) -> Cursor:
    """ Queries and returns all docs in a collection"""
    cursor: Cursor = mongo_collection.find({})
    return cursor
