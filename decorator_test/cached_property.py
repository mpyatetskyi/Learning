from collections import OrderedDict
import functools
import time

def limit(par=10):

    limit = par

    def cached(function):

        cache = OrderedDict()

        @functools.wraps(function)
        def wrapper(*args):

            if len(cache) > limit:
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

    return cached

@limit(1)
def power(x, y):

    time.sleep(3)
    return x**y

@limit
def added(a):
    time.sleep(3)
    return a+a

