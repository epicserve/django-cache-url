import sys
import mock
import pytest
import importlib


MODULE_NAME = 'django_cache_url'
DJANGO_VERSION_3 = (3, 0, 0, "final", 0)
DJANGO_VERSION_4 = (4, 0, 0, "final", 0)


@pytest.fixture()
def django_cache_url_dj3():
    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]
    with mock.patch('django.VERSION', DJANGO_VERSION_3):
        module = importlib.import_module(MODULE_NAME)
        yield module
        del sys.modules[MODULE_NAME]


@pytest.fixture()
def django_cache_url_dj4():
    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]
    with mock.patch('django.VERSION', DJANGO_VERSION_4):
        module = importlib.import_module(MODULE_NAME)
        yield module
        del sys.modules[MODULE_NAME]
