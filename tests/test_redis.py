import pytest

from django import VERSION as DJANGO_VERSION

import django_cache_url

#
# HIREDIS
#


def test_hiredis():
    url = 'hiredis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_socket():
    url = 'hiredis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


#
# REDIS
#

def test_redis_dj4():
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'


def test_redis_socket():
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url.parse(url)

    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'OPTIONS' not in config


@pytest.mark.skipif(DJANGO_VERSION[0] >= 4, reason="requires Django 3 or lower")
def test_redis_with_password_dj3():
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'


@pytest.mark.skipif(DJANGO_VERSION[0] < 4, reason="requires Django 4 or higher")
def test_redis_with_password_dj4():
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://:redispass@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
