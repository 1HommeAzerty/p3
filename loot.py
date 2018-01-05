class Loot:
    def __init__(self, diplay, maze):
        self.structure = maze.structure
        self.display = display
        self.position = None

    def position(self, position):
        i, j = position
        self.structure[i][j] = self.display
        self.positon = position

