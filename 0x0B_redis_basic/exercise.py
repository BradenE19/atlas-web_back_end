#!/usr/bin/env python3
"""Writes strings to Redis"""
import redis
from typing import Union
from uuid import uuid4, UUID

class Cache():
    """create Cache class"""
    def __init__(self):
        """method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a
        random key and return the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key
