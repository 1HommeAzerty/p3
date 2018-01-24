#! /usr/bin/env python3
# coding: utf-8

from maze import*
from loot import*
from macg import*

class Game:

    def __init__(self):
        maze1 = Maze("level1.txt")         
        needle = Loot('N')
        ether = Loot('E') 
        tube = Loot('T') 
        maze1.generate() 
        

        maze1.position_randomly([needle.disp, ether.disp, tube.disp])
        maze1.get_mac_position()
        maze1.get_guardian_position()
        mg = Mac(maze1)     
        maze1.display()

        self.item_pos = maze1.get_item_pos()
        self.loot = needle, ether, tube
        self.maze = maze1
        self.macg = mg

    def start(self):
        game_continue = True  

        while game_continue:
            answer = input('Press U, D, L or R to move, Q to quit: ')
            
            if answer == 'R':
                self.macg.move_right()
                self.macg.pick_up(self.item_pos)
                self.maze.display()

            if answer == 'L':
                self.macg.move_left()
                self.macg.pick_up(self.item_pos)
                self.maze.display()

            if answer == 'U':
                self.macg.move_up()
                self.macg.pick_up(self.item_pos)
                self.maze.display()

            if answer == 'D':
                self.macg.move_down()
                self.macg.pick_up(self.item_pos)
                self.maze.display()
                #if game_continue:

            if answer == 'Q':
                game_continue = False
def main():
    game = Game()
    game.start()
if __name__ == '__main__':
    main()