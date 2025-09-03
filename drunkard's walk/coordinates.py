class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Coordinates(self.x + dx, self.y + dy)
    
    def distance(self, other_coordinate):
        dx = self.x - other_coordinate.x
        dy = self.y - other_coordinate.y
        return (dx**2 + dy**2)**0.5