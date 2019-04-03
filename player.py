from environment import *
from enemy import *


class Player:
    # ***Variables***
    max_hp = 100
    hp = copy(max_hp)
    mana_max = 0
    mana = copy(mana_max)
    armor = []
    inventory = []
    weapons = []
    x = None
    y = None
    xp = 0

    # ***Methods***
    def __init__(self, room):
        if type(room) != Map:
            raise Exception("Wrong 'room' param")

        self.x = rand.randint(0, room.width - 1)
        self.y = rand.randint(0, room.height - 1)

    def move(self, room, dx, dy):
        if type(room) != Map:
            raise Exception("Wrong 'room' param")

        if 0 <= self.x + dx < room.width and 0 <= self.y + dy < room.height:
            self.x += dx
            self.y += dy
        else:
            raise Exception("Cannot move into the wall")

        loot = room.action(self.x, self.y, self)

        if loot is not None and loot[0] != "EXIT" and loot[0] != "ENEMY":
            for i in loot:
                if i[0] == "Armor":
                    del i[0]
                    self.armor.append(i)
                elif i[0] == "Item":
                    del i[0]
                    self.inventory.append(i)
                elif i[0] == "Weapon":
                    del i[0]
                    self.weapons.append(i)
        elif loot is None:
            self.i_do_nothing()
        elif loot[0] == "EXIT":
            return True
        elif loot[0] == "ENEMY":
            if type(loot[1]) != Enemy:
                raise Exception("Wrong 'enemy' param")
            loot = loot[1].battle(self)
            if loot is None:
                print("YOU DIED")
                return -1
            for i in loot:
                if i[0] == "Armor":
                    del i[0]
                    self.armor.append(i)
                elif i[0] == "Item":
                    del i[0]
                    self.inventory.append(i)
                elif i[0] == "Weapon":
                    del i[0]
                    self.weapons.append(i)

        room.move_possibilities(self.x, self.y)
        return False

    def show_hud(self):
        print("HP: {0} / {1}\t".format(self.hp, self.max_hp),
              "Mana: {0} / {1}\t".format(self.mana, self.mana_max),
              "XP: {0}".format(self.xp))
        print("Armor: {0}".format(self.armor))
        print("Inventory: {0}".format(self.inventory))
        print("Weapons: {0}".format(self.weapons))

    def reposition(self, room):
        if type(room) != Map:
            raise Exception("Wrong 'room' param")

        self.x = rand.randint(0, room.width - 1)
        self.y = rand.randint(0, room.height - 1)

    def i_do_nothing(self):
        return
