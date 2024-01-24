#!/usr/bin/env python3
"""queries a collection and sorts by key"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """ Calculates and returns the average score of each student """
    pipeline = [
        {
            '$unwind': '$topics'
        },
        {
            '$group': {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}},
    ]
    return list(mongo_collection.aggregate(pipeline))
