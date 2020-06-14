from client.pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, board, color, x, y):
        if color == 'white':
            p_type = '♗'
            super().__init__(board, p_type, color, x, y)
        elif color == 'black':
            p_type = '♝'
            super().__init__(board, p_type, color, x, y)
        else:
            print('incorrect parameter for piece type')
            quit()

    def find_possible_moves(self):
        for i in range(1, 8):
            new_x = self.x + i
            new_y = self.y + i
            if self.out_of_bounds_checking(new_x, new_y):
                piece = self.board.get_tile(new_x, new_y).get_contains()
                if piece is None:
                    self.possible_moves.append([new_x, new_y])
                elif piece.get_color() != self.color:
                    self.possible_moves.append([new_x, new_y])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            new_x = self.x - i
            new_y = self.y + i
            if self.out_of_bounds_checking(new_x, new_y):
                piece = self.board.get_tile(new_x, new_y).get_contains()
                if piece is None:
                    self.possible_moves.append([new_x, new_y])
                elif piece.get_color() != self.color:
                    self.possible_moves.append([new_x, new_y])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            new_x = self.x - i
            new_y = self.y - i
            if self.out_of_bounds_checking(new_x, new_y):
                piece = self.board.get_tile(new_x, new_y).get_contains()
                if piece is None:
                    self.possible_moves.append([new_x, new_y])
                elif piece.get_color() != self.color:
                    self.possible_moves.append([new_x, new_y])
                    break
                else:
                    break
            else:
                break

        for i in range(1, 8):
            new_x = self.x + i
            new_y = self.y - i
            if self.out_of_bounds_checking(new_x, new_y):
                piece = self.board.get_tile(new_x, new_y).get_contains()
                if piece is None:
                    self.possible_moves.append([new_x, new_y])
                elif piece.get_color() != self.color:
                    self.possible_moves.append([new_x, new_y])
                    break
                else:
                    break
            else:
                break
