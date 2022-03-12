# -*- coding: utf-8 -*-
"""
django-cache-url
~~~~~~~~~~~~~~~~

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``CACHE_URL`` environment variable to configure your Django application.


Usage
-----

Configure your cache in ``settings.py``::

    CACHES={'default': django_cache_url.config()}

Nice and simple.
"""
from setuptools import setup


setup(
    name='django-cache-url',
    version='3.4.0',
    url='https://github.com/epicserve/django-cache-url',
    license='MIT',
    author="Brent O'Connor",
    author_email='epicserve@gmail.com',
    description='Use Cache URLs in your Django application.',
    long_description=__doc__,
    packages=('django_cache_url',),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
