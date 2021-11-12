import logging
import os

from PColorLogging import DEBUG
from PColorLogging.Formatter.colored_formatter import ColoredFormatter
from PColorLogging.Logger.Adapter.extra_adapter_logger import ExtraAdapterLogger

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))

    colored_formatter = ColoredFormatter("[%(asctime)s] %(levelname)s: %(message)s", file_config="config.json")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(colored_formatter)

    extra_logger = ExtraAdapterLogger("logger")

    extra_logger.add_handler(console_handler)
    extra_logger.setLevel(DEBUG)

    extra_logger.debug("this is debug")
    extra_logger.info("this is info")
    extra_logger.warning("this is warning")
    extra_logger.error("this is error")
    extra_logger.critical("this is critical")
