#! /usr/bin/env python3
# coding: utf-8

"""Creates the main structure and elements for the game"""

import random

class Maze:

    """Gets the level structure from a .txt file.
    Generates the level and returns positions for the game elements.

    """

    def __init__(self, configfile):
        self.file = configfile
        self.structure = 0
        self.paths = 0
        self.wall_positions = 0
        self.mac_position = 0
        self.guardian_position = 0
        self.item_pos = []

    def generate(self):
        """Gets the structure from the .txt file.
        Puts it in lists.
        Creates the coordinates for the game's elements:
        Main character (Mac), Goal (Guardian), Walls, Path.

        """
        with open(self.file, "r") as f_a:
            level1 = []
            free_positions = []
            wall_positions = []
            mac_position = None
            guardian_position = None

            for i, line in enumerate(f_a):
                line_lvl = []

                for j, sprite in enumerate(line):
                    if sprite != '\n':
                        line_lvl.append(sprite)
                    if sprite == " ":
                        free_positions.append((i, j))
                    elif sprite == 'x':
                        wall_positions.append((i, j))
                    elif sprite == 'M':
                        mac_position = i, j
                    elif sprite == 'G':
                        guardian_position = i, j
                level1.append(line_lvl)

        self.structure = level1
        self.paths = free_positions
        self.wall_positions = wall_positions
        self.mac_position = mac_position
        self.guardian_position = guardian_position

    def position_randomly(self, items):
        """Gets a list of items and places them randomly in the maze."""
        k = len(items)
        positions = random.sample(self.paths, k)
        for position, item in zip(positions, items):
            (x_a, y_a) = position
            self.structure[x_a][y_a] = item #item.display
            self.item_pos.append(position)

    def get_item_pos(self):
        """Returns the items position."""
        return self.item_pos

    def get_mac_position(self):
        """Returns the character position."""
        return self.mac_position

    def get_guardian_position(self):
        """Returns the guardian position."""
        return self.guardian_position

    def move_mac(self, new_position):
        """
        Gets a new position as argument that replaces the actual character's postion.

        """
        actual_position = self.get_mac_position()
        (x_a, y_a) = actual_position
        self.structure[x_a][y_a] = ' '
        (x_a, y_a) = new_position
        self.structure[x_a][y_a] = 'M'
        self.mac_position = new_position

    def is_wall(self, x_a, y_a):
        """Returns the coordinates of the walls blocks."""
        return (x_a, y_a) in self.wall_positions

    def walls_pos(self):
        """Returns walls positions in a list."""
        return self.wall_positions

    def getdisplay(self):
        """Returns the maze's structure."""
        return self.structure

    def display(self):
        """Cleans and prints the maze's structure on the console."""
        for line in self.structure:
            print("".join(line))

def main():
    """Creates instances of Maze, generates and displays the maze."""
    maze1 = Maze("level1.txt")
    maze1.generate()
    maze1.display()

if __name__ == "__main__":
    main()
