from client.pieces.Piece import Piece
from client.pieces.Rook import *


class King(Piece):
    def __init__(self, board, color, x, y):
        if color == 'white':
            p_type = '♔'
            super().__init__(board, p_type, color, x, y)
            self.has_not_moved = True
            self.is_checked = False
            self.castle_moves = {}
        elif color == 'black':
            p_type = '♚'
            super().__init__(board, p_type, color, x, y)
            self.has_not_moved = True
            self.is_checked = False
            self.castle_moves = {}
        else:
            print('incorrect parameter for piece type')
            quit()

    # Castling may only be done if 
    # the king has never moved, X
    # the rook involved has never moved, X
    # the squares between the king and the rook involved are unoccupied, X
    # the king is not in check, X
    # and the king does not cross over or end on a square attacked by an enemy piece X
    def castle_check(self):
        if self.color == 'white':
            black_possible_moves = self.board.all_possible_moves(self.board.black_pieces)
            # check if king has moved or is checked
            if not self.has_not_moved or self.is_checked:
                return
            # checks which rooks haven't moved
            rooks = []
            for i in self.board.white_pieces:
                if isinstance(i, Rook):
                    if i.has_not_moved:
                        rooks.append(i)
                    else:
                        continue
            if not rooks:
                return
            # checks if tiles between rooks are clear
            for i in rooks:
                dist = i.y - self.y
                if dist < 0:
                    for j in range(-1, dist, -1):
                        if self.board.get_tile(self.x, self.y + j).get_contains() is None:
                            elem = [self.x, self.y + j]
                            if elem in black_possible_moves:
                                break
                            if j == (dist + 1):
                                self.possible_moves.append([self.x, self.y + (j + 1)])
                                self.castle_moves['[{}, {}]'.format(self.x, self.y + (j + 1))] = i
                            else:
                                continue
                        else:
                            return
                else:
                    for j in range(1, dist):
                        if self.board.get_tile(self.x, self.y + j).get_contains() is None:
                            elem = [self.x, self.y + j]
                            if elem in black_possible_moves:
                                break
                            if j == (dist - 1):
                                self.possible_moves.append([self.x, self.y + j])
                                self.castle_moves['[{}, {}]'.format(self.x, self.y + j)] = i
                            else:
                                continue
                        else:
                            return
        else:
            white_possible_moves = self.board.all_possible_moves(self.board.white_pieces)
            # check if king has moved or is checked
            if not self.has_not_moved or self.is_checked:
                return
            # checks which rooks haven't moved
            rooks = []
            for i in self.board.black_pieces:
                if isinstance(i, Rook):
                    if i.has_not_moved:
                        rooks.append(i)
                    else:
                        continue
            if not rooks:
                return
            # checks if tiles between rooks are clear
            for i in rooks:
                dist = i.y - self.y
                if dist < 0:
                    for j in range(-1, dist, -1):
                        if self.board.get_tile(self.x, self.y + j).get_contains() is None:
                            elem = [self.x, self.y + j]
                            if elem in white_possible_moves:
                                break
                            if j == (dist + 1):
                                self.possible_moves.append([self.x, self.y + (j + 1)])
                                self.castle_moves['[{}, {}]'.format(self.x, self.y + (j + 1))] = i
                            else:
                                continue
                        else:
                            return
                else:
                    for j in range(1, dist):
                        if self.board.get_tile(self.x, self.y + j).get_contains() is None:
                            elem = [self.x, self.y + j]
                            if elem in white_possible_moves:
                                break
                            if j == (dist - 1):
                                self.possible_moves.append([self.x, self.y + j])
                                self.castle_moves['[{}, {}]'.format(self.x, self.y + j)] = i
                            else:
                                continue
                        else:
                            return

    def move(self, x, y):

        elem = [x, y]
        if self.has_not_moved:
            elem_string = '{}'.format(elem)

        if elem in self.possible_moves:
            if elem_string in self.castle_moves:
                if y < self.y:
                    rook = self.castle_moves[elem_string]
                    rook.debug_move(x, y + 1)
                    rook.has_not_moved = False
                    rook.find_possible_moves()
                else:
                    rook = self.castle_moves[elem_string]
                    rook.debug_move(x, y - 1)
                    rook.has_not_moved = False
                    rook.find_possible_moves()

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
            self.has_not_moved = False
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

    def find_possible_moves(self):
        if self.color == 'white':
            enemy_possible_moves = self.board.all_possible_moves(self.board.black_pieces)
        else:
            enemy_possible_moves = self.board.all_possible_moves(self.board.white_pieces)

        self.castle_check()

        if self.out_of_bounds_checking(self.x, self.y - 1):
            if [self.x, self.y - 1] not in enemy_possible_moves:
                self.possible_moves.append([self.x, self.y - 1])
        if self.out_of_bounds_checking(self.x, self.y + 1):
            if [self.x, self.y + 1] not in enemy_possible_moves:
                self.possible_moves.append([self.x, self.y + 1])

        new_x = self.x - 1
        if self.out_of_bounds_checking(new_x, self.y):
            pattern = [[new_x, self.y + y] for y in range(-1, 2)]
            for i in pattern:
                piece = self.board.get_tile(i[0], i[1]).get_contains()
                if piece is None:
                    if [i[0], i[1]] not in enemy_possible_moves:
                        self.possible_moves.append([i[0], i[1]])
                    continue

                if piece.get_color() == self.get_color():
                    continue
                else:
                    if [i[0], i[1]] not in enemy_possible_moves:
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

    def get_coordinates(self):
        return [self.x, self.y]

