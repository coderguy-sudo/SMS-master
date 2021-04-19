import os

from django.core.exceptions import ImproperlyConfigured


def from_env(key, default=None):
    try:
        value = os.environ.get(key)
    except KeyError:
        value = default

    if value is None:
        raise ImproperlyConfigured('Set the {} environment variable'.format(key))
    return value
