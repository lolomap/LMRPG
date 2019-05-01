import numpy as np

from enemy import *
from items.weapon import *
from items.armor import *
from items.stuff import *


class Map:
    # ***Constants***
    MAX_WIDTH = 5
    MAX_HEIGHT = 5

    MIN_WIDTH = 2
    MIN_HEIGHT = 2

    MIN_ROOMS = 4

    ROOMS = ("EMPTY", "CHEST", "ITEM", "ENEMY", "EXIT")

    # ***Methods***
    def __init__(self):
        self.width = rand.randint(self.MIN_WIDTH, self.MAX_WIDTH)
        self.height = rand.randint(self.MIN_HEIGHT, self.MAX_HEIGHT)

        self.data = np.array(([], []), dtype=object)

        self.is_right = False
        self.is_left = False
        self.is_forward = False
        self.is_back = False
        self.data.resize(self.height, self.width, refcheck=False)

        for i in range(self.height):
            for j in range(self.width):
                self.data[i][j] = rand.choice(self.ROOMS)

    def action(self, x, y, pl):
        room_type = self.data[y][x]
        if room_type == "EMPTY":
            print("This room is empty. You haven't reason to stay here")
        elif room_type == "ITEM":
            w = Weapon()
            a = Armor()
            s = Stuff()
            found_item = rand.choice([w, a, s])
            print("You see table at middle of room\n"
                  "There {0} on the table\n"
                  "Do you want to pick it up?".format(found_item.name))
            if not PARAMS.TESTING:
                pl_choice = ch_input(pl)
                pl_choice = pl_choice.upper()
            else:
                pl_choice = "YES"
            if pl_choice == "YES":
                self.data[y][x] = "EMPTY"
                return [found_item]
        elif room_type == "EXIT":
            print("This is exit from the floor. Do you want to exit?")
            if not PARAMS.TESTING:
                pl_choice = ch_input(pl)
                pl_choice = pl_choice.upper()
            else:
                pl_choice = "YES"
            if pl_choice == "YES":
                return 0
        elif room_type == "ENEMY":
            e = Enemy()
            return e

        print()

    def move_possibilities(self, x, y):
        print("Possible directions:", end=' ')
        if 0 <= x + 1 < self.width:
            print("right", end=' ')
            self.is_right = True
        else:
            self.is_right = False
        if 0 <= x - 1 < self.width:
            print("left", end=' ')
            self.is_left = True
        else:
            self.is_left = False
        if 0 <= y - 1 < self.height:
            print("forward", end=' ')
            self.is_forward = True
        else:
            self.is_forward = False
        if 0 <= y + 1 < self.height:
            print("back", end=' ')
            self.is_back = True
        else:
            self.is_back = False

        print()

    def show_map(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.data[i][j], end='\t')
            print()

# TODO: limit for some rooms and locked rooms
