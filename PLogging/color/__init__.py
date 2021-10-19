from PLogging.color.color_code import _ColorModeCode, _TextModeCode, _ForegroundCode, _BackgroundCode
from PLogging.color.colored_config import _ColoredConfig

p_logging_color = _ColoredConfig()


def get_color(key):
    if key == "reset":
        return _ColorModeCode.RESET
    elif key == "bold":
        return _ColorModeCode.BOLD
    elif key == "dark":
        return _ColorModeCode.DARK
    elif key == "italic":
        return _TextModeCode.ITALIC
    elif key == "underline":
        return _TextModeCode.UNDERLINE
    elif key == "slow_blink":
        return _TextModeCode.SLOW_BLINK
    elif key == "fast_blink":
        return _TextModeCode.FAST_BLINK
    elif key == "reserves":
        return _TextModeCode.REVERSE
    elif key == "hide":
        return _TextModeCode.HIDE
    elif key == "cross":
        return _TextModeCode.CROSS
    elif key == "black":
        return _ForegroundCode.BLACK
    elif key == "red":
        return _ForegroundCode.RED
    elif key == "green":
        return _ForegroundCode.GREEN
    elif key == "yellow":
        return _ForegroundCode.YELLOW
    elif key == "blue":
        return _ForegroundCode.BLUE
    elif key == "purple":
        return _ForegroundCode.PURPLE
    elif key == "cyan":
        return _ForegroundCode.CYAN
    elif key == "white":
        return _ForegroundCode.WHITE
    elif key == "b_black":
        return _BackgroundCode.BLACK
    elif key == "b_red":
        return _BackgroundCode.RED
    elif key == "b_green":
        return _BackgroundCode.GREEN
    elif key == "b_yellow":
        return _BackgroundCode.YELLOW
    elif key == "b_blue":
        return _BackgroundCode.BLUE
    elif key == "b_purple":
        return _BackgroundCode.PURPLE
    elif key == "b_cyan":
        return _BackgroundCode.CYAN
    elif key == "b_white":
        return _BackgroundCode.WHITE
