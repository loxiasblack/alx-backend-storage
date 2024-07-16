#!/usr/bin/env python3
"""list of school with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return the find algo"""
    return mongo_collection.find({'topics': topic})
