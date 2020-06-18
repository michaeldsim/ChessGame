from client.Tile import Tile
from client.pieces.Pawn import *
from client.pieces.Queen import *
from client.pieces.King import *
from client.pieces.Bishop import *
from client.pieces.Rook import *
from client.pieces.Knight import *


class Board:
    ROWS = COLUMNS = 8
    removed_pieces = []
    black_pieces = []
    white_pieces = []

    # TODO: FIGURE OUT TO FIND REMOVED PIECES FROM TILES AND PUT IN A LIST ON THE BOARD
    def __init__(self):
        self.board = self.create_empty_board()
        self.populate_board()

    def create_empty_board(self):
        count = 1
        same = 'white'
        opposite = 'black'
        new_board = [[0 for x in range(self.ROWS)] for y in range(self.COLUMNS)]
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if count % 8 == 0 and count != 0:
                    # this is so that every time it starts a new row the color is the same as the previous
                    # and it will swap all the colors so the alternation will continue
                    color = opposite
                    temp = same
                    same = opposite
                    opposite = temp
                elif count % 2 == 0:
                    color = opposite
                else:
                    color = same
                new_board[i][j] = Tile(None, color, i, j)
                count += 1
        return new_board

    def get_tile(self, x, y):
        return self.board[x][y]

    def populate_board(self):
        # fill in pawns
        for i in range(self.ROWS):
            if i == 2 or i == 3 or i == 4 or i == 5:
                continue
            for j in range(self.COLUMNS):
                if i == 7:
                    if j == 0 or j == 7:
                        piece = Rook(self.board, 'white', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 1 or j == 6:
                        piece = Knight(self.board, 'white', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 2 or j == 5:
                        piece = Bishop(self.board, 'white', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 3:
                        piece = Queen(self.board, 'white', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    else:
                        piece = King(self.board, 'white', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                elif i == 0:
                    if j == 0 or j == 7:
                        piece = Rook(self.board, 'black', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 1 or j == 6:
                        piece = Knight(self.board, 'black', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 2 or j == 5:
                        piece = Bishop(self.board, 'black', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    elif j == 3:
                        piece = Queen(self.board, 'black', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                    else:
                        piece = King(self.board, 'black', i, j)
                        self.get_tile(i, j).set_contains(piece)
                        self.white_pieces.append(piece)
                elif i == 6:
                    piece = Pawn(self.board, 'white', i, j)
                    self.get_tile(i, j).set_contains(piece)
                    self.white_pieces.append(piece)
                elif i == 1:
                    piece = Pawn(self.board, 'black', i, j)
                    self.get_tile(i, j).set_contains(piece)
                    self.black_pieces.append(piece)

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.get_tile(i, j))

    def print_board_matrix(self):
        print('    0   1   2   3   4   5   6   7')
        for i in range(len(self.board)):
            print('{} ['.format(i), end='')
            for j in range(len(self.board[i])):
                piece = self.get_tile(i, j).contains
                if piece is None:
                    piece = '  '
                if j == self.COLUMNS - 1:
                    print('{}'.format(piece), end='')
                else:
                    print('{},'.format(piece), end=' ')
            print(']')

    def print_board_matrix_p2(self):
        print('    7   6   5   4   3   2   1  0')
        for i in range(len(self.board) - 1, -1, -1):
            print('{} ['.format(i), end='')
            for j in range(len(self.board[i])- 1, -1, -1):
                piece = self.get_tile(i, j).contains
                if piece is None:
                    piece = '  '
                if j == 0:
                    print('{}'.format(piece), end='')
                else:
                    print('{},'.format(piece), end=' ')
            print(']')

    def print_board_matrix_color(self):
        for i in range(len(self.board)):
            print('[', end='')
            for j in range(len(self.board[i])):
                color = self.get_tile(i, j).get_color()
                if color == 'black':
                    print('███', end='')
                else:
                    print('   ', end='')
            print(']')

    @staticmethod
    def all_possible_moves(pieces):
        lst = []
        for piece in pieces:
            lst.extend(piece.possible_moves)
        return lst

    def get_white_king(self):
        for piece in self.white_pieces:
            if not isinstance(King):
                continue
            else:
                return piece

    def get_black_king(self):
        for piece in self.black_pieces:
            if not isinstance(King):
                continue
            else:
                return piece


board = Board()
board.print_board_matrix()
board.print_board_matrix_color()
