from client.pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, board, color, x, y):
        if color == 'white':
            p_type = '♘'
            super().__init__(board, p_type, color, x, y)
        elif color == 'black':
            p_type = '♞'
            super().__init__(board, p_type, color, x, y)
        else:
            print('incorrect parameter for piece type')
            quit()

    def find_possible_moves(self):
        # right
        temp = [[self.x + n, self.y + 2] for n in range(-1, 2, 2)]
        # left
        temp += [[self.x + n, self.y - 2] for n in range(-1, 2, 2)]
        # up
        temp += [[self.x - 2, self.y + n] for n in range(-1, 2, 2)]
        # down
        temp += [[self.x + 2, self.y + n] for n in range(-1, 2, 2)]

        for i in temp:
            if self.out_of_bounds_checking(i[0], i[1]):
                if self.board.get_tile(i[0], i[1]).get_contains() is None:
                    self.possible_moves.append(i)
                elif self.board.get_tile(i[0], i[1]).get_contains().get_color() == self.color:
                    continue
                else:
                    self.possible_moves.append(i)
            else:
                continue

