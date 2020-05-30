from client.Tile import Tile
from Pawn import *


class Board:
    ROWS = COLUMNS = 8

    def __init__(self):
        self.board = self.create_empty_board()
        self.populate_board()

    def create_empty_board(self):
        count = 1
        color = ''
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
        for i in range(len(self.board)):
            print('[', end='')
            for j in range(len(self.board[i])):
                piece = self.get_tile(i, j).contains
                if piece is None:
                    piece = 'empty'
                if j == self.COLUMNS - 1:
                    print('{}'.format(piece), end='')
                else:
                    print('{}, '.format(piece), end='')
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
board.print_board()
board.print_board_matrix()
board.print_board_matrix_color()
