#! /usr/bin/env python3
# coding: utf-8

class Mac:
    def __init__(self, maze):
        self.maze = maze
        self.position = self.maze.get_mac_position()
        self.item_pos = self.maze.get_item_pos()

        
    def move_right(self):
        
        (x, y) = self.position 
        
        if y < 14 :
        #SI la position à droite n'est pas un mur FAIRE
            if not self.maze.is_wall(x, y + 1):
                self.position = (x, y + 1)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")
                pass

    def move_left(self):

        (x, y) = self.position

        if 0 < y < 14 : 
        #SI la position à gauche n'est pas un mur FAIRE
            if not self.maze.is_wall(x, y - 1):
                self.position = (x, y - 1)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")
                pass

    def move_up(self):

        (x, y) = self.position

        if 0 < x < 14 : 
        #SI la position au dessus n'est pas un mur FAIRE
            if not self.maze.is_wall(x -1, y):
                self.position = (x -1, y)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")
                pass

    def move_down(self):

        (x, y) = self.position

        if 0 < x < 14 : 
        #SI la position au dessous n'est pas un mur FAIRE
            if not self.maze.is_wall(x + 1, y):
                self.position = (x + 1, y)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")
                pass

    def pick_up(self, item_pos):
        #print (self.item_pos)
        for position in self.item_pos:
            if self.position == position:
                print('I got it !!')