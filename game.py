#! /usr/bin/env python3
# coding: utf-8

import pygame
from maze import*
from loot import*
from macg import*

pygame.init()
sprite_number = 15
sprite_size = 40
win_size = sprite_number * sprite_size
screen = pygame.display.set_mode((win_size, win_size))
macpic = pygame.image.load("macgyver.png").convert_alpha()
murdoc = pygame.image.load("murdoc.png").convert_alpha()
floor = pygame.image.load("tile2.png").convert_alpha()
wall = pygame.image.load("wall1.png").convert_alpha()
ether_pic = pygame.image.load("ether.png").convert_alpha()
needle_pic = pygame.image.load("needle.png").convert_alpha()
tube_pic = pygame.image.load("tube.png").convert_alpha()
item_pics = []
item_pics.append(ether_pic)
item_pics.append(tube_pic)
item_pics.append(needle_pic)
pygame.display.set_caption("MazeGyver")
pygame.display.set_icon(macpic)
maze1 = Maze("level1.txt")
needle = Loot('N')
ether = Loot('E')
tube = Loot('T') 
maze1.generate()

maze1.position_randomly([needle.disp, ether.disp, tube.disp])
mg = Mac(maze1)

walls = maze1.wall_positions
mac_pos = maze1.mac_position
guard_pos = maze1.guardian_position
item_pos = maze1.item_pos
path = maze1.paths
maze = maze1
macg = mg


game_continue = True

while game_continue:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_continue = False

            elif event.key == pygame.K_UP:
                macg.move_up()

            elif event.key == pygame.K_RIGHT:
                macg.move_right()      
                
                if not (1, 0) in path:
                    path.append((1,0))

            elif event.key == pygame.K_DOWN:
                macg.move_down()

            elif event.key == pygame.K_LEFT:
                macg.move_left()

            mac_pos = maze.mac_position
            macg.pick_up()

    for (x, y) in walls:
        screen.blit(wall, (y * sprite_size, x * sprite_size))

    for (x, y) in path:
        screen.blit(floor, (y * sprite_size, x * sprite_size))

    (x, y) = guard_pos
    screen.blit(murdoc, (y * sprite_size, x * sprite_size))

    (x, y) = mac_pos
    screen.blit(macpic, (y * sprite_size, x * sprite_size))
    
    for (x, y), item_pic in zip (item_pos, item_pics):
        screen.blit(item_pic, (y * sprite_size, x * sprite_size))

    if macg.meet_guardian() == False:
        print('Game Over Mac Gyver !!!')
        game_continue = False

    elif macg.meet_guardian() == True:
        print('Well Done !!')
        game_continue = False


    pygame.display.flip()

pygame.quit()