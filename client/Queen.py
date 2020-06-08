from client.Piece import Piece


class Queen(Piece):
    def __init__(self, board , color, x, y):
        if color == 'white':
            ptype = '♕'
        else:
            ptype = '♛'
        super().__init__(board, ptype, color, x, y)

    def find_possible_moves(self):
        pass

    def can_eat(self):
        pass


