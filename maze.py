#! /usr/bin/env python3
# coding: utf-8


class Maze:
  """docstring for maze"""
  def __init__(self, file):
    self.file = "level1.txt" #file
    #self.structure = 0
    # path, walls + guardian

  def generate(self):
    with open(self.file, "r") as file:
      level1 = []
      free_positions = []
           
      for i, line in enumerate(file):      #parcours des lignes
        line_lvl = []
        
        for j, sprite in enumerate(line): #parcours de chaque element          
          if sprite != '\n':
            line_lvl.append(sprite)
          if sprite == " ":
            free_positions.append((i, j))
            
        level1.append(line_lvl)

      self.structure = level1
      #self.path = free_positions
      print(free_positions)

  def position_randomly(self, display):
    pass
    
  def getdisplay(self):
    return maze1

  def display(self):
    for line in self.structure:
      print("".join(line))

def main():
  maze1 = Maze("level1.txt")
  maze1.generate()
  maze1.display()
main()