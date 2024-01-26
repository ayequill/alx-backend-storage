#!/usr/bin/env python3
"""queries a collection and prints the results"""
from pymongo import MongoClient

if __name__ == "__main__":
    db_client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = db_client.logs.nginx
    print(logs_db.count_documents({}), 'logs', '\nMethods:')
    print("\tmethod GET:", logs_db.count_documents({"method": "GET"}))
    print("\tmethod POST:", logs_db.count_documents({"method": "POST"}))
    print("\tmethod PUT:", logs_db.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:", logs_db.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:", logs_db.count_documents({"method": "DELETE"}))
    print(logs_db.count_documents({
        "method": "GET", "path": "/status"
    }), "status check")
