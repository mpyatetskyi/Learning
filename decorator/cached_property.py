import functools
import time

def cached(function):

    cache = {}

    @functools.wraps(function)
    def wrapper(*args):

        signature = (function, *args)

        if signature in cache:
            result = cache[signature]
        else:
            result = function(*args)
            cache[signature] = result

        return result

    return wrapper

@cached
def power(x,y):

    time.sleep(3)
    return x**y

@cached
def added(a):
    time.sleep(3)
    return a+a
