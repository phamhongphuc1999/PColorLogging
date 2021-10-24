import logging

from src.PColorLogging import INFO, ERROR, WARNING, CRITICAL, DEBUG, add_level_name
from src.PColorLogging.Drawer.color import PColor, TextMode
from src.PColorLogging.Formatter.colored_formatter import ColoredFormatter
from src.PColorLogging.Logger.Adapter.extra_adapter_logger import ExtraAdapterLogger


def makeup(base_extra):
    if "att1" in base_extra:
        if base_extra['att1'] == "att1-debug":
            return {"att1": [PColor.GREEN, PColor.B_YELLOW]}
    if "att2" in base_extra:
        if base_extra['att2'] == "att2-info":
            return {"att2": [PColor.B_CYAN, PColor.YELLOW]}
    return None


if __name__ == "__main__":
    add_level_name(25, "custom")

    colored_formatter = ColoredFormatter("[%(asctime)s] %(levelname)s: %(att1)s %(att2)s %(message)s", [
        {"config": {"message": [PColor.WHITE]}, "level": [DEBUG]},
        {"config": {"message": [PColor.GREEN]}, "level": [INFO]},
        {"config": {"message": [PColor.YELLOW]}, "level": [WARNING]},
        {"config": {"message": [PColor.RED, TextMode.UNDERLINE]}, "level": [ERROR]},
        {"config": {"message": [PColor.CYAN, TextMode.CROSS]}, "level": [CRITICAL]},
        {"config": {"message": [PColor.PURPLE]}, "level": [25]},
        {"config": {"asctime": [PColor.BLUE, PColor.B_WHITE]}, "level":
            [DEBUG, INFO, WARNING, ERROR, CRITICAL, 25]}
    ])

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(colored_formatter)

    extra_logger = ExtraAdapterLogger("logger", {"att1": "", "att2": ""})
    extra_logger.set_maker(makeup)

    extra_logger.add_handler(console_handler)
    extra_logger.setLevel(DEBUG)

    extra_logger.debug("this is debug", extra={"att1": "att1-debug"})
    extra_logger.info("this is info", extra={"att2": "att2-info"})
    extra_logger.warning("this is warning", extra={"att1": "att1", "att2": "att2"})
    extra_logger.error("this is error")
    extra_logger.critical("this is critical")
    extra_logger.log(25, "this is custom")
