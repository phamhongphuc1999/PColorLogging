import logging

from PLogging.Formatter.colored_formatter import ColoredFormatter

if __name__ == "__main__":
    logger = logging.getLogger("abc")

    console_handler = logging.StreamHandler()
    colored_formatter = ColoredFormatter(f"[%(asctime)s] %(levelname)s: %(message)s (%(pathname)s:%(lineno)d)")
    console_handler.setFormatter(colored_formatter)
    logger.addHandler(console_handler)

    logger.setLevel(logging.DEBUG)

    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")
