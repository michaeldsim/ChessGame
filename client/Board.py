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

    # TODO: FIGURE OUT TO FIND REMOVED PIECES FROM TILES AND PUT IN A LIST ON THE BOARD
    def __init__(self):
        self.board = self.create_empty_board()
        # self.populate_board()

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
            for j in range(self.COLUMNS):
                if i == 1:
                    self.get_tile(i, j).set_contains(Pawn(self.board,'white', i, j))
                elif i == 6:
                    self.get_tile(i, j).set_contains(Pawn(self.board, 'black', i, j))

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


board = Board()
# board.print_board()
# board.print_board_matrix_color()
pawn = Pawn(board, 'white', 5, 2)
pawn2 = Pawn(board, 'black', 3, 1)
pawn3 = Pawn(board, 'black', 2, 5)
board.get_tile(5, 2).set_contains(pawn)
board.get_tile(3, 1).set_contains(pawn2)
board.get_tile(2, 5).set_contains(pawn3)
board.print_board_matrix()
board.print_board_matrix_p2()
print('------------Possible Moves---------------')
king = King(board, 'white', 4, 3)
board.get_tile(4, 3).set_contains(king)
king.find_possible_moves()
print(king.possible_moves)
king.show_moves_on_board()
board.print_board_matrix()

