
# region HIREDIS url
def test_hiredis_dj3(django_cache_url_dj3):
    url = 'hiredis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_dj4(django_cache_url_dj4):
    url = 'hiredis://127.0.0.1:6379/0?key_prefix=site1&pool_class=redis.BlockingConnectionPool'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'
    assert config['OPTIONS']['pool_class'] == 'redis.BlockingConnectionPool'


def test_hiredis_with_password_dj3(django_cache_url_dj3):
    url = 'hiredis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_with_password_dj4(django_cache_url_dj4):
    url = 'hiredis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://:redispass@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'


def test_hiredis_with_username_dj3(django_cache_url_dj3):
    url = 'hiredis://foo:@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_with_username_dj4(django_cache_url_dj4):
    url = 'hiredis://foo:@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'


def test_hiredis_with_username_password_dj3(django_cache_url_dj3):
    url = 'hiredis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'bar'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_with_username_password_dj4(django_cache_url_dj4):
    url = 'hiredis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:bar@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'
# endregion


# region HIREDIS socket
def test_hiredis_socket_dj3(django_cache_url_dj3):
    url = 'hiredis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_socket_dj4(django_cache_url_dj4):
    url = 'hiredis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'


def test_hiredis_socket_with_username_password_dj3(django_cache_url_dj3):
    url = 'hiredis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix://foo:bar@/path/to/socket?db=1'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert config['KEY_PREFIX'] == 'site1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_socket_with_username_password_dj4(django_cache_url_dj4):
    url = 'hiredis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix://foo@/path/to/socket?db=1&password=bar'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
    assert 'PARSER_CLASS' not in config.get('OPTIONS', {})
    assert config['KEY_PREFIX'] == 'site1'
    assert config['OPTIONS']['parser_class'] == 'redis.connection.HiredisParser'
# endregion


# region REDIS url
def test_redis_dj3(django_cache_url_dj3):
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['KEY_PREFIX'] == 'site1'


def test_redis_dj4(django_cache_url_dj4):
    url = 'redis://127.0.0.1:6379/0?key_prefix=site1'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['KEY_PREFIX'] == 'site1'


def test_redis_with_password_dj3(django_cache_url_dj3):
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'redispass'


def test_redis_with_password_dj4(django_cache_url_dj4):
    url = 'redis://:redispass@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://:redispass@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


def test_redis_with_username_dj3(django_cache_url_dj3):
    url = 'redis://foo:@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


def test_redis_with_username_dj4(django_cache_url_dj4):
    url = 'redis://foo:@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})


def test_redis_with_username_password_dj3(django_cache_url_dj3):
    url = 'redis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DEFAULT_REDIS_BACKEND
    assert config['LOCATION'] == 'redis://foo@127.0.0.1:6379/0'
    assert config['OPTIONS']['PASSWORD'] == 'bar'


def test_redis_with_username_password_dj4(django_cache_url_dj4):
    url = 'redis://foo:bar@127.0.0.1:6379/0'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'redis://foo:bar@127.0.0.1:6379/0'
    assert 'PASSWORD' not in config.get('OPTIONS', {})
# endregion


# region REDIS socket
def test_redis_socket_dj3(django_cache_url_dj3):
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


def test_redis_socket_dj4(django_cache_url_dj4):
    url = 'redis:///path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix:///path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


def test_redis_socket_with_username_password_dj3(django_cache_url_dj3):
    url = 'redis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'unix://foo:bar@/path/to/socket?db=1'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'


def test_redis_socket_with_username_password_dj4(django_cache_url_dj4):
    url = 'redis://foo:bar@/path/to/socket/1?key_prefix=site1'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'unix://foo@/path/to/socket?db=1&password=bar'
    assert 'OPTIONS' not in config
    assert config['KEY_PREFIX'] == 'site1'
# endregion


# region REDISS
def test_rediss_dj3(django_cache_url_dj3):
    url = 'rediss://127.0.0.1:6379'
    config = django_cache_url_dj3.parse(url)

    assert config['BACKEND'] == django_cache_url_dj3.DJANGO_REDIS_BACKEND
    assert config['LOCATION'] == 'rediss://127.0.0.1:6379/0'


def test_rediss_dj4(django_cache_url_dj4):
    url = 'rediss://127.0.0.1:6379'
    config = django_cache_url_dj4.parse(url)

    assert config['BACKEND'] == django_cache_url_dj4.BUILTIN_DJANGO_BACKEND
    assert config['LOCATION'] == 'rediss://127.0.0.1:6379/0'
# endregion
