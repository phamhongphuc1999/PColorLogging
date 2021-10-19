import logging

NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

_p_level = {
    "notset": "notset",
    "debug": "debug",
    "info": "info",
    "warning": "warning",
    "error": "error",
    "critical": "critical"
}


def get_level(key=None):
    if key is None:
        return _p_level
    elif key in _p_level:
        return _p_level[key]
    else:
        return None


def is_level(key):
    return key in _p_level


def add_level(key, value):
    _p_level[key] = value


def remove_level(key):
    if key in _p_level:
        del _p_level[key]
