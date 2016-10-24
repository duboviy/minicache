<h1><img src="https://raw.githubusercontent.com/duboviy/minicache/master/logo.png" height=85 alt="logo" title="logo"> minicache</h1>

Python memory caching utilities for Python 2 and 3 versions, also PyPy.

by [Eugene Duboviy](https://duboviy.github.io/)

[![Build Status](https://travis-ci.org/duboviy/minicache.svg?branch=master)](https://travis-ci.org/duboviy/minicache) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/0dd178380aca4c5c80c45d10d5935320)](https://www.codacy.com/app/dubovoy/minicache?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/minicache&amp;utm_campaign=Badge_Grade) [![PyPI](https://img.shields.io/pypi/v/minicache.svg)](https://pypi.python.org/pypi/minicache) [![Code Health](https://landscape.io/github/duboviy/minicache/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/minicache/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/duboviy/minicache/) [![PRs & Issues Welcome](https://img.shields.io/badge/PRs%20&%20Issues-welcome-brightgreen.svg)](https://github.com/duboviy/minicache/pulls) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/duboviy/minicache/)

## Why?

A major problem of [funcy.memoize](http://funcy.readthedocs.org/en/stable/calc.html#memoize) you couldn't test with it because there was no (obvious) way to turn it off.
This project was created to suit the "memoization" needs, with a hook to turn it off (for testing or other purposes).

## Current features

* Simple set and get workflow
* Decorator for "memoization" class methods and functions
* Enabling and disabling functionality (including a context manager)
* No additional packages required to be installed (using only standard python lib)

## Installation

Install from PyPI:
```
pip install minicache
```
Or using alternative command:
```
pip install https://github.com/duboviy/minicache/archive/master.zip
```
Or from source use:
```
python setup.py install
```

## Supported python versions

  * 2.7
  * 3.3
  * 3.4
  * 3.5
  * PyPy

## PyPI

* [Package](https://pypi.python.org/pypi/minicache)
* [Documentation](https://pythonhosted.org/minicache/)

## Examples

Basic usage
```python
>>> from minicache import cache
>>> cache.has('key')
False
>>> cache.get('key', default='default')
'default'
>>> cache.update('key', 'value')
>>> cache.get('key')
'value'
>>> cache.disable()
>>> cache.get('key')
```

Decorator and context manager
```python
from minicache import cache
import time

@cache.this
def somefunc():
    time.sleep(5)
    return "this will be cached, and you won't have to wait a second time!"

def test_somefunc():
    somefunc()
    somefunc()
    with cache.temporarily_disabled():
        # now we'll have to wait again
        somefunc()
```

Decorator for "memoization" class methods:
```python
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
```

... and many other features


## License

**MIT** licensed library. See [LICENSE](LICENSE) for details.

## Contributing

If you have suggestions for improving the minicache, please [open an issue or
pull request on GitHub](https://github.com/duboviy/minicache/).

## Badges

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/minicache/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/minicache/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/minicache/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/minicache/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/minicache/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/minicache/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/minicache/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/minicache/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/minicache/)
