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

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status_check} status check")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
    ]
    commonIps = collection.aggregate(pipeline)

    print("IPs:")
    for item in commonIps:
        ip = item.get("ip")
        count = item.get("count")
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log()
