================
django-cache-url
================

.. image:: https://img.shields.io/pypi/v/django-cache-url.svg
    :alt: PyPI version
    :target: https://pypi.org/project/django-cache-url/

.. image:: https://img.shields.io/pypi/pyversions/django-cache-url.svg
   :alt: Supported Python versions
   :target: https://pypi.org/project/django-cache-url/

.. image:: https://github.com/epicserve/django-cache-url/workflows/CI/badge.svg?branch=master
   :target: https://github.com/epicserve/django-cache-url/actions
   :alt: Tests

⚠️ Important Notice for Redis Users
------------------------------------

**If you only need Redis cache support**, Django 4.2+ now includes native Redis support via
``django.core.cache.backends.redis.RedisCache``. For new projects using only Redis, we
recommend using Django's built-in support instead of this library.

**This project remains useful for:**

- Supporting non-Redis cache backends (memcached, file, database, etc.)
- Using URL-based cache configuration for any backend (12-factor app pattern)
- Maintaining legacy projects already using django-cache-url
- Projects that need multiple cache backend support with unified configuration

**For Redis-only new projects**: See `Django's cache documentation <https://docs.djangoproject.com/en/stable/topics/cache/#redis>`_
for native Redis setup.

----

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.

This was built with inspiration from rdegges'
`django-heroku-memcacheify <https://github.com/rdegges/django-heroku-memcacheify>`_
as a way to use CACHE_URL in apps that aren't necessarily hosted on Heroku.

The internals borrow heavily from kennethreitz's
`dj-database-url <https://github.com/kennethreitz/dj-database-url>`_.


Usage
-----
Configure your cache in ``settings.py`` from ``CACHE_URL``::

    import django_cache_url
    CACHES = {'default': django_cache_url.config()}

Defaults to local memory cache if ``CACHE_URL`` isn't set.

Parse an arbitrary Cache URL::

    CACHES = {'default': django_cache_url.parse('memcache://...')}

Migrating to Django's Native Redis Support
-------------------------------------------

If you're using this library only for Redis and want to migrate to Django's built-in Redis backend (Django 4.2+),
here's how to transition:

**Before** (using django-cache-url)::

    import django_cache_url
    import os

    CACHES = {
        'default': django_cache_url.config(default='redis://localhost:6379/1')
    }

**After** (using Django's native Redis backend)::

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.redis.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
        }
    }

For more details, see the `Django Redis cache documentation <https://docs.djangoproject.com/en/stable/topics/cache/#redis>`_.

Supported Caches
----------------
Support currently exists for:

* locmem (default): ``'locmem://[NAME]'``
* db: ``'db://TABLE_NAME'``
* dummy: ``'dummy://'``
* file: ``'file:///PATH/TO/FILE'``
* memcached: ``'memcached://HOST:PORT'`` [#memcache]_
* pymemcached: ``'pymemcached://HOST:PORT'`` For use with the `python-memcached`_ library. Useful if you're using Ubuntu <= 10.04.
* pymemcache: ``'pymemcache://HOST:PORT'`` For use with the `pymemcache`_ library.
* djangopylibmc: ``'djangopylibmc://HOST:PORT'`` For use with SASL based setups such as Heroku.
* redis: ``'redis://[USER:PASSWORD@]HOST:PORT[/DB]'`` or ``'redis:///PATH/TO/SOCKET[/DB]'`` For use with `django-redis`_. To use `django-redis-cache`_ just add ``?lib=redis-cache`` to the URL.
* rediss: ``'rediss://[USER:PASSWORD@]HOST:PORT[/DB]'`` For use with `django-redis`_.
* hiredis: ``'hiredis://[USER:PASSWORD@]HOST:PORT[/DB]'`` or ``'hiredis:///PATH/TO/SOCKET[/DB]'`` For use with django-redis library using HiredisParser.
* uwsgicache: ``'uwsgicache://[CACHENAME]'`` For use with `django-uwsgi-cache`_. Fallbacks to ``locmem`` if not running on uWSGI server.

All cache urls support optional cache arguments by using a query string, e.g.: ``'memcached://HOST:PORT?key_prefix=site1'``. See the Django `cache arguments documentation`_.

.. [#memcache] To specify multiple instances, separate the ``HOST:PORT`` pair
               by commas, e.g: ``'memcached://HOST1:PORT1,HOST2:PORT2'``

.. _django-redis: https://github.com/niwibe/django-redis
.. _django-redis-cache: https://github.com/sebleier/django-redis-cache
.. _python-memcached: https://github.com/linsomniac/python-memcached
.. _pymemcache: https://github.com/pinterest/pymemcache
.. _cache arguments documentation: https://docs.djangoproject.com/en/dev/topics/cache/#cache-arguments
.. _django-uwsgi-cache: https://github.com/ionelmc/django-uwsgi-cache

Installation
------------
Installation is simple too::

    $ pip install django-cache-url

Tests
-----

To run the tests install tox::

    pip install tox

Then run them with::

    make test

