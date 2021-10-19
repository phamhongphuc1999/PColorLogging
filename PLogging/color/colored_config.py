from PLogging import PLevel
from PLogging.color.color_code import _ForegroundCode, _BaseColorCode


class _ColoredConfig:
    def __init__(self):
        self._debug = _ForegroundCode.WHITE
        self._info = _ForegroundCode.GREEN
        self._warning = _ForegroundCode.YELLOW
        self._error = _ForegroundCode.RED
        self._critical = _ForegroundCode.PURPLE

        self._color = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def is_level(self, level: str):
        if level.upper() in self._color:
            return True
        return False

    def set_level_color(self, level: PLevel, _color: _BaseColorCode):
        if level == PLevel.DEBUG:
            self._debug = _color
        elif level == PLevel.INFO:
            self._info = _color
        elif level == PLevel.WARNING:
            self._warning = _color
        elif level == PLevel.ERROR:
            self._error = _color
        elif level == PLevel.CRITICAL:
            self._critical = _color

    def get_level_color(self, level: PLevel):
        if level == PLevel.DEBUG:
            return self._debug
        elif level == PLevel.INFO:
            return self._info
        elif level == PLevel.WARNING:
            return self._warning
        elif level == PLevel.ERROR:
            return self._error
        elif level == PLevel.CRITICAL:
            return self._critical
