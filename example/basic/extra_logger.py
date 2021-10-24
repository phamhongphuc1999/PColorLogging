import logging

from src.PColorLogging import INFO, ERROR, WARNING, CRITICAL, DEBUG, add_level_name
from src.PColorLogging.Drawer.color import PColor, TextMode, ColorMode
from src.PColorLogging.Formatter.colored_formatter import ColoredFormatter
from src.PColorLogging.Logger.Adapter.extra_adapter_logger import ExtraAdapterLogger


def makeup(base_extra):
    if "att1" in base_extra and "att2" in base_extra:
        return {
            "att1": [PColor.GREEN],
            "att2": [PColor.PURPLE]
        }
    if "att1" in base_extra:
        if base_extra['att1'] == "debug1":
            return {"att1": [PColor.WHITE, PColor.B_YELLOW]}
    if "att2" in base_extra:
        if base_extra['att2'] == "info2":
            return {"att2": [PColor.B_WHITE, PColor.BLACK]}
    return None


if __name__ == "__main__":
    add_level_name(25, "CUSTOM")

    colored_formatter = ColoredFormatter(
        "[%(asctime)s] %(levelname)-10s: %(att1)s %(att2)s %(message)s %(module)s %(msecs)d %(name)s (%(pathname)s)",
        [
            {
                "config": {
                    "message": [PColor.WHITE],
                    "levelname": [PColor.WHITE]
                },
                "level": [DEBUG]
            },
            {
                "config": {
                    "message": [PColor.GREEN],
                    "levelname": [PColor.GREEN]
                },
                "level": [INFO]
            },
            {
                "config": {
                    "message": [PColor.YELLOW],
                    "levelname": [PColor.YELLOW]
                },
                "level": [WARNING]
            },
            {
                "config": {
                    "message": [PColor.RED, TextMode.UNDERLINE],
                    "levelname": [PColor.RED]
                },
                "level": [ERROR]
            },
            {
                "config": {
                    "message": [PColor.CYAN, TextMode.CROSS],
                    "levelname": [PColor.CYAN]
                },
                "level": [CRITICAL]
            },
            {
                "config": {
                    "message": [PColor.PURPLE],
                    "levelname": [PColor.PURPLE]
                },
                "level": [25]
            },
            {
                "config": {
                    "asctime": [PColor.BLUE],
                    "levelname": [ColorMode.BOLD],
                    "module": [PColor.GREEN],
                    "pathname": [TextMode.ITALIC]},
                "level": [DEBUG, INFO, WARNING, ERROR, CRITICAL, 25]
            }
        ])

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(colored_formatter)

    extra_logger = ExtraAdapterLogger("logger", {"att1": '', "att2": ''})
    extra_logger.set_maker(makeup)

    extra_logger.add_handler(console_handler)
    extra_logger.setLevel(DEBUG)

    extra_logger.debug("this is debug", extra={"att1": "debug1"})
    extra_logger.info("this is info", extra={"att2": "info2"})
    extra_logger.warning("this is warning", extra={"att1": "warning1", "att2": "warning2"})
    extra_logger.error("this is error")
    extra_logger.critical("this is critical")
    extra_logger.log(25, "this is custom")
