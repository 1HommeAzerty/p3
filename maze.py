#! /usr/bin/env python3
# coding: utf-8
import random

class Maze:
    """docstring for maze"""
    def __init__(self, file):
      self.file = file
      #self.structure = 0
      # path, walls + guardian

    def generate(self):
      with open(self.file, "r") as f:
        level1 = []
        free_positions = []
            
        for i, line in enumerate(f):      #parcours des lignes
          line_lvl = []
          
          for j, sprite in enumerate(line): #parcours de chaque element          
            if sprite != '\n':
              line_lvl.append(sprite)
            if sprite == " ":
              free_positions.append((i, j))
              
          level1.append(line_lvl)

        self.structure = level1
        self.paths = free_positions
        print(free_positions)

    def position_randomly(self):
      
      items = ["N", "E", "T"]
      positions = random.sample(self.paths, 3)

      for position, item in zip(positions, items):
          print(position, item)   

      
    def getdisplay(self):
      return self.structure

    def display(self):
      for line in self.structure:
        print("".join(line))

def main():
    maze1 = Maze("level1.txt")
    maze1.generate()
    maze1.display()
    maze1.position_randomly()
main()