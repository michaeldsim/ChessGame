from client.Piece import Piece


class Pawn(Piece):
    def __init__(self, board, color, x, y):
        super().__init__(board,'Pawn', color, x, y)
        # first move has the option to move either one or two spaces
        # this will keep track of that
        self.first_move = True

    def move(self, x, y):
        if self.first_move:
            self.first_move = False
        self.x = x
        self.y = y
        self.find_possible_moves()

    # need to add thing to check if can eat another piece. only move 1 diagonally
    # x-1, y+1
    # x+1, y+1
    def can_eat(self):
        pass

    # you get to the end you promote to queen
    def promote(self):
        pass

    def find_possible_moves(self):
        if self.first_move:
            # TODO: this only works for player 1 as of right now.
                # when finished with core game, need to add functionality for either player
            self.possible_moves = [[self.x, self.y + y] for y in range(1,3)]
        else:
            pass
