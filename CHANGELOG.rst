CHANGELOG
=========

v3.5.0
------

- Add support for Django 4.2, 5.0
- Add support for Python 3.12
- Drop support for Python 3.7

v3.4.4
------

- Add support for Django 4.1
- Drop support for Django 2.2, 4.0
- Add support for Python 3.11
- Drop support for Python 3.6

v3.4.2
------

- Fix a bug where providing a password for the redis backend would produce an invalid configuration on Django 4.

v3.4.0
------

- Add support for Django 4.0

v3.3.0
------

- Add support for pymemcache.

v3.1.0
------

- Bring the project back into active status, so it can be used with `environs <https://github.com/sloria/environs>`_.
- Drop support for Python less than 3.8.

v3.0.0
------

- Deprecate project in favour of `Django Environ <https://pypi.org/project/django-environ/>`_.


v2.0.0
------

- **Backwards Incompatible** Remove Python 2.6 support
- Fix urls without a port getting their port set to "None" instead (thanks to Linus Lewandowski)


v1.4.0
------

- Add django-elasticache support (thanks to Alex Couper)


v1.3.1
------

- Fix django-redis support (thanks to Manatsawin Hanmongkolchai)


v1.3.0
------

- Support for django-redis >= 4.50 (thanks to Egor Yurtaev)


v1.2.0
------

- Run tests on Python 3.5 (thanks to Anton Egorov)
- Add support for MAX_ENTRIES and CULL_FREQUENCY options (thanks to Anton Egorov)


v1.1.0
------

- Add support for uwsgi caching (thanks to Alan Justino da Silva)


v1.0.0
------

- **Backwards Incompatible** Improve Redis URL parsing, making PREFIX parsing much easier and automatically converting query args into Django Cache settings (thanks to Russell Davies)
- **Backwards Incompatible** Switch to ``django-redis``'s new import name (thanks to Michael Warkentin)
- Switch to Tox for running tests with different pythons
- Switch to pytest


v0.8.0
------

- Add support for password in redis urls (thanks to Mjumbe Wawatu Ukweli)


v0.7.0
------

- Add support for UNIX sockets in redis urls (thanks to Jannis Leidel)


v0.6.0
------

- Fix Python 3 support


v0.5.0
------

- Add multiple memcache locations


v0.4.0
------

- Add redis and hiredis support


v0.3.4
------

- Fix Python 3 compatibility import bug


v0.3.3
------

- Add Python 3 compatibility


v0.3.2
------

- Fix setting name bug


v0.3.1
------

- Remove underscore from django pylibmc scheme


v0.3.0
------

- Add python memcached support
- Add django pylibmc support


v0.2.0
------

- Add prefix support
- Split up tests
- Tidy up examples


v0.1.0
------

- Initial release
