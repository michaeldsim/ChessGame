
class Tile:
    def __init__(self, contains, color, x, y):
        self.contains = contains
        self.color = color
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_contains(self):
        return self.contains

    def set_contains(self, contains):
        self.contains = contains

    def get_color(self):
        return self.color

    def __str__(self):
        return 'Tile Coords: ({},{}) Color: {} Contains: {}'.format(self.x, self.y, self.color, self.contains.__str__())
