#! /usr/bin/env python3
# coding: utf-8


class Game:
    
    def __init__(self):
        maze1 = Maze("level1.txt")
        needle = Loot('N')
        ether = Loot('E')
        tube = Loot('T')


        maze1.position_randomly([needle, ether, tube])

    def start(self):
        while game_continue:
            maze1.display()
            answer = imput('Press Arrows to move Q to quit:')
            if answer == move:
                continue
                if game_end:
                    print ('Congratulations !' )
            if answer == 'Q'
                break
        pass