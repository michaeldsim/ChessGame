
class Game(object):

    def __init__(self, board, players):
        self.board = board
        self.players = players

    def get_players(self):
        return self.players

    def get_board(self):
        return self.board
