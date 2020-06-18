import abc

# TODO: ALL PIECES/SUBCLASSES NEED TO BE FINISHED


class Piece(metaclass=abc.ABCMeta):
    def __init__(self, board, piece_type, color, x, y):
        self.board = board
        self.piece_type = piece_type
        self.color = color
        self.x = x
        self.y = y
        self.possible_moves = []

    def get_color(self):
        return self.color

    def move(self, x, y):
        # move to new tile
        elem = [x, y]
        if elem in self.possible_moves:
            piece = self.board.get_tile(x, y).get_contains()
            if piece is None:
                pass
            else:
                self.board.removed_pieces.append(piece)

            print('element found, move possible')
            self.board.get_tile(x, y).set_contains(self)
            # remove instance from old tile
            self.board.get_tile(self.x, self.y).set_contains(None)
            self.x = x
            self.y = y
            self.possible_moves = []
            self.find_possible_moves()

            if self.color == 'white':
                king = self.board.get_black_king().get_coordinates()
                if king in self.possible_moves:
                    king.is_checked = True
            else:
                king = self.board.get_white_king().get_coordinates()
                if king in self.possible_moves:
                    king.is_checked = True

        else:
            print('element not found, move not possible')

    # always works even if not in possible_moves
    def debug_move(self, x, y):
        # move to new tile
        if self.out_of_bounds_checking(x, y):
            self.board.get_tile(x, y).set_contains(self)
            # remove instance from old tile
            self.board.get_tile(self.x, self.y).set_contains(None)
            self.x = x
            self.y = y
            self.possible_moves = []
            self.find_possible_moves()
        else:
            print('cannot move out of bounds issue')

    def out_of_bounds_checking_one(self, n):
        """
        checks if the coordinate is out of bounds
        if true: it is in range
        if false: it is not
        """
        if n > 7 or n < 0:
            print("Out of bounds error!\n({}) from {}".format(n, self))
            return False
        else:
            return True

    def out_of_bounds_checking(self, x, y):
        """
        checks if the coordinate is out of bounds
        if true: it is in range
        if false: it is not
        """
        if x > 7 or x < 0 or y > 7 or y < 0:
            print("Out of bounds error!\nCoordinates: ({},{}) from {}".format(x, y, self))
            return False
        else:
            return True

    def show_moves_on_board(self):
        print('    0   1   2   3   4   5   6   7')
        for i in range(self.board.ROWS):
            print('{} ['.format(i), end='')
            for j in range(self.board.COLUMNS):
                if j == 7:
                    if [i, j] in self.possible_moves:
                        print('███', end='')
                    elif [i, j] == [self.x, self.y]:
                        print(' O ', end='')
                    else:
                        print('   ', end='')
                else:
                    if [i, j] in self.possible_moves:
                        print('███,', end='')
                    elif [i, j] == [self.x, self.y]:
                        print(' O ,', end='')
                    else:
                        print('   ,', end='')
            print(']')

    def __str__(self):
        return self.piece_type

    @abc.abstractmethod
    def find_possible_moves(self):
        pass
