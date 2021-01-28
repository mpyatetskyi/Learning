from collections import OrderedDict
import time


def cached(function):

    cache = OrderedDict()

    if len(cache) > 10:
        cache.popitem(last=False)

    def wrapper(func=function):

        if func in cache:
            result = cache[func]
            return result
        else:
            result = func
            cache[func] = result
            return result

    return wrapper

@cached
def power(a, b):
    time.sleep(4)
    return pow(a,b)

