from environment import *
from enemy import *


class Player:

    # ***Methods***
    def __init__(self, room):
        self.max_hp = 100
        self.hp = copy(self.max_hp)
        self.mana_max = 0
        self.mana = copy(self.mana_max)
        self.armor = []
        self.inventory = []
        self.weapons = []
        self.xp = 0
        self.x = rand.randint(0, room.width - 1)
        self.y = rand.randint(0, room.height - 1)

    def move(self, room, dx=None, dy=None, nx=None, ny=None):
        if type(room) != Map:
            raise Exception("Wrong 'room' param")

        if dx is not None and dy is not None:
            if 0 <= self.x + dx < room.width and 0 <= self.y + dy < room.height:
                self.x += dx
                self.y += dy
            else:
                raise Exception("Cannot move into the wall")
        elif nx is not None and ny is not None:
            if 0 <= nx < room.width and 0 <= ny < room.height:
                self.x = nx
                self.y = ny
            else:
                raise Exception("Cannot move into the wall")
        else:
            raise Exception("Wrong move params")

        loot = room.action(self.x, self.y, self)

        if loot == 0:
            return True

        if loot is None:
            room.move_possibilities(self.x, self.y)
            return False

        if type(loot) == Enemy:
            loot = loot.battle(self)

        for i in loot:
            if type(i) == Armor:
                self.armor.append(i)
            elif type(i) == Weapon:
                self.weapons.append(i)
            elif type(i) == Stuff:
                self.inventory.append(i)

        room.move_possibilities(self.x, self.y)
        return False

    def show_hud(self):
        print("HP: {0} / {1}\t".format(self.hp, self.max_hp),
              "Mana: {0} / {1}\t".format(self.mana, self.mana_max),
              "XP: {0}".format(self.xp))

        armor_list = []
        for i in self.armor:
            armor_list.append([i.name, i.defeat, i.durability, i.weight, i.price])
        weapon_list = []
        for i in self.weapons:
            weapon_list.append([i.name, i.damage, i.durability, i.speed, i.weight, i.price])
        stuff_list = []
        for i in self.inventory:
            stuff_list.append([i.name, i.extra_param, i.weight, i.price])

        print("\nArmor:")
        for i in armor_list:
            print(i)
        print("\nInventory:")
        for i in stuff_list:
            print(i)
        print("\nWeapons:")
        for i in weapon_list:
            print(i)
        print("\n")

    def reposition(self, room):
        if type(room) != Map:
            raise Exception("Wrong 'room' param")

        self.x = rand.randint(0, room.width - 1)
        self.y = rand.randint(0, room.height - 1)

# TODO: limit for inventory
