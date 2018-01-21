#! /usr/bin/env python3
# coding: utf-8
import random


class Maze:
    """docstring for maze"""
    def __init__(self, configfile):
        self.file = configfile
        #self.structure = 0
        # path, walls + guardian

    def generate(self):
        with open(self.file, "r") as f:
            level1 = []
            free_positions = []
            wall_positions = []
            mac_position = None
            guardian_position = None

            for i, line in enumerate(f):    #parcours des lignes
                line_lvl = []
                
                for j, sprite in enumerate(line):   #parcours de chaque element
                    if sprite != '\n':
                        line_lvl.append(sprite)
                    if sprite == " ":
                        free_positions.append((i, j))
                    elif sprite == 'x':
                        wall_positions.append((i,j))
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
        self.item_pos = []

    def position_randomly(self, items):
        k = len(items)
        positions = random.sample(self.paths, k)
        for position, item in zip(positions, items):
            (x, y) = position
            self.structure[x][y] = item
            self.item_pos.append(position)
        
    def get_item_pos(self):
        return self.item_pos

    def get_mac_position(self):
        return self.mac_position 

    def get_guardian_position(self):
        return self.guardian_position

    def move_mac(self, new_position):
        actual_position = self.get_mac_position()
        (x, y) = actual_position
        self.structure[x][y] = ' '
        (x, y) = new_position
        self.structure[x][y] = 'M'
        self.mac_position = new_position


    def is_wall (self, x, y):
        return (x, y) in self.wall_positions 

    def getdisplay(self):
        return self.structure

    def display(self):
        for line in self.structure:
            print("".join(line))

def main():
    maze1 = Maze("level1.txt")
    maze1.generate()
    maze1.position_randomly()
    maze1.display()
    maze1.is_wall()
if __name__ == "__main__":
    main()