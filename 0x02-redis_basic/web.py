#!/usr/bin/env python3
""" A module for a cache instance """
import requests
from redis import Redis
from functools import wraps
from typing import Callable, Awaitable

redis_client = Redis()


def cache_data(method: Callable) -> Callable:
    """ Decorator to cache with expiry """

    @wraps(method)
    def wrapper(url, *args, **kwd):
        key = f"cache:{url}"
        get_data = redis_client.get(key)
        if get_data:
            return get_data.decode("utf-8")
        res = method(url, *args, **kwd)
        redis_client.setex(key, 10, res)
        return res

    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called """

    @wraps(method)
    def wrapper(url, *args, **kwd):
        key = f"count:{url}"
        print(key)
        redis_client.incr(key)
        return method(url, *args, **kwd)

    return wrapper


@cache_data
@count_calls
def get_page(url: str) -> str:
    res = requests.get(url)
    return res.text
