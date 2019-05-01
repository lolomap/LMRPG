from os import system
from EXTRA_FILES import PARAMS, extra_funcs
from EXTRA_FILES.cheat_codes import ch_input
import msvcrt
from copy import copy

from items.weapon import *
from items.stuff import *
from items.armor import *


class Enemy:
    # ***Constants***
    MAX_HP = 50
    MIN_HP = 20

    MAX_DAMAGE = 20
    MIN_DAMAGE = 5

    MAX_DISTANCE = 1.0
    MIN_DISTANCE = 0.3
    LARGE_DISTANCE = 0.55

    BONUS_BOW_DAMAGE = 2

    ENEMY_NAMES = ("Dworf", "Gnome", "Wizard", "Goblin", "Gomuncule")

    # ***Methods***
    def __init__(self):
        self.name = rand.choice(self.ENEMY_NAMES)
        self.hp = rand.randint(self.MIN_HP, self.MAX_HP)
        self.distance = rand.triangular(self.MIN_DISTANCE, self.MAX_DISTANCE)
        self.weapon = Weapon()

    def battle(self, pl):

        while self.hp > 0 and pl.hp > 0:
            system("cls")
            pl.show_hud()
            print()
            print("You see {0} in the room. Distance to him is {1}".format(self.name, round(self.distance, 1)))
            print("{0}'s HP is {1}, damage is {2}".format(self.name, self.hp, self.weapon.damage))
            if not PARAMS.TESTING:
                pl_choice = ch_input(pl)
            else:
                pl_choice = pl.weapons[0].name
                print("HITTING")

            for i in pl.weapons:
                if pl_choice == i.name:
                    if i.item_type != "bow":
                        if i.speed > self.weapon.speed:
                            self.hp -= i.damage
                        elif i.speed == self.weapon.speed:
                            prob = rand.randint(0, 1)
                            if prob:
                                self.hp -= i.damage
                    else:
                        if i.speed >= self.weapon.speed:
                            if self.distance >= self.LARGE_DISTANCE:
                                self.hp -= i.damage*self.BONUS_BOW_DAMAGE
                            else:
                                self.hp -= i.damage

            armor_damage = "BODY"
            if pl.armor:
                pl_armor = rand.choice(pl.armor)
                if pl_armor is not None:
                    sum_damage = self.weapon.damage*(1-pl_armor.defeat)
                    pl_armor.durability -= 1
                    armor_damage = pl_armor.name
                else:
                    sum_damage = self.weapon.damage
            else:
                sum_damage = self.weapon.damage
            print("{0} hitted your {1} in {2} points with {3}".format(self.name, armor_damage,
                                                                      sum_damage, self.weapon.name))

            pl.hp -= sum_damage
            print("\nPress any key to continue")
            # msvcrt.getwch()
            # Use this when you make .exe

        i = 0
        while i < len(pl.armor):
            if pl.armor[i].durability <= 0:
                del pl.armor[i]
            else:
                i += 1

        if self.hp <= 0:
            is_loot = extra_funcs.rand(yes=60, no=40)
            if is_loot:
                loot = copy(self.weapon)
                print("You picked up {0}".format(loot.name))
                is_extra_loot = extra_funcs.rand(yes=30, no=70)
                if is_extra_loot:
                    extra_loot = Stuff()
                    print("Also you picked up {0}".format(extra_loot.name))
                    return [loot, extra_loot]
                else:
                    return [loot]


# TODO: Add item using
# TODO: Balance player's and enemys' params
# TODO: Different probability for armor damage
# TODO: Different count of loot
# TODO: Weapons' durability getting lower
