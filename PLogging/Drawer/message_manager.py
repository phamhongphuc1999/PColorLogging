class _MessageManager:
    def __init__(self, base_message, level_list: list):
        self._base_message = base_message
        self._level_message_list = {}
        for _level in level_list:
            self._level_message_list[_level] = base_message

    def is_level(self, level):
        return level in self._level_message_list

    def get_default_message(self):
        default_message_list = []
        for _level in self._level_message_list:
            default_message_list[_level] = self._base_message
        return default_message_list

    def get_message(self, level):
        if level in self._level_message_list:
            return self._level_message_list[level]
        return None

    def set_base_message(self, base_message):
        self._base_message = base_message

    def set_message(self, level, config_message):
        self._level_message_list[level] = config_message

    def reset_message(self):
        reset_message_list = {}
        for _level in self._level_message_list:
            reset_message_list[_level] = self._base_message
        self._level_message_list = reset_message_list
