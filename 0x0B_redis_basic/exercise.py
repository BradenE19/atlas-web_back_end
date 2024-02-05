#!/usr/bin/env python3
"""Writes strings to Redis"""
import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """takes a single arguement,
     returns a Callable """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorator functionality"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    """create Cache class"""
    def __init__(self):
        """method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store input daata in Redis
        use random key to return key
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert data to desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """ Parameterizes a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
