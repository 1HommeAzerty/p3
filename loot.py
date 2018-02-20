#! /usr/bin/env python3
# coding: utf-8

"""In charge of items""" 
class Loot:

    """Creates the items"""

    def __init__(self, display):
        self.disp = display

def main():
    """Creates loot instances"""
    needle = Loot('N')
    ether = Loot('E')
    tube = Loot('T')

if __name__ == '__main__':
    main()
