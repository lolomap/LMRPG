from items.weapon import *
from items.armor import *
CHEAT_CODES = ("gw", "ga", "hl")


def ch_input(pl, cheat=None):
    if cheat is not None:
        if cheat == "gw":
            pl.weapons.append(Weapon(999, 999))
        elif cheat == "ga":
            pl.armor.append(Armor(999, 1))
        elif cheat == "hl":
            pl.hp = 9999
        return
    while True:
        s = input()
        if s == "gw":
            pl.weapons.append(Weapon(999, 999, True))
        elif s == "ga":
            pl.armor.append(Armor(999, 1))
        elif s == "hl":
            pl.hp = 9999
        else:
            return s
