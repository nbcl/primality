from enum import Enum, auto


class RandomStrategy(Enum):
    SECRETS_CHOICE = auto()
    SECRETS_RANDOM = auto()
    RANDOM_LIB = auto()
