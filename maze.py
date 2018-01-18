#! /usr/bin/env python3
# coding: utf-8
import random
#import loot

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

    #def position_randomly(self, items):
    #    positions = random.sample(self.paths, 3)    #loot list len
    #    items = self.loot.get_display()# = items
    #    for position, item in zip(positions, items):
    #        (x, y) = position
    #        self.structure[x][y] = self.loot.get_display(items) #get_display method from loot to get instances

    def get_mac_position(self):
        return self.mac_position 

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