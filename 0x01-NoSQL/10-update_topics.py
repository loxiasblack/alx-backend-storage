#!/usr/bin/env python3
"""change the name with topics"""


def update_topics(mongo_collection, name, topics):
    """update the topics of school collection"""
    new_values = {"$set": {'topics': topics} }
    filter = {'name' : name}
    return mongo_collection.update_one(filter, new_values)
