from client.pieces.Queen import *
from client.pieces.Rook import *
from client.pieces.Bishop import *
from client.pieces.Knight import *


class Pawn(Piece):
    def __init__(self, board, color, x, y):
        if color == 'black':
            p_type = '♟'
            super().__init__(board, p_type, color, x, y)
            self.first_move = True
        elif color == 'white':
            p_type = '♙'
            super().__init__(board, p_type, color, x, y)
            self.first_move = True
        else:
            print('incorrect parameter for color')
            quit()

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

            piece = self.board.get_tile(x, y).get_contains()
            if piece is None:
                pass
            else:
                self.board.removed_pieces.append(piece)

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

    def promote(self, new_piece):
        """
        :arg
        new_piece is the name of the new piece the pawn is wanting to promote to

        this function will replace the pawn from the current tile with a new object in the same position
        """
        if (self.color == 'white' and self.x == 0) or (self.color == 'black' and self.x == 7):
            if new_piece == 'queen':
                queen = Queen(self.board, self.color, self.x, self.y)
                self.board.get_tile(self.x, self.y).set_contains(queen)
                queen.find_possible_moves()
            elif new_piece == 'rook':
                rook = Rook(self.board, self.color, self.x, self.y)
                self.board.get_tile(self.x, self.y).set_contains(rook)
                rook.find_possible_moves()
            elif new_piece == 'bishop':
                bishop = Bishop(self.board, self.color, self.x, self.y)
                self.board.get_tile(self.x, self.y).set_contains(bishop)
                bishop.find_possible_moves()
            elif new_piece == 'knight':
                knight = Knight(self.board, self.color, self.x, self.y)
                self.board.get_tile(self.x, self.y).set_contains(knight)
                knight.find_possible_moves()
            else:
                print('incorrect parameter for promotion: can only be queen, rook, bishop, knight')
        else:
            print('unable to promote because incorrect coordinates')

    # TODO: IMPLEMENT EN PASSANT
    # if it moves 2 square it can be captured in the current and square it passed over for only one turn (x - 1)
    def find_possible_moves(self):
        if self.color == 'white':
            if self.first_move:
                self.possible_moves = [[self.x - x, self.y] for x in range(1, 3)]
            else:
                new_x = self.x - 1
                if self.out_of_bounds_checking(new_x, self.y):
                    pattern = [[new_x, self.y + y] for y in range(-1, 2)]
                    for i in pattern:
                        pos = self.y - i[1]
                        if pos == -1 or pos == 1:
                            piece = self.board.get_tile(i[0], i[1]).get_contains()
                            if piece is None:
                                continue

                            if piece.get_color() == self.get_color():
                                continue
                            else:
                                self.possible_moves.append([i[0], i[1]])
                        else:
                            piece = self.board.get_tile(i[0], i[1]).get_contains()
                            if piece is None:
                                self.possible_moves.append([i[0], i[1]])
        else:
            if self.first_move:
                self.possible_moves = [[self.x + x, self.y] for x in range(1, 3)]
            else:
                new_x = self.x + 1
                if self.out_of_bounds_checking(new_x, self.y):
                    pattern = [[new_x, self.y + y] for y in range(-1, 2)]
                    for i in pattern:
                        pos = self.y - i[1]
                        if pos == -1 or pos == 1:
                            piece = self.board.get_tile(i[0], i[1]).get_contains()
                            if piece is None:
                                continue

                            if piece.get_color() == self.get_color():
                                continue
                            else:
                                self.possible_moves.append([i[0], i[1]])
                        else:
                            piece = self.board.get_tile(i[0], i[1]).get_contains()
                            if piece is None:
                                self.possible_moves.append([i[0], i[1]])

