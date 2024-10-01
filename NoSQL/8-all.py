#!/usr/bin/env python3
""" NoSQL using PyMongo """


def list_all(mongo_collection):
    """lists all documents in a collection
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object"""

    if not mongo_collection:
        return []
    return list(mongo_collection.find())
