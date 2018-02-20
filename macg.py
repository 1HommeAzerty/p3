#! /usr/bin/env py_athon3
# coding: utf-8

"""In charge of the character's actions.

"""
class Mac:

    """Uses positions to manage the character's actions
    movements in all directions if possible
    method to pick up items
    end game conditions

    """

    def __init__(self, maze):
        self.maze = maze
        self.position = self.maze.get_mac_position()
        self.item_pos = self.maze.get_item_pos()
        self.guardian_pos = self.maze.get_guardian_position()
        self.item_count = 0

    def move_right(self):
        """Checks the structure limits and walls
        Moves Mac to the right if possible

        """
        (x_a, y_a) = self.position
        if y_a < 14:
            if not self.maze.is_wall(x_a, y_a + 1):
                self.position = (x_a, y_a + 1)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")

    def move_left(self):
        """Checks the structure limits and walls
        Moves Mac to the left if possible

        """
        (x_a, y_a) = self.position
        if 0 < y_a < 14:
            if not self.maze.is_wall(x_a, y_a - 1):
                self.position = (x_a, y_a - 1)
                self.maze.move_mac(self.position)
            else:
                print("You can't go this way")

    def move_up(self):
        """Checks the structure limits and walls
        Moves Mac up if possible

        """
        (x_a, y_a) = self.position
        if 0 < x_a < 14:
            if not self.maze.is_wall(x_a -1, y_a):
                self.position = (x_a -1, y_a)
                self.maze.move_mac(self.position)
            else:
                print("You can't go up")

    def move_down(self):
        """Checks the structure limits and walls
        Moves Mac down if possible

        """
        (x_a, y_a) = self.position
        if 0 < x_a < 14:
            if not self.maze.is_wall(x_a + 1, y_a):
                self.position = (x_a + 1, y_a)
                self.maze.move_mac(self.position)
            else:
                print("You can't go down")

    def pick_up(self):
        """Add to a counter, and remove the item position if Mac walks on it"""
        for position in self.item_pos:
            if self.position == position:
                print('I got it !!')
                self.item_pos.remove(position)
                self.item_count += 1

    def meet_guardian(self):
        """Checks the item count if Mac gets in the case next to Guardian"""
        (x_a, y_a) = self.guardian_pos

        if (x_a + 1, y_a) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x_a - 1, y_a) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x_a, y_a + 1) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True

        elif (x_a, y_a - 1) == self.position:
            if self.item_count != 3:
                return False
            elif self.item_count == 3:
                return True
