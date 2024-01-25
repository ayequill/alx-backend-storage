#!/usr/bin/env python3
""" A module for a cache instance """
from redis import Redis
from typing import Union
from uuid import uuid4 as uuid


class Cache:
    """ Cache Class for data persistence """

    def __init__(self):
        """ Initializer """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """ Stores and returns a key """
        _id = str(uuid())
        self._redis.set(_id, data)
        return _id
