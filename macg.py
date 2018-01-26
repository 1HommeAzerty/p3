#! /usr/bin/env python3
# coding: utf-8

class Mac:
    def __init__(self, maze):
        self.maze = maze
        self.position = self.maze.get_mac_position()
        self.item_pos = self.maze.get_item_pos()
        self.guardian_pos = self.maze.get_guardian_position()
        self.item_count = 0

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
                print("You can't go up")
                pass

    def move_down(self):

        (x, y) = self.position

        if 0 < x < 14 : 
        #SI la position au dessous n'est pas un mur FAIRE
            if not self.maze.is_wall(x + 1, y):
                self.position = (x + 1, y)
                self.maze.move_mac(self.position)
            else:
                print("You can't go down")
                pass

    def pick_up(self): 
        for position in self.item_pos:
            if self.position == position:
                print('I got it !!')
                self.item_pos.remove(position)
                self.item_count += 1
    
    def get_item_count(self):
        print(self.item_count)

    def meet_guardian(self):
        (x, y) = self.guardian_pos

        if (x + 1, y) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x - 1, y) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x, y + 1) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x, y - 1) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True