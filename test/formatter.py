import logging

from PLogging.Drawer.color import PColor
from PLogging.Formatter.colored_formatter import ColoredFormatter

if __name__ == "__main__":

    _format = ColoredFormatter(f"[%(asctime)s] %(levelname)s: %(message)s (%(pathname)s:%(lineno)d)", [
        {"config": {"message": PColor.BLUE}, "level": ['debug', 'info']},
        {"config": {"message": PColor.CYAN}, "level": ['error']},
        {"config": {"message": PColor.GREEN}, "level": ['warning']}
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
