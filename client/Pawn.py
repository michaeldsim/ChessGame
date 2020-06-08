from client.Piece import *


class Pawn(Piece):
    def __init__(self, board, color, x, y):
        if color == 'black':
            ptype = '♟'
        else:
            ptype = '♙'
        super().__init__(board, ptype, color, x, y)
        # first move has the option to move either one or two spaces
        # this will keep track of that
        self.first_move = True

    def move(self, x, y):
        """
        :arg
        x is new x coordinate to move to
        y is new y coordinate to move to

        this will check if the given coordinates is possible given in the list of possible_moves and
        move to the provided spot if found in that list
        """
        elem = [x, y]
        if elem in self.possible_moves:
            print('element found, move possible')
            if self.first_move:
                self.first_move = False
            self.board.get_tile(x, y).set_contains(self)
            # remove instance from old tile
            self.board.get_tile(self.x, self.y).set_contains(None)
            self.x = x
            self.y = y
            self.possible_moves = []
            self.find_possible_moves()
        else:
            print('element not found, move not possible')

    def can_eat(self):
        if color == 'white':
            eat_pattern = [[self.x - 1 , self.y + y] for y in range(-1, 2, 2)]
            for i in eat_pattern:
                piece = self.board.get_tile(i[0], i[1]).get_contains()
                if piece is None:
                    continue

                if piece.get_color() == self.get_color():
                    continue
                else:
                    self.possible_moves.append([i[0], i[1]])
        else:
            eat_pattern = [[self.x + 1, self.y + y] for y in range(-1, 2, 2)]
            for i in eat_pattern:
                piece = self.board.get_tile(i[0], i[1]).get_contains()
                if piece is None:
                    continue

                if piece.get_color() == self.get_color():
                    continue
                else:
                    self.possible_moves.append([i[0], i[1]])

    def promote(self, new_piece):
        """
        :arg
        new_piece is the name of the new piece the pawn is wanting to promote to

        this function will replace the pawn from the current tile with a new object in the same position
        """
        if new_piece == 'queen':
            queen = Queen(self.board, self.color, self.x, self.y)
            self.board.get_tile(self.x, self.y).set_contains(queen)
        elif new_piece == 'rook':
            rook = Rook(self.board, self.color, self.x, self.y)
            self.board.get_tile(self.x, self.y).set_contains(rook)
        elif new_piece == 'bishop':
            bishop = Bishop(self.board, self.color, self.x, self.y)
            self.board.get_tile(self.x, self.y).set_contains(bishop)
        elif new_piece == 'knight':
            knight = Knight(self.board, self.color, self.x, self.y)
            self.board.get_tile(self.x, self.y).set_contains(knight)
        else:
            print('incorrect parameter for promotion: can only be queen, rook, bishop, knight')

    def find_possible_moves(self):
        if self.color == 'white':
            if self.first_move:
                self.possible_moves = [[self.x - x, self.y] for x in range(1,3)]
            else:
                self.can_eat()
                new_x = self.x - 1
                if self.out_of_bounds_checking(new_x, self.y):
                    self.possible_moves.append([new_x, self.y])
        else:
            if self.first_move:
                self.possible_moves = [[self.x + x, self.y] for x in range(1,3)]
            else:
                new_x = self.x + 1
                if self.out_of_bounds_checking(new_x, self.y):
                    self.possible_moves.append([new_x, self.y])

