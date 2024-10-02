#!/usr/bin/env python3
""" NoSQL using PyMongo """
from pymongo import MongoClient

if __name__ == "__main__":
    """provides some stats about Nginx logs stored in MongoDB"""
    collection = MongoClient("mongodb://127.0.0.1:27017").logs.nginx

    print(f"{collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
