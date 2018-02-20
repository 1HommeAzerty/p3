#! /usr/bin/env python3
# coding: utf-8

"""Makes the game run in text mode"""

from maze import Maze
from loot import Loot
from macg import Mac

class GameText:

    """Creates the instances for the main elements of the game.
    Uses those element to run the game loop.

    """

    def __init__(self):
        maze1 = Maze("level1.txt")
        needle = Loot('N')
        ether = Loot('E')
        tube = Loot('T')
        maze1.generate()

        maze1.position_randomly([needle.disp, ether.disp, tube.disp])
        m_g = Mac(maze1)

        self.maze = maze1
        self.macg = m_g


    def start(self):
        """Starts & stops the game loop"""
        game_continue = True

        while game_continue:
            self.maze.display()
            answer = input('Press U, D, L or R to move, Q to quit: ')

            if answer == 'R':
                self.macg.move_right()

            elif answer == 'L':
                self.macg.move_left()

            elif answer == 'U':
                self.macg.move_up()

            elif answer == 'D':
                self.macg.move_down()

            elif answer == 'Q':
                game_continue = False

            self.macg.pick_up()

            if self.macg.meet_guardian() is False:
                print('Game Over Mac Gyver !!!')
                game_continue = False

            elif self.macg.meet_guardian() is True:
                print('Well Done !!')
                game_continue = False

def main():
    """Creates instance of GameText and starts the game"""
    game = GameText()
    game.start()

if __name__ == '__main__':
    main()
