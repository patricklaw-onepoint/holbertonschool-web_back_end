#!/usr/bin/env python3
""" NoSQL using PyMongo """


def top_students(mongo_collection):
    # Aggregate pipeline to calculate average score and sort students
    pipeline = [
        {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
        {"$project": {"_id": 0, "name": 1, "averageScore": 1}},
    ]

    return mongo_collection.aggregate(pipeline)
