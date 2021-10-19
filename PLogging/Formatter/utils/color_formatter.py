base_char = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 'f']


class ColorFormatter:
    def __init__(self, message: str, config):
        self.message = message
        self.config = config

    def _detect_format_attribute(self, record_attribute: str):
        index = self.message.find(record_attribute)
        if index == -1:
            return record_attribute
        base_index = index + len(record_attribute)
        _len = len(self.message)
        while base_index < _len:
            if self.message[base_index] in base_char:
                record_attribute += self.message[base_index]
                base_index += 1
            else:
                break
        return record_attribute
