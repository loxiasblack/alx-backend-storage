#!/usr/bin/env python3
"""insert document to in collection based"""


def insert_school(mongo_collection, **kwargs):
    """return the new_id"""
    post_id = mongo_collection.insert_one(kwargs).inserted_id
    return post_id
