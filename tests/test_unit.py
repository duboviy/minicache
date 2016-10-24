from minicache import cache


def test_has_disabled():
    cache.set('test_has_disabled', 'value')
    assert cache.has('test_has_disabled') is True
    cache.options.enabled = False
    assert cache.has('test_has_disabled') is False
    cache.options.enabled = True


def test_set_disabled():
    cache.options.enabled = False
    cache.set('test_set_disabled', 'value')
    assert cache.has('test_set_disabled') is False
    cache.options.enabled = True
    cache.set('test_set_disabled', 'value')
    assert cache.has('test_set_disabled') is True


def test_get_disabled():
    cache.set('test_get_disabled', 'value')
    assert cache.get('test_get_disabled') == 'value'
    cache.options.enabled = False
    assert cache.get('test_get_disabled') is None
    cache.options.enabled = True


def test_clear_disabled():
    cache.set('test_clear_disabled', 'value')
    cache.options.enabled = False
    cache.clear()
    cache.options.enabled = True
    assert cache.has('test_clear_disabled') is True


def test_this():
    entry = {'flag': False}

    @cache.this
    def testable(arg, kwarg=None):
        entry['flag'] = True
        return arg, kwarg

    assert testable('arg') == ('arg', None)
    assert entry['flag'] is True
    entry['flag'] = False
    assert testable('arg') == ('arg', None)
    assert entry['flag'] is False
    assert testable('arg', 'kwarg') == ('arg', 'kwarg')
    assert entry['flag'] is True
    cache.options.enabled = False
    entry['flag'] = False
    assert testable('arg') == ('arg', None)
    assert entry['flag'] is True
    cache.options.enabled = True


def test_disable_no_clear():
    cache.set('test_disable_no_clear', 'value')
    cache.disable(clear_cache=False)
    assert cache.has('test_disable_no_clear') is False
    cache.enable()
    assert cache.has('test_disable_no_clear') is True
