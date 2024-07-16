#!/usr/bin/env python3
"""List all document with pymongo"""


def list_all(mongo_collection):
    """function that list all document"""
    list = mongo_collection.find({})
    if list:
        return list
    return []
