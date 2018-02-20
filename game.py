#! /usr/bin/env python3
# coding: utf-8
# pylint: disable=no-member

"""Makes the game run in graphic mode"""

import time

import pygame
from maze import Maze
from loot import Loot
from macg import Mac

class Game:

    """Creates classes instances
    Uses instances with the pygame module to display graphics

    """

    def __init__(self):
        pygame.init()
        sprite_number = 15
        self.sprite_size = 50
        win_size = sprite_number * self.sprite_size
        self.screen = pygame.display.set_mode((win_size, win_size))
        self.macpic = pygame.image.load("macgyver.png").convert_alpha()
        self.murdoc = pygame.image.load("murdoc.png").convert_alpha()
        self.floor = pygame.image.load("tile1.png").convert_alpha()
        self.wall = pygame.image.load("wall2.png").convert_alpha()
        self.game_over = pygame.image.load("gameover.png").convert_alpha()
        ether_pic = pygame.image.load("ether.png").convert_alpha()
        needle_pic = pygame.image.load("needle.png").convert_alpha()
        tube_pic = pygame.image.load("tube.png").convert_alpha()
        self.stairs = pygame.image.load("stairs.png").convert_alpha()
        self.well_done = pygame.image.load("welldone.png").convert_alpha()
        self.item_pics = []
        self.item_pics.append(ether_pic)
        self.item_pics.append(tube_pic)
        self.item_pics.append(needle_pic)
        pygame.display.set_caption("MazeGyver")
        pygame.display.set_icon(self.macpic)
        maze1 = Maze("level1.txt")
        needle = Loot('N')
        ether = Loot('E')
        tube = Loot('T')
        maze1.generate()

        maze1.position_randomly([needle.disp, ether.disp, tube.disp])
        m_g = Mac(maze1)

        self.walls = maze1.wall_positions
        self.mac_pos = maze1.mac_position
        self.guard_pos = maze1.guardian_position
        self.item_pos = maze1.item_pos
        self.path = maze1.paths
        self.maze = maze1
        self.macg = m_g

        for (x_a, y_a) in self.path:
            self.screen.blit(self.floor, (y_a * self.sprite_size, x_a * self.sprite_size))

        for (x_a, y_a) in self.walls:
            self.screen.blit(self.wall, (y_a * self.sprite_size, x_a * self.sprite_size))

        (x_a, y_a) = self.guard_pos
        self.screen.blit(self.stairs, (y_a * self.sprite_size, x_a * self.sprite_size))

        (x_a, y_a) = self.guard_pos
        self.screen.blit(self.murdoc, (y_a * self.sprite_size, x_a * self.sprite_size))

        for (x_a, y_a), item_pic in zip(self.item_pos, self.item_pics):
            self.screen.blit(item_pic, (y_a * self.sprite_size, x_a * self.sprite_size))

    def start(self):
        """Starts & stops the game loop"""
        game_continue = True

        while game_continue:
            (x_a, y_a) = self.mac_pos
            self.screen.blit(self.floor, (y_a * self.sprite_size, x_a * self.sprite_size))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_continue = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_continue = False

                    elif event.key == pygame.K_UP:
                        self.macg.move_up()

                    elif event.key == pygame.K_RIGHT:
                        self.macg.move_right()

                    elif event.key == pygame.K_DOWN:
                        self.macg.move_down()

                    elif event.key == pygame.K_LEFT:
                        self.macg.move_left()

            self.mac_pos = self.maze.mac_position
            self.macg.pick_up()

            (x_a, y_a) = self.mac_pos
            self.screen.blit(self.macpic, (y_a * self.sprite_size, x_a * self.sprite_size))

            if self.macg.meet_guardian() is False:
                 #time.sleep(1)
                self.path.append(self.guard_pos)
                self.path.append((1, 0))
                for (x_a, y_a) in self.path:
                    self.screen.blit(self.wall, (y_a * self.sprite_size, x_a * self.sprite_size))
                #time.sleep(2)
                self.screen.blit(self.game_over, (50, 300))
                print('Game Over Mac Gyver !!!')
                game_continue = False

            elif self.macg.meet_guardian() is True:
                self.screen.blit(self.well_done, (50, 300))
                print('Well Done !!')
                game_continue = False

            pygame.display.flip()
        time.sleep(5)
        pygame.quit()

def main():
    """Creates instance of Game and starts the game"""
    game = Game()
    game.start()

if __name__ == '__main__':
    main()
