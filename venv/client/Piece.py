import abc


class Piece(metaclass=abc.ABCMeta):
    def __init__(self, piece_type,color, x, y):
        self.piece_type = piece_type
        self.color = color
        self.x = x
        self.y = y
        self.possible_moves = []

    def get_color(self):
        return self.color

    def move(self, x, y):
        self.x = x
        self.y = y
        find_possible_moves()

    def out_of_bounds_checking(self):
        """
        checks if the coordinate is out of bounds
        """
        if x > 7 or x > 0 or y > 7 or y > 0:
            print("Out of bounds error!\nCoordinates: ({},{})".format(self.x, self.y))
            return False
        else:
            return True

    @abc.abstractmethod
    def find_possible_moves(self):
        pass

