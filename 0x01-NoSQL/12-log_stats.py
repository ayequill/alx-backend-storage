#!/usr/bin/env python3
"""queries a collection and prints the results"""
from pymongo import MongoClient

if __name__ == "__main__":
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = db_client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(logs_db.count_documents({}), 'logs', '\nMethods:')
    for method in methods:
        print(f"\tmethod {method}:", logs_db.count_documents({"method": method}))
    print(logs_db.count_documents(
        {'method': 'GET', 'path': '/status'}), 'status check'
    )
