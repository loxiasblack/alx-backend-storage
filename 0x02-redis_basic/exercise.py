#!/usr/bin/env python3
"""Module to implement a simple caching system using Redis."""
import redis
import uuid
from typing import Union


class Cache:

    def __init__(self):
        """ initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in the cache"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
