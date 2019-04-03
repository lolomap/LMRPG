import random as rand
from os import system
from EXTRA_FILES import PARAMS, probrand, GAME_ELEMENTS
from EXTRA_FILES.cheat_codes import ch_input
import player


class Enemy:
    # ***Constants***
    MAX_HP = 50
    MIN_HP = 20

    MAX_DAMAGE = 20
    MIN_DAMAGE = 5

    MAX_DISTANCE = 1.0
    MIN_DISTANCE = 0.3
    LARGE_DISTANCE = 0.55
    SMALL_DISTANCE = 0.4

    BONUS_BOW_DAMAGE = 6
    MULCT_BOW_DAMAGE = 4

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
        self.name = rand.choice(GAME_ELEMENTS.ENEMY_NAMES)
        self.hp = rand.randint(self.MIN_HP, self.MAX_HP)
        self.damage = rand.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)
        self.distance = rand.triangular(self.MIN_DISTANCE, self.MAX_DISTANCE)
        self.weapon = rand.choice(GAME_ELEMENTS.WEAPON_NAMES)
        self.durability = rand.randint(self.MIN_DURABILITY, self.MAX_DURABILITY)

    def battle(self, pl):
        if type(pl) != player.Player:
            raise Exception("Wrong 'pl' param")

        while self.hp > 0 and pl.hp > 0:
            system("cls")
            pl.show_hud()
            print()
            print("You see {0} in the room. Distance to him is {1}".format(self.name, round(self.distance, 1)))
            print("{0}'s HP is {1}, damage is {2}".format(self.name, self.hp, self.damage))
            print("Choose your weapon: {0}".format(pl.weapons))
            if not PARAMS.TESTING:
                pl_choice = ch_input(pl)
            else:
                pl_choice = pl.weapons[0][0]
                print("HITTING")
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

            armor_damage = ["BODY"]
            if pl.armor:
                armor_damage = rand.choice(pl.armor)
                if armor_damage is not None:
                    sum_damage = self.damage/2
                    armor_damage[1] -= self.damage/2
                else:
                    sum_damage = self.damage
            else:
                sum_damage = self.damage
            print("{0} hitted your {1} in {2} points with {3}".format(self.name, armor_damage[0],
                                                                      sum_damage, self.weapon))

            pl.hp -= sum_damage
            # print("\nPress any key to continue")
            # msvcrt.getwch() Use this when you make .exe

        i = 0
        while i < len(pl.armor):
            if pl.armor[i][1] <= 0:
                del pl.armor[i]
            else:
                i += 1

        if self.hp <= 0:
            is_loot = probrand.rand(yes=60, no=40)
            if is_loot:
                s = ["Weapon", self.weapon, self.durability, self.damage]
                ss = s.copy()
                del ss[0]
                print("You picked up {0}".format(ss))
                is_extra_loot = probrand.rand(yes=30, no=70)
                if is_extra_loot:
                    e_s = rand.choice(GAME_ELEMENTS.ITEMS)
                    return [s, e_s]
                else:
                    return [s]


# TODO: Add item using
# TODO: Balance player's and enemys' params
# TODO: Different probability for armor damage
# TODO: Different count of loot
# TODO: Weapons' durability getting lower
