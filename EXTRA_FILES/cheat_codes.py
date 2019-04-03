import player
CHEAT_CODES = ("gw_", "gi_", "ga_", "hl_")


def ch_input(pl, cheat=None):
    if type(pl) != player.Player:
        raise Exception("Wrong 'pl' param")
    if cheat is not None:
        s = cheat
        if s[0:3] == "gw_":
            ss = s[3:].split('_')
            weapon = [ss[0], int(ss[1]), int(ss[2])]
            pl.weapons.append(weapon)
        elif s[0:3] == "gi_":
            ss = s[3:].split('_')
            item = [ss[0], ss[1], int(ss[2])]
            pl.inventory.append(item)
        elif s[0:3] == "ga_":
            ss = s[3:].split('_')
            armor = [ss[0], int(ss[1])]
            pl.armor.append(armor)
        elif s[0:3] == "hl_":
            hp = int(s[3:])
            pl.hp = hp
        return
    while True:
        s = input()
        if not CHEAT_CODES.__contains__(s[0:3]):
            return s

        if s[0:3] == "gw_":
            ss = s[3:].split('_')
            weapon = [ss[0], int(ss[1]), int(ss[2])]
            pl.weapons.append(weapon)
        elif s[0:3] == "gi_":
            ss = s[3:].split('_')
            item = [ss[0], ss[1], int(ss[2])]
            pl.inventory.append(item)
        elif s[0:3] == "ga_":
            ss = s[3:].split('_')
            armor = [ss[0], int(ss[1])]
            pl.armor.append(armor)
        elif s[0:3] == "hl_":
            hp = int(s[3:])
            pl.hp = hp
