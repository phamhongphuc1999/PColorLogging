import logging

NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


def get_level_name(key: int):
    if key == NOTSET:
        return "notset"
    elif key == DEBUG:
        return "debug"
    elif key == INFO:
        return "info"
    elif key == WARNING:
        return "warning"
    elif key == ERROR:
        return "error"
    elif key == CRITICAL:
        return "critical"
    else:
        return None
