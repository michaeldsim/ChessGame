from client.Piece import Piece


class Knight(Piece):
    def __init__(self, board, color, x, y):
        super().__init__(self, board, color, x, y)

    def find_possible_moves(self):
        pass
