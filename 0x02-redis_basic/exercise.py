#!/usr/bin/env python3
""" A module for a cache instance """
from redis import Redis
from typing import Union, Callable, Any
from uuid import uuid4 as uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Counts how many times a method has been called """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self: Any, *args, **kwd) -> Any:
        self._redis.incr(key)
        return method(self, *args, **kwd)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs for a particular function. """
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self: Any, *args, **kwd) -> Any:
        self._redis.rpush(inputs, str(args))
        output = method(self, str(args))
        self._redis.rpush(outputs, output)
        return output

    return wrapper


class Cache:
    """ Cache Class for data persistence """

    def __init__(self):
        """ Initialize the instance """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Stores and returns a key """
        _id = str(uuid())
        self._redis.set(_id, data)
        return _id

    def get(self, key: str, fn: Union[Callable, None] = None) -> (
            Union)[str, bytes, int, float]:
        """ Gets a value from redis db with a specified key"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ Gets and returns a string """
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """ Gets and returns a number """
        return int(self._redis.get(key))
