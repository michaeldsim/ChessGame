from client.Piece import Piece


class Rook(Piece):
    def __init__(self, board, color, x, y):
        super.__init__(board, color, x, y)
        self.piece_type = 'Rook'

    # iterate over the board horizontally and vertically until either the end is found or another piece
    def find_possible_moves(self):
        pass

    def can_eat(self):
        pass

