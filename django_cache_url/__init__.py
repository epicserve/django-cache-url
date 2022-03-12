# -*- coding: utf-8 -*-
import os
import re

from django import VERSION

try:
    import urllib.parse as urlparse
except ImportError:  # python 2
    import urlparse


# Register cache schemes in URLs.
urlparse.uses_netloc.append('db')
urlparse.uses_netloc.append('dummy')
urlparse.uses_netloc.append('file')
urlparse.uses_netloc.append('locmem')
urlparse.uses_netloc.append('uwsgicache')
urlparse.uses_netloc.append('memcached')
urlparse.uses_netloc.append('elasticache')
urlparse.uses_netloc.append('djangopylibmc')
urlparse.uses_netloc.append('pymemcached')
urlparse.uses_netloc.append('pymemcache')
urlparse.uses_netloc.append('redis')
urlparse.uses_netloc.append('hiredis')

DEFAULT_ENV = 'CACHE_URL'
DJANGO_REDIS_CACHE = 'redis-cache'

# TODO Remove as soon as Django 3.2 goes EOL
redis_backend = 'django_redis.cache.RedisCache' if VERSION[0] < 4 else 'django.core.cache.backends.redis.RedisCache'

BACKENDS = {
    'db': 'django.core.cache.backends.db.DatabaseCache',
    'dummy': 'django.core.cache.backends.dummy.DummyCache',
    'elasticache': 'django_elasticache.memcached.ElastiCache',
    'file': 'django.core.cache.backends.filebased.FileBasedCache',
    'locmem': 'django.core.cache.backends.locmem.LocMemCache',
    'uwsgicache': 'uwsgicache.UWSGICache',
    'memcached': 'django.core.cache.backends.memcached.PyLibMCCache',
    'djangopylibmc': 'django_pylibmc.memcached.PyLibMCCache',
    'pymemcached': 'django.core.cache.backends.memcached.MemcachedCache',
    'pymemcache': 'django.core.cache.backends.memcached.PyMemcacheCache',
    DJANGO_REDIS_CACHE: 'redis_cache.RedisCache',
    'redis': redis_backend,
    'rediss': redis_backend,
    'hiredis': redis_backend,
}


# django-redis-cache
def config(env=DEFAULT_ENV, default='locmem://'):
    """Returns configured CACHES dictionary from CACHE_URL"""
    config = {}

    s = os.environ.get(env, default)

    if s:
        config = parse(s)

    return config


def parse(url):
    """Parses a cache URL."""
    config = {}

    url = urlparse.urlparse(url)
    path, query = url.path, url.query

    cache_args = dict([(key.upper(), ';'.join(val)) for key, val in urlparse.parse_qs(query).items()])

    # Update with environment configuration.
    backend = BACKENDS.get(url.scheme)
    if not backend:
        raise Exception(f'Unknown backend: "{url.scheme}"')

    lib = cache_args.get('LIB')
    if 'redis' in url.scheme and lib in BACKENDS:
        backend = BACKENDS[lib]

    config['BACKEND'] = backend

    redis_options = {}
    if url.scheme == 'hiredis':
        redis_options['PARSER_CLASS'] = 'redis.connection.HiredisParser'

    # File based
    if not url.netloc:
        if url.scheme in ('memcached', 'pymemcached', 'pymemcache', 'djangopylibmc'):
            config['LOCATION'] = 'unix:' + path

        elif url.scheme in ('redis', 'hiredis'):
            match = re.match(r'.+?(?P<db>\d+)', path)
            if match:
                db = match.group('db')
                path = path[:path.rfind('/')]
            else:
                db = '0'
            config['LOCATION'] = 'unix:%s?db=%s' % (path, db)
        else:
            config['LOCATION'] = path
    # URL based
    else:
        # Handle multiple hosts
        config['LOCATION'] = ';'.join(url.netloc.split(','))

        if url.scheme in ('redis', 'rediss', 'hiredis'):
            if url.password and lib != DJANGO_REDIS_CACHE:
                redis_options['PASSWORD'] = url.password
            # Specifying the database is optional, use db 0 if not specified.
            db = path[1:] or '0'
            port = url.port if url.port else 6379
            scheme = 'rediss' if url.scheme == 'rediss' else 'redis'
            config['LOCATION'] = f'{scheme}://{url.hostname}:{port}/{db}'
            if lib == DJANGO_REDIS_CACHE and url.password:
                config['LOCATION'] = f'{scheme}://:{url.password}@{url.hostname}:{port}/{db}'

            if lib == DJANGO_REDIS_CACHE:
                if 'PARSER_CLASS' in cache_args:
                    redis_options['PARSER_CLASS'] = cache_args['PARSER_CLASS']

                if 'CONNECTION_POOL_CLASS' in cache_args:
                    redis_options['CONNECTION_POOL_CLASS'] = cache_args['CONNECTION_POOL_CLASS']

                if 'MAX_CONNECTIONS' in cache_args or 'TIMEOUT' in cache_args:
                    redis_options['CONNECTION_POOL_CLASS_KWARGS'] = {}

                    if 'MAX_CONNECTIONS' in cache_args:
                        redis_options['CONNECTION_POOL_CLASS_KWARGS']['max_connections'] = int(
                            cache_args['MAX_CONNECTIONS'])

                    if 'TIMEOUT' in cache_args:
                        redis_options['CONNECTION_POOL_CLASS_KWARGS']['timeout'] = int(cache_args['TIMEOUT'])

    if redis_options:
        config.setdefault('OPTIONS', {}).update(redis_options)

    if url.scheme == 'uwsgicache':
        config['LOCATION'] = config.get('LOCATION', 'default') or 'default'

    # Pop special options from cache_args
    # https://docs.djangoproject.com/en/1.10/topics/cache/#cache-arguments
    options = {}
    for key in ['MAX_ENTRIES', 'CULL_FREQUENCY']:
        val = cache_args.pop(key, None)
        if val is not None:
            options[key] = int(val)
    if options:
        config.setdefault('OPTIONS', {}).update(options)

    config.update(cache_args)

    return config
