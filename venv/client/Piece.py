import abc


class Piece(metaclass=abc.ABCMeta):
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

    def get_color(self):
        return self.color

    @abc.abstractmethod
    def possible_moves(self):
        pass
