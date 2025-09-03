class Field():
    def __init__(self):
        self.drunk_coordinates = {}

    def add_drunk(self, drunk, coordinate):
        self.drunk_coordinates[drunk] = coordinate

    def move_drunk(self, drunk):
        dx, dy = drunk.walk()
        current_coordinate = self.drunk_coordinates[drunk]
        new_coordinate = current_coordinate.move(dx, dy)
        self.drunk_coordinates[drunk] = new_coordinate

    def get_coordinate(self, drunk):
        return self.drunk_coordinates[drunk]