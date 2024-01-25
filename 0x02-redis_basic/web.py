#!/usr/bin/env python3
""" A module for a cache instance """
import requests
from redis import Redis
from functools import wraps
from typing import Callable

redis_client = Redis()


def cache_data(method: Callable[..., str]) -> Callable[..., str]:
    """ Decorator to cache with expiry """

    @wraps(method)
    def wrapper(url: str, *args, **kwd) -> str:
        """ Wrapper function """
        key = f"cache:{url}"
        get_data = redis_client.get(key)
        res = method(url, *args, **kwd)
        if get_data:
            return res
        redis_client.setex(key, 10, res)
        return res

    return wrapper


def count_calls(method: Callable[..., str]) -> Callable[..., str]:
    """ Decorator to count how many times a method is called """

    @wraps(method)
    def wrapper(url: str, *args, **kwd) -> str:
        """ Wrapper function """
        key = f"count:{url}"
        redis_client.incr(key, 1)
        return method(url, *args, **kwd)

    return wrapper


@cache_data
@count_calls
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    res = requests.get(url)
    return res.text
