import abc


class Player(metaclass=abc.ABCMeta):
    def __init__(self, pieces):
        self.pieces = pieces
