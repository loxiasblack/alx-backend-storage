#!/usr/bin/env python3
"""change the name with topics"""


def update_topics(mongo_collection, name, topics):
    """update the topics of school collection"""
    return mongo_collection.update_one({'name': name},
                                       {"$set": {'topics': topics}})
