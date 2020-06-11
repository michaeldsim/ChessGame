from client.Piece import Piece


class Rook(Piece):
    def __init__(self, board, color, x, y):
        if color == 'black':
            p_type = '♜'
            super().__init__(board, p_type, color, x, y)
        elif color == 'white':
            p_type = '♖'
            super().__init__(board, p_type, color, x, y)
        else:
            print('incorrect parameter for color')
            quit()

    # iterate over the board horizontally and vertically until either the end is found or another piece
    def find_possible_moves(self):
        pass
