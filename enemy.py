import random as rand
from os import *
import msvcrt
import probrand
import player


class Enemy:
    # ***Constants***
    MAX_HP = 145
    MIN_HP = 30

    MAX_DAMAGE = 43
    MIN_DAMAGE = 15

    MAX_DISTANCE = 1.0
    MIN_DISTANCE = 0.3
    LARGE_DISTANCE = 0.55
    SMALL_DISTANCE = 0.4

    BONUS_BOW_DAMAGE = 6
    MULCT_BOW_DAMAGE = 4

    NAMES = ("SCELETON", "ZOMBIE", "WIZARD", "DRAGON", "DWORF")
    WEAPONS = ("Knife", "Steel Axe", "Bow")

    MIN_DURABILITY = 2
    MAX_DURABILITY = 40

    # ***Variables***
    name = None
    hp = None
    damage = None
    distance = None
    weapon = None
    durability = None

    # ***Methods***
    def __init__(self):
        self.name = rand.choice(self.NAMES)
        self.hp = rand.randint(self.MIN_HP, self.MAX_HP)
        self.damage = rand.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)
        self.distance = rand.triangular(self.MIN_DISTANCE, self.MAX_DISTANCE)
        self.weapon = rand.choice(self.WEAPONS)
        self.durability = rand.randint(self.MIN_DURABILITY, self.MAX_DURABILITY)

    def battle(self, pl):
        if type(pl) != player.Player:
            raise Exception("Wrong 'pl' param")

        while self.hp > 0 and pl.hp > 0:
            system("cls")
            pl.show_hud()
            print()
            print("You see {0} in the room. Distance to him is {1}".format(self.name, self.distance))
            print("{0}'s HP is {1}, damage is {2}".format(self.name, self.hp, self.damage))
            print("Choose your weapon: {0}".format(pl.weapons))
            pl_choice = input()
            for i in pl.weapons:
                if pl_choice == i[0]:
                    if i[0] != "Bow":
                        self.hp -= i[len(i) - 1]
                    else:
                        if self.distance > self.LARGE_DISTANCE:
                            self.hp -= i[len(i) - 1] + self.BONUS_BOW_DAMAGE
                        elif self.distance < self.MIN_DISTANCE:
                            self.hp -= i[len(i) - 1] - self.MULCT_BOW_DAMAGE
                        else:
                            self.hp -= i[len(i - 1)]

            print("{0} give you damage in {1} points with {2}".format(self.name, self.damage, self.weapon))
            pl.hp -= self.damage
            # print("\nPress any key to continue")
            # msvcrt.getwch() Use this when you make .exe

        if self.hp <= 0:
            is_loot = probrand.rand(yes=60, no=40)
            if is_loot:
                s = ["Weapon", self.weapon, self.durability, self.damage]
                ss = s.copy()
                del ss[0]
                print("You picked up {0}".format(ss))
                return s

# TODO: Add extra loot from enemies
# TODO: Add armor damage
# TODO: Add item using
