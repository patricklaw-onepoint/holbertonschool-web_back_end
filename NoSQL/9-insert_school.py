#!/usr/bin/env python3
""" NoSQL using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id