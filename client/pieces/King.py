from client.pieces.Piece import Piece


class King(Piece):

    def __init__(self, board, color, x, y):
        if color == 'white':
            p_type = '♔'
            super().__init__(board, p_type, color, x, y)
            self.has_moved = False
        elif color == 'black':
            p_type = '♚'
            super().__init__(board, p_type, color, x, y)
            self.has_moved = False
        else:
            print('incorrect parameter for piece type')
            quit()

    # TODO: IMPLEMENT CASTLING
    def castle_check(self):
        pass

    # TODO: IMPLEMENT MOVES TO INCLUDE CASTLING AND ADD REMOVED PIECES
    def move(self, x, y):
        pass

    def find_possible_moves(self):
        new_x = self.x - 1
        if self.out_of_bounds_checking(new_x, self.y):
            pattern = [[new_x, self.y + y] for y in range(-1, 2)]
            for i in pattern:
                piece = self.board.get_tile(i[0], i[1]).get_contains()
                if piece is None:
                    self.possible_moves.append([i[0], i[1]])
                    continue

                if piece.get_color() == self.get_color():
                    continue
                else:
                    self.possible_moves.append([i[0], i[1]])

        new_x = self.x + 1
        if self.out_of_bounds_checking(new_x, self.y):
            pattern = [[new_x, self.y + y] for y in range(-1, 2)]
            for i in pattern:
                piece = self.board.get_tile(i[0], i[1]).get_contains()
                if piece is None:
                    self.possible_moves.append([i[0], i[1]])
                    continue

                if piece.get_color() == self.get_color():
                    continue
                else:
                    self.possible_moves.append([i[0], i[1]])

