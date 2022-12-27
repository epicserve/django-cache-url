import mock
import importlib

import django_cache_url

#
# HIREDIS
#


def test_hiredis():
    url = 'hiredis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_socket():
    url = 'hiredis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_hiredis_socket_with_username_password_dj3():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix://foo:bar@/path/to/socket?db=1'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['KEY_PREFIX'] == 'site1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_hiredis_socket_with_username_password_dj4():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix://foo@/path/to/socket?db=1&password=bar'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['KEY_PREFIX'] == 'site1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_hiredis_with_password_dj3():
    importlib.reload(django_cache_url)
    url = 'hiredis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_hiredis_with_password_dj4():
    importlib.reload(django_cache_url)
    url = 'hiredis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://:redispass@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_hiredis_with_username_dj3():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_hiredis_with_username_dj4():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_hiredis_with_username_password_dj3():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'bar'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_hiredis_with_username_password_dj4():
    importlib.reload(django_cache_url)
    url = 'hiredis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:bar@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


#
# REDIS
#

@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_dj3():
    importlib.reload(django_cache_url)
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_dj4():
    importlib.reload(django_cache_url)
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_socket_dj3():
    importlib.reload(django_cache_url)
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_socket_dj4():
    importlib.reload(django_cache_url)
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_socket_with_username_password_dj3():
    importlib.reload(django_cache_url)
    url = 'redis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix://foo:bar@/path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_socket_with_username_password_dj4():
    importlib.reload(django_cache_url)
    url = 'redis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix://foo@/path/to/socket?db=1&password=bar'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_with_password_dj3():
    importlib.reload(django_cache_url)
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_with_password_dj4():
    importlib.reload(django_cache_url)
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://:redispass@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_with_username_dj3():
    importlib.reload(django_cache_url)
    url = 'redis://foo:@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_with_username_dj4():
    importlib.reload(django_cache_url)
    url = 'redis://foo:@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


@mock.patch('django.VERSION', (3, 0, 0, "final", 0))
def test_redis_with_username_password_dj3():
    importlib.reload(django_cache_url)
    url = 'redis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'bar'


@mock.patch('django.VERSION', (4, 0, 0, "final", 0))
def test_redis_with_username_password_dj4():
    importlib.reload(django_cache_url)
    url = 'redis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:bar@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
