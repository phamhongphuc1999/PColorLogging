import logging

from PLogging.Formatter import COLORS
from PLogging.resources.color_config import RESET


class ColoredFormatter(logging.Formatter):
    """
    Wrap Formatter, add color BASH PS1
    """

    def __init__(self, ftm, use_color=True):
        """
        Set use_color resources will use

        :param use_color: The use_config option, if True trava_logger will log with color, else will log without color
        """
        logging.Formatter.__init__(self, ftm, datefmt='%m-%d %H:%M:%S')
        self.use_color = use_color

    def format(self, record):
        level_name = record.levelname
        if self.use_color and level_name in COLORS:
            level_name_color = COLORS[level_name] + f"[{level_name}]" + RESET
            record.levelname = level_name_color
        return logging.Formatter.format(self, record)
