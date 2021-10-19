_p_record_attribute = {
    "asctime": "asctime",
    "created": "created",
    "filename": "filename",
    "funcName": "funcName",
    "levelname": "levelname",
    "levelno": "levelno",
    "lineno": "lineno",
    "message": "message",
    "module": "module",
    "name": "name",
    "pathname": "pathname",
    "process": "process",
    "processName": "processName",
    "relativeCreated": "relativeCreated",
    "thread": "thread",
    "threadName": "threadName",
}


def get_record_attribute(key=None):
    if key is None:
        return _p_record_attribute
    elif key in _p_record_attribute:
        return _p_record_attribute[key]
    else:
        return None


def is_record_attribute(key):
    return key in _p_record_attribute


def add_record_attribute(key, value):
    _p_record_attribute[key] = value


def remove_record_attribute(key):
    if key in _p_record_attribute:
        del _p_record_attribute[key]
