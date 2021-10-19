import logging

from PLogging import convert_level
from PLogging.color import get_color, p_logging_color


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
        reset = get_color("reset")
        bold = get_color("bold")
        if self.use_color and p_logging_color.is_level(level_name):
            p_level = convert_level(level_name)
            print("p_level", level_name, p_level)
            level_color = p_logging_color.get_level_color(p_level)
            self._style._fmt = self._style._fmt.replace("%(message)s", f"{level_color}%(message)s{reset}").\
                replace("%(levelname)s", f"{level_color}{bold}%(levelname)s{reset}{reset}")
        return logging.Formatter.format(self, record)
