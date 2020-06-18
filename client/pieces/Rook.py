from client.pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, board, color, x, y):
        if color == 'black':
            p_type = '♜'
            super().__init__(board, p_type, color, x, y)
            self.has_not_moved = True
        elif color == 'white':
            p_type = '♖'
            super().__init__(board, p_type, color, x, y)
            self.has_not_moved = True
        else:
            print('incorrect parameter for color')
            quit()

    # iterate over the board horizontally and vertically until either the end is found or another piece
    def find_possible_moves(self):
        # iterate horizontally starting from piece and goes right
        for i in range(self.y + 1, 8):
            piece = self.board.get_tile(self.x, i).get_contains()
            if not self.out_of_bounds_checking_one(i):
                break
            if piece is None:
                self.possible_moves.append([self.x, i])
            elif piece.get_color() != self.color:
                self.possible_moves.append([self.x, i])
                break
            else:
                break

        for i in range(self.x + 1, 8):
            piece = self.board.get_tile(i, self.y).get_contains()
            if not self.out_of_bounds_checking_one(i):
                break
            if piece is None:
                self.possible_moves.append([i, self.y])
            elif piece.get_color() != self.color:
                self.possible_moves.append([i, self.y])
                break
            else:
                break

        for i in range(self.y - 1, -8, -1):
            piece = self.board.get_tile(self.x, i).get_contains()
            if not self.out_of_bounds_checking_one(i):
                break
            elif piece is None:
                self.possible_moves.append([self.x, i])
            elif piece.get_color() != self.color:
                self.possible_moves.append([self.x, i])
                break
            else:
                break

        for i in range(self.x - 1, -8, -1):
            piece = self.board.get_tile(i, self.y).get_contains()
            if not self.out_of_bounds_checking_one(i):
                break
            if piece is None:
                self.possible_moves.append([i, self.y])
            elif piece.get_color() != self.color:
                self.possible_moves.append([i, self.y])
                break
            else:
                break