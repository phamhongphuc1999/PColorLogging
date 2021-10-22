import logging

from PLogging import INFO, ERROR, WARNING, CRITICAL, DEBUG
from PLogging.Drawer.color import PColor, TextMode
from PLogging.Formatter.colored_formatter import ColoredFormatter

if __name__ == "__main__":
    logging.addLevelName(25, "trava_log")

    _format = ColoredFormatter(f"[%(asctime)s] %(levelname)s: %(message)s (%(pathname)s:%(lineno)d)", [
        {"config": {"message": [PColor.BLUE]}, "level": [DEBUG]},
        {"config": {"message": [PColor.BLUE, TextMode.CROSS]}, "level": [INFO]},
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

    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")
    logger.log(25, "abcbcbcbchfjfjf")
