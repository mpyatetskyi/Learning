from collections import OrderedDict
import functools
import time

def cached(function):

    cache = OrderedDict()

    @functools.wraps(function)
    def wrapper(*args):

        if len(cache) > 10:
            print('i deleted one item')
            cache.popitem(last=False)

        signature = (function, *args)

        if signature in cache:
            print('i returned result')
            result = cache[signature]
        else:
            print('i added one result')
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
