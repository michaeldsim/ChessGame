from client.Piece import Piece


class Knight(Piece):
    def __init__(self):
        super().__init__(self, color, x, y)

    def find_possible_moves(self):
        pass
