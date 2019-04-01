import random as rand
import numpy as np
from copy import *


class Map:
    # Constants
    MAX_WIDTH = 5
    MAX_HEIGHT = 5

    MIN_WIDTH = 2
    MIN_HEIGHT = 2

    MIN_ROOMS = 4

    ROOMS = ("EMPTY", "CHEST", "ITEM", "ENEMY", "BONUS CHEST", "EXIT")
    ITEMS = (["Armor", "Helmet", 12], ["Armor", "Chain Mail", 30],
             ["Weapon", "Knife", 13, 10], ["Weapon", "Bow", 20, 3],
             ["Item", "Poision", "Large Heal", 40], ["Item", "Posion", "Small Heal", 20], ["Item", "Arrow", 12])

    # Variables
    width = 0
    height = 0

    data = np.array(([], []), dtype=object)

    is_right = False
    is_left = False
    is_forward = False
    is_back = False

    # Methods
    def __init__(self):
        self.width = rand.randint(self.MIN_WIDTH, self.MAX_WIDTH)
        self.height = rand.randint(self.MIN_HEIGHT, self.MAX_HEIGHT)

        self.data.resize(self.height, self.width, refcheck=False)

        for i in range(self.height):
            for j in range(self.width):
                self.data[i][j] = rand.choice(self.ROOMS)

    def action(self, x, y):
        print()

        room_type = self.data[y][x]
        if room_type == "EMPTY":
            print("This room is empty. You haven't reason to stay here")
            return ["EMPTY"]
        elif room_type == "ITEM":
            found_item = rand.choice(self.ITEMS)
            output_item = copy(found_item)
            del output_item[0]
            print("You see table at middle of room\n"
                  "There {0} on the table\n"
                  "Do you want to pick it up?".format(output_item))
            pl_choice = input()
            pl_choice = pl_choice.upper()
            if pl_choice == "YES":
                return [found_item]
        elif room_type == "EXIT":
            print("This is exit from the floor. Do you want to exit?")
            pl_choice = input()
            pl_choice = pl_choice.upper()
            if pl_choice == "YES":
                return ["EXIT"]
        else:
            return ["EMPTY"]

        print()

    def move_possibilities(self, x, y):
        print("Possible directions:", end=' ')
        if 0 <= x+1 < self.width:
            print("right", end=' ')
            self.is_right = True
        else:
            self.is_right = False
        if 0 <= x-1 < self.width:
            print("left", end=' ')
            self.is_left = True
        else:
            self.is_left = False
        if 0 <= y-1 < self.height:
            print("forward", end=' ')
            self.is_forward = True
        else:
            self.is_forward = False
        if 0 <= y+1 < self.height:
            print("back", end=' ')
            self.is_back = True
        else:
            self.is_back = False

        print()

    def show_map(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.data[i][j], end=' ')
            print()
