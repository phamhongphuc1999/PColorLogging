import logging

from PLogging import is_level
from PLogging.Drawer import Drawer


class ColoredFormatter(logging.Formatter):
    def __init__(self, ftm, config=None, use_color=True):
        logging.Formatter.__init__(self, ftm, datefmt='%m-%d %H:%M:%S')
        self.drawer = Drawer(ftm, config)
        self.use_color = use_color

    def format(self, record):
        level_name = record.levelname.lower()
        if self.use_color and is_level(level_name):
            self._style._fmt = self.drawer.get_message(level_name)
        return logging.Formatter.format(self, record)
