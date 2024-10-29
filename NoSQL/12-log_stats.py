#!/usr/bin/env python3
""" NoSQL using PyMongo """
from pymongo import MongoClient


def log():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log()
