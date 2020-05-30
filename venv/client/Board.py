from client.Tile import Tile


class Board:
    ROWS = COLUMNS = 8

    def __init__(self):
        self.board = self.create_empty_board()

    def create_empty_board(self):
        count = 0
        new_board = [[0 for x in range(self.ROWS)] for y in range(self.COLUMNS)]
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if count % 2 == 0:
                    color = 'white'
                else:
                    color = 'black'
                new_board[i][j] = Tile(None, color, i, j)
                count += 1
        return new_board

    def get_tile(self, x, y):
        return self.board[x][y]

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
                    print(piece, end='')
                else:
                    print(piece + ', ', end='')
            print(']')


board = Board()
board.print_board()
board.print_board_matrix()
