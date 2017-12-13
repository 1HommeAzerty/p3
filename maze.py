#! /usr/bin/env python3
# coding: utf-8


class Maze:
  """docstring for maze"""
  def __init__(self, file):
    self.file = "level1.txt"
    #self.structure = 0
    # path, walls + guardian
    
  def generate(self):
    with open(self.file, "r") as file:
      level1 = []
      
      for line in file:      #parcours des lignes
        line_lvl = []
        
        for sprite in line: #parcours de chaque element
          if sprite != '\n':
            line_lvl.append(sprite)
        level1.append(line_lvl)

      self.structure = level1
    #return level1

    for sprite in level1:
      print(sprite)
    
  def getdisplay(self):
    
    return maze1
    #for sprite in line_lvl:
      #
    #pass
    #return (level1)
maze1 = Maze("level1.txt")
print (maze1.generate())
def main():
  pass
  #maze1 = Maze("level1.txt")
  #print (maze1)
main()