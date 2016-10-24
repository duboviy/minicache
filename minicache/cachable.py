from collections import defaultdict


class Cacheable(object):
    """ Use it as a Base class (inherit from it) to cache result of specific methods. """
    def __init__(self):
        self._cache = defaultdict(dict)

    def clear_cache(self):
        self._cache.clear()

    @staticmethod
    def cached(member):

        def wrapper(self, *args, **kwargs):

            memberCache = self._cache[member]

            if len(args) > 0 and len(kwargs) > 0:
                key = args, frozenset(kwargs)
            elif len(args) > 0:
                key = args
            elif len(kwargs) > 0:
                key = frozenset(kwargs)
            else:
                key = 0

            value = memberCache.get(key, None)

            if value is None:
                value = memberCache[key] = member(self, *args, **kwargs)

            return value

        return wrapper


if __name__ == '__main__':
    # Example of usage
    class Foo(Cacheable):
        def __init__(self):
            super(Foo, self).__init__()
            self._bar = 5

        @property
        @Cacheable.cached
        def m1(self):
            print('actual call property...', self._bar)
            return self._bar

        @Cacheable.cached
        def m2(self, a, b, k=4, m=10):
            s = a + b + k + m
            print('actual call method...', a, b, k, m, s)
            return s

        @Cacheable.cached
        def m3(self, a=3, b=2):
            s = a + b
            print('actual call method (kwargs only)', a, b, s)
            return s
