#!/usr/bin/env python3
"""give me some logs stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    x = nginx_collection.count_documents({})
    print("{} logs".format(x))
    print("Methods:")

    for item in method:
        y = nginx_collection.count_documents({"method": item})
        print("\tmethod {}: {}".format(item, y))
    z = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(z))
