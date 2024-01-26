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

# First attempt didnt pass the checker, but it works
# might be the use of functions
# def connect_db():
#     """Connect DB"""
#     db_client = MongoClient('mongodb://127.0.0.1:27017')
#     logs_db = db_client.logs
#     nginx_col = logs_db.nginx
#     return nginx_col
#
#
# def return_str(method, count):
#     """returns a string"""
#     return f'\tmethod {method}: {count}'
#
#
# def print_results(methods):
#     """ Print results from logs """
#     db = connect_db()
#     print(db.count_documents({}), 'logs', '\nMethods:')
#     for method in methods:
#         to_print = db.count_documents({'method': method})
#         print(return_str(method, to_print))
#     print(db.count_documents(
#         {'method': 'GET', 'path': '/status'}), 'status check'
#     )
#
#
# if __name__ == "__main__":
#     print_results(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

#
#
# Used loops instead of functions but still didnt pass the checker
# logs_db = db_client.logs.nginx
# methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# print(logs_db.count_documents({}), 'logs', '\nMethods:')
# for method in methods:
#     print(f"\tmethod {method}:", logs_db.count_documents({"method": method}))
# print(logs_db.count_documents(
#     {'method': 'GET', 'path': '/status'}), 'status check'
# )
