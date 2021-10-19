import logging


class PLevel:
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def convert_level(level: str):
    if level.upper() == "NOTSET":
        return PLevel.NOTSET
    elif level.upper() == "DEBUG":
        return PLevel.DEBUG
    elif level.upper() == "INFO":
        return PLevel.INFO
    elif level.upper() == "WARNING":
        return PLevel.WARNING
    elif level.upper() == "ERROR":
        return PLevel.ERROR
    elif level.upper() == "CRITICAL":
        return PLevel.CRITICAL
