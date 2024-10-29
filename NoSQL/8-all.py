#!/usr/bin/env python3
""" NoSQL using PyMongo """


def list_all(mongo_collection):
    """lists all documents in a collection
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object"""
    doc_list = []

    docs = mongo_collection.find()
    for doc in docs:
        doc_list.append(doc)

    return doc_list
