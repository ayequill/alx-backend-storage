#!/usr/bin/env python3
"""queries a collection and prints the results"""
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


def connect_db():
    """Connect DB"""
    db_client: MongoClient = MongoClient('mongodb://127.0.0.1:27017')
    logs_db: Database = db_client.logs
    nginx_col: Collection = logs_db.nginx
    return nginx_col


def return_str(method: str, count: int):
    """returns a string"""
    return f'\tmethod {method}: {count}'


def print_results(methods):
    """ Print results from logs """
    db = connect_db()
    print(db.count_documents({}), 'logs', '\nMethods:')
    for method in methods:
        to_print = db.count_documents({'method': method})
        print(return_str(method, to_print))
    print(db.count_documents(
        {'method': 'GET', '$and': [{'path': '/status'}]}), 'status check'
    )


if __name__ == "__main__":
    print_results(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
