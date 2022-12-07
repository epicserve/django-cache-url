import django_cache_url


def test_pymemcache_url_returns_pymemcache_cache():
    url = 'pymemcache://127.0.0.1:11211?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django.core.cache.backends.memcached.PyMemcacheCache'
    assert config['LOCATION'] == '127.0.0.1:11211'
    assert config['KEY_PREFIX'] == 'site1'


def test_pymemcache_url_multiple_locations():
    url = 'pymemcache://127.0.0.1:11211,192.168.0.100:11211?key_prefix=site1'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == '127.0.0.1:11211;192.168.0.100:11211'


def test_pymemcache_socket_url():
    url = 'pymemcache:///path/to/socket/'
    config = django_cache_url.parse(url)
    assert config['LOCATION'] == 'unix:///path/to/socket/'
