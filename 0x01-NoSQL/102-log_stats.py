#!/usr/bin/env python3
"""queries a collection and prints the results"""
from pymongo import MongoClient


def connect_db():
    """Connect DB"""
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = db_client.logs
    nginx_col = logs_db.nginx
    return nginx_col


def print_results(methods=None):
    """ Print results from logs """
    if methods is None:
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    db = connect_db()
    print(db.count_documents({}), 'logs', '\nMethods:')
    for method in methods:
        to_print = db.count_documents({'method': method})
        print(f'\tmethod {method}: {to_print}')
    print(db.count_documents(
        {'method': 'GET', 'path': '/status'}), 'status check'
    )

    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'sum': {'$sum': 1}
            }
        },
        {
            '$sort': {'sum': -1}
        },
        {
            '$limit': 10
        }
    ]

    top = db.aggregate(pipeline)
    print('IPs:')
    [print(f'\t{obj["_id"]}: {obj["sum"]}') for obj in top]


print_results()
