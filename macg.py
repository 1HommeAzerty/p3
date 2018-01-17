#! /usr/bin/env python3
# coding: utf-8

class Mac:
    def __init__(self, maze):
        self.maze = maze
        self.position = self.maze.get_mac_position()

        
    def move_right(self):
        
        #print(self.position)
        (x, y) = self.position 
        
        if y < 14 : 
        #SI la position à droite n'est pas un mur FAIRE
            if not self.maze.is_wall(x, y + 1):
                self.position = (x, y + 1)
                self.maze.move_mac(self.position)
            else:
                pass

    def move_left(self):

        (x, y) = self.position

        if 0 < y < 14 : 
        #SI la position à droite n'est pas un mur FAIRE
            if not self.maze.is_wall(x, y - 1):
                self.position = (x, y - 1)
                self.maze.move_mac(self.position)
            else:
                pass

    def move_up(self):

        (x, y) = self.position

        if 0 < x < 14 : 
        #SI la position à droite n'est pas un mur FAIRE
            if not self.maze.is_wall(x -1, y):
                self.position = (x -1, y)
                self.maze.move_mac(self.position)
            else:
                #print("YOu can't go this way")
                pass

    def move_down(self):

        (x, y) = self.position

        if 0 < x < 14 : 
        #SI la position à droite n'est pas un mur FAIRE
            if not self.maze.is_wall(x + 1, y):
                self.position = (x + 1, y)
                self.maze.move_mac(self.position)
            else:
                print("YOu can't go this way")
                pass