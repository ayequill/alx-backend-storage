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
        res = method(url, *args, **kwd)
        if get_data:
            return res
        redis_client.setex(key, 10, res)
        return res

    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator to count how many times a method is called """

    @wraps(method)
    def wrapper(url, *args, **kwd):
        key = f"count:{url}"
        redis_client.incr(key, 1)
        return method(url, *args, **kwd)

    return wrapper


@cache_data
@count_calls
def get_page(url: str) -> str:
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    # Simulate slow response for testing
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"

    # Access the slow URL multiple times to test counting and caching
    for _ in range(5):
        content = get_page(slow_url)
        print(content)

    # Print access count
    access_count = redis_client.get(f"count:{slow_url}")
    print(f"Access count for {slow_url}: {int(access_count)}")
