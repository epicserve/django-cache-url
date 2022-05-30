import django_cache_url

redis_cache = django_cache_url.DJANGO_REDIS_CACHE_LIB_KEY


def test_basic_config():
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'


def test_advanced_config():
    extra_params = [
        'parser_class=redis.connection.HiredisParser',
        'connection_pool_class=redis.BlockingConnectionPool',
        'max_connections=50',
        'timeout=20',
    ]
    url = f'redis://:mypassword@127.0.0.1:6379/1?lib={redis_cache}&{"&".join(extra_params)}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://:mypassword@127.0.0.1:6379/1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['max_connections'] == 50
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['timeout'] == 20


def test_basic_config_with_db():
    url = f'redis://127.0.0.1:6379/1?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/1'


def test_basic_config_with_password():
    url = f'redis://:mypassword@127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://:mypassword@127.0.0.1:6379/0'


def test_basic_config_with_parser_class():
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}&parser_class=redis.connection.HiredisParser'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_basic_config_with_connection_pool_class():
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}&connection_pool_class=redis.BlockingConnectionPool'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['CONNECTION_POOL_CLASS'] == 'redis.BlockingConnectionPool'


def test_basic_config_with_connection_pool_class_kwargs():

    # both max_connections and timeout
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}&max_connections=50&timeout=20'
    config = django_cache_url.parse(url)
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['max_connections'] == 50
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['timeout'] == 20

    # just max_connections
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}&max_connections=10'
    config = django_cache_url.parse(url)
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['max_connections'] == 10
    assert 'timeout' not in config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']

    # just timeout
    url = f'redis://127.0.0.1:6379/?lib={redis_cache}&timeout=10'
    config = django_cache_url.parse(url)
    assert config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']['timeout'] == 10
    assert 'max_connections' not in config['OPTIONS']['CONNECTION_POOL_CLASS_KWARGS']


def test_rediss_config_with_db():
    url = f'rediss://127.0.0.1:6379/1?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'rediss://127.0.0.1:6379/1'


def test_rediss_config():
    url = f'rediss://127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'rediss://127.0.0.1:6379/0'


def test_rediss_config_with_password():
    url = f'rediss://:mypassword@127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'rediss://:mypassword@127.0.0.1:6379/0'


def test_hiredis_config_with_db():
    url = f'hiredis://127.0.0.1:6379/1?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/1'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_config():
    url = f'hiredis://127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'


def test_hiredis_config_with_password():
    url = f'hiredis://:mypassword@127.0.0.1:6379/?lib={redis_cache}'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == django_cache_url.DJANGO_REDIS_CACHE_BACKEND
    assert config['LOCATION'] == 'redis://:mypassword@127.0.0.1:6379/0'
    assert config['OPTIONS']['PARSER_CLASS'] == 'redis.connection.HiredisParser'
