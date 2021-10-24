import logging

from src.PColorLogging import INFO, ERROR, WARNING, CRITICAL, DEBUG, add_level_name
from src.PColorLogging.Drawer.color import PColor, TextMode
from src.PColorLogging.Formatter.colored_formatter import ColoredFormatter
from src.PColorLogging.Logger.Adapter.extra_adapter_logger import ExtraAdapterLogger


def makeup(base_extra):
    if "phuc" in base_extra:
        if base_extra['phuc'] == 4321:
            return {"phuc": [PColor.GREEN]}
        elif base_extra['phuc'] == "123333":
            return {"phuc": [PColor.B_CYAN, PColor.YELLOW]}
    return None


if __name__ == "__main__":
    add_level_name(25, "trava_log")

    _format = ColoredFormatter(f"[%(asctime)s] %(levelname)s:%(phuc)s %(phuc1)s %(message)s", [
        {"config": {"message": [PColor.BLUE]}, "level": [DEBUG]},
        {"config": {"message": [PColor.BLUE, TextMode.CROSS], "phuc": [PColor.B_WHITE]}, "level": [INFO]},
        {"config": {"message": [PColor.CYAN, TextMode.UNDERLINE]}, "level": [ERROR]},
        {"config": {"message": [PColor.GREEN, TextMode.SLOW_BLINK]}, "level": [WARNING]},
        {"config": {"message": [PColor.WHITE, TextMode.FAST_BLINK]}, "level": [CRITICAL]},
        {"config": {"message": [PColor.BLUE], "levelname": [PColor.B_CYAN, PColor.WHITE]}, "level": [25]},
        {"config": {"asctime": [PColor.CYAN]}, "level": [DEBUG, INFO, WARNING, ERROR]}
    ])

    extra_logger = ExtraAdapterLogger("logger", {"phuc": "", "phuc1": ""})
    extra_logger.set_maker(makeup)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(_format)
    extra_logger.add_handler(console_handler)
    extra_logger.setLevel(logging.DEBUG)

    extra_logger.debug("this is debug", extra={"phuc": 4321, "phuc1": 44444})
    extra_logger.info("this is info", extra={"phuc": "123333"})
    extra_logger.warning("this is warning", extra={"phuc": "33333"})
    extra_logger.error("this is error")
    extra_logger.critical("this is critical")
    extra_logger.log(25, "this is custom log")
