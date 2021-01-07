from enum import Enum


class Player(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class BoardSize(Enum):
    beginner = 7
    medium = 13
    expert = 19
