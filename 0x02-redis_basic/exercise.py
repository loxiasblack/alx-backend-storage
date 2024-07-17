#!/usr/bin/env python3
"""Module to implement a simple caching system using Redis."""
import redis
import uuid
from typing import Union


class Cache:

    def __init__(self):
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self.__redis.set(random_key, data)
        return random_key
