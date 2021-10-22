import logging

from PColorLog import INFO, ERROR, WARNING, CRITICAL, DEBUG
from PColorLog.Drawer.color import PColor, TextMode
from PColorLog.Formatter.colored_formatter import ColoredFormatter
from PColorLog.Logger.Adapter.extra_adapter_logger import ExtraAdapterLogger

if __name__ == "__main__":
    logging.addLevelName(25, "trava_log")

    _format = ColoredFormatter(f"[%(asctime)s] %(levelname)s:%(phuc)s %(message)s", [
        {"config": {"message": [PColor.BLUE]}, "level": [DEBUG]},
        {"config": {"message": [PColor.BLUE, TextMode.CROSS], "phuc": [PColor.B_WHITE]}, "level": [INFO]},
        {"config": {"message": [PColor.CYAN, TextMode.UNDERLINE]}, "level": [ERROR]},
        {"config": {"message": [PColor.GREEN, TextMode.SLOW_BLINK]}, "level": [WARNING]},
        {"config": {"message": [PColor.WHITE, TextMode.FAST_BLINK]}, "level": [CRITICAL]},
        {"config": {"message": [PColor.BLUE], "levelname": [PColor.B_CYAN, PColor.WHITE]}, "level": [25]}
    ])

    logger = logging.getLogger("abc")
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(_format)
    logger.addHandler(console_handler)
    logger.setLevel(logging.DEBUG)

    extra_logger = ExtraAdapterLogger(logger, {"phuc": ""})

    extra_logger.debug("this is debug", extra={"phuc": 4321})
    extra_logger.info("this is info")
    extra_logger.warning("this is warning")
    extra_logger.error("this is error")
    extra_logger.critical("this is critical")
    extra_logger.log(25, "abcbcbcbchfjfjf")
