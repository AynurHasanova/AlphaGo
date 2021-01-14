from enum import Enum


class Player(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class BoardSize(Enum):
    beginner = 7
    medium = 13
    expert = 19


class Color:
    NORMAL = '\033[95m'
    PASSING = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    # Misc colors
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDLINE = '\033[0m'

    @classmethod
    def fprint(cls, data, fmt, *other):
        if fmt := getattr(cls, fmt):
            return f"{fmt}{data}{cls.ENDLINE}"
        return data
