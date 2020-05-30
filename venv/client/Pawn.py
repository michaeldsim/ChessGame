from client.Piece import Piece


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(self, color, x, y)
        # first move has the option to move either one or two spaces
        # this will keep track of that
        self.first_move = True

    def move(self, x, y):
        self.x = x
        self.y = y
        first_move = False

    def find_possible_moves(self):
        if self.first_move:
            lst = [[self.x, self.y + y] for y in range(1,3)]
            self.possible_moves = lst
        else:
            pass
