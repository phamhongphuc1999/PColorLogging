import logging

from PLogging.Formatter.colored_formatter import ColoredFormatter
from PLogging.resources.color_config import BOLD, RESET, FONT_CYAN

if __name__ == "__main__":
    logger = logging.getLogger("abc")

    console_handler = logging.StreamHandler()
    colored_formatter = ColoredFormatter(f"{BOLD}[%(asctime)s]{RESET} %(levelname)s: %(message)s {FONT_CYAN}(%(pathname)s:%(lineno)d){RESET}")
    console_handler.setFormatter(colored_formatter)
    logger.addHandler(console_handler)

    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")
