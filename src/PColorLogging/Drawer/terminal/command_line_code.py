class _CursorNavigationCode:
    @staticmethod
    def up(i: int):
        return f"\u001b[{i}A"

    @staticmethod
    def down(i):
        return f"\u001b[{i}B"

    @staticmethod
    def right(i):
        return f"\u001b[{i}C"

    @staticmethod
    def left(i):
        return f"\u001b[{i}D"


class _PositionCode:
    @staticmethod
    def next_line(i):
        return f"\u001b[{i}E"

    @staticmethod
    def prev_line(i):
        return f"\u001b[{i}F"

    @staticmethod
    def set_column(i):
        return f"\u001b[{i}G"

    @staticmethod
    def set_position(i, j):
        return f"\u001b[{i};{j}H"
