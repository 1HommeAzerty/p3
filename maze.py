#! /usr/bin/env python3
# coding: utf-8


# -tc- fais attention avec l'indentation. En python, on recommande
# -tc- d'indenter avec 4 espaces
class Maze:
  """docstring for maze"""
  # -tc- pour définir une valeur de file par défaut, le mieux
  # -tc- est de donner une valeur par défaut dans les paramètres
  # -tc- de __init__. Eviter également d'utiliser le mot clé file
  # qui est une fonction intégrée en python. Je remplace par configfile
  def __init__(self, configfile='level1.txt'):
    self.file = configfile
    #self.structure = 0
    # path, walls + guardian

  def generate(self):
    # -tc- Eviter file. J'utilise f ici
    with open(self.file, "r") as f:
      level1 = []
      # -tc- sert à recueillir les positions libres du labyrinthe
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
      # -tc- ajouter la propriété free_positions
      self.free_positions = free_positions
    #return level1

  def position_randomly(self, loots):
    k = len(loots)
    # loots -> [needle, ether, tube]
    # positions -> [(1, 0), (5, 4), (11, 10)]
    positions = random.sample(self.free_positions, k)

    # POUR chaque $position dans $positions et chaque $loot dans $loots FAIRE
    for loot, position in zip(loots, positions):
       loot.position(position) 

  # -tc- L'alternative à l'utilisation de zip serait:
  # for i, loot in enumerate(loots):
  #   loot.position(positions[i])

  # -tc- ou encore
  # for i in range(len(loots)):
  #   loots[i].position(positions[i])

  def getdisplay(self):   
    return maze1
    #for sprite in line_lvl:
      #
    #pass
    #return (level1)

  def display(self):
    for line in self.structure: 
      print("".join(line))

def main():
  maze1 = Maze("level1.txt")
  maze1.generate()
  maze1.display()
  #maze1 = Maze("level1.txt")
  #print (maze1)
main()
