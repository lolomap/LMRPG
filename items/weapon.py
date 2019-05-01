import items.item as item
import random as rand


class Weapon(item.Item):
    # ***Constants***
    JOKE_NAMES = ("fork", "wooden stick")
    SWORD_NAMES = ("steel sword", "gold_sword")
    MACE_NAMES = ("steel mace", "spiked mace")
    BOW_NAMES = ("bow", "crossbow")
    SMALL_NAMES = ("knife", "nail puller")
    WEAPON_TYPES = ("sword", "mace", "bow", "joke", "small")

    WEAPON_PARAMS = {"sword": {"min_damage": 10, "max_damage": 30, "min_durability": 6, "max_durability": 12,
                               "speed": 0.7, "armor_dp_prob": 0.2, "weight": 15, "min_price": 13, "max_price": 30},
                     "mace": {"min_damage": 23, "max_damage": 46, "min_durability": 6, "max_durability": 10,
                              "speed": 0.4, "armor_dp_prob": 0.5, "weight": 30, "min_price": 17, "max_price": 56},
                     "bow": {"min_damage": 10, "max_damage": 15, "min_durability": 10, "max_durability": 14,
                             "speed": 1, "armor_dp_prob": 0.05, "weight": 5, "min_price": 17, "max_price": 21},
                     "joke": {"min_damage": 1, "max_damage": 3, "min_durability": 2, "max_durability": 5,
                              "speed": 0.8, "armor_dp_prob": 0.007, "weight": 2, "min_price": 0, "max_price": 0},
                     "small": {"min_damage": 6, "max_damage": 15, "min_durability": 4, "max_durability": 8,
                               "speed": 0.8, "armor_dp_prob": 0.07, "weight": 4, "min_price": 10, "max_price": 21}
                     }

    def __init__(self, damage=None, durability=None, fast=None):
        item.Item.__init__(self)

        self.item_type = rand.choice(self.WEAPON_TYPES)
        if self.item_type == "sword":
            self.name = rand.choice(self.SWORD_NAMES)
            self.damage = rand.randint(self.WEAPON_PARAMS["sword"]["min_damage"],
                                       self.WEAPON_PARAMS["sword"]["max_damage"])
            self.durability = rand.randint(self.WEAPON_PARAMS["sword"]["min_durability"],
                                           self.WEAPON_PARAMS["sword"]["max_durability"])
            self.speed = self.WEAPON_PARAMS["sword"]["speed"]
            self.armor_dp_prob = self.WEAPON_PARAMS["sword"]["armor_dp_prob"]
            self.weight = self.WEAPON_PARAMS["sword"]["weight"]
            self.price = rand.randint(self.WEAPON_PARAMS["sword"]["min_price"],
                                      self.WEAPON_PARAMS["sword"]["max_price"])
        elif self.item_type == "mace":
            self.name = rand.choice(self.MACE_NAMES)
            self.damage = rand.randint(self.WEAPON_PARAMS["mace"]["min_damage"],
                                       self.WEAPON_PARAMS["mace"]["max_damage"])
            self.durability = rand.randint(self.WEAPON_PARAMS["mace"]["min_durability"],
                                           self.WEAPON_PARAMS["mace"]["max_durability"])
            self.speed = self.WEAPON_PARAMS["mace"]["speed"]
            self.armor_dp_prob = self.WEAPON_PARAMS["mace"]["armor_dp_prob"]
            self.weight = self.WEAPON_PARAMS["mace"]["weight"]
            self.price = rand.randint(self.WEAPON_PARAMS["mace"]["min_price"],
                                      self.WEAPON_PARAMS["mace"]["max_price"])
        elif self.item_type == "bow":
            self.name = rand.choice(self.BOW_NAMES)
            self.damage = rand.randint(self.WEAPON_PARAMS["bow"]["min_damage"],
                                       self.WEAPON_PARAMS["bow"]["max_damage"])
            self.durability = rand.randint(self.WEAPON_PARAMS["bow"]["min_durability"],
                                           self.WEAPON_PARAMS["bow"]["max_durability"])
            self.speed = self.WEAPON_PARAMS["bow"]["speed"]
            self.armor_dp_prob = self.WEAPON_PARAMS["bow"]["armor_dp_prob"]
            self.weight = self.WEAPON_PARAMS["bow"]["weight"]
            self.price = rand.randint(self.WEAPON_PARAMS["bow"]["min_price"],
                                      self.WEAPON_PARAMS["bow"]["max_price"])
        elif self.item_type == "joke":
            self.name = rand.choice(self.JOKE_NAMES)
            self.damage = rand.randint(self.WEAPON_PARAMS["joke"]["min_damage"],
                                       self.WEAPON_PARAMS["joke"]["max_damage"])
            self.durability = rand.randint(self.WEAPON_PARAMS["joke"]["min_durability"],
                                           self.WEAPON_PARAMS["joke"]["max_durability"])
            self.speed = self.WEAPON_PARAMS["joke"]["speed"]
            self.armor_dp_prob = self.WEAPON_PARAMS["joke"]["armor_dp_prob"]
            self.weight = self.WEAPON_PARAMS["joke"]["weight"]
            self.price = rand.randint(self.WEAPON_PARAMS["joke"]["min_price"],
                                      self.WEAPON_PARAMS["joke"]["max_price"])
        elif self.item_type == "small":
            self.name = rand.choice(self.SMALL_NAMES)
            self.damage = rand.randint(self.WEAPON_PARAMS["small"]["min_damage"],
                                       self.WEAPON_PARAMS["small"]["max_damage"])
            self.durability = rand.randint(self.WEAPON_PARAMS["small"]["min_durability"],
                                           self.WEAPON_PARAMS["small"]["max_durability"])
            self.speed = self.WEAPON_PARAMS["small"]["speed"]
            self.armor_dp_prob = self.WEAPON_PARAMS["small"]["armor_dp_prob"]
            self.weight = self.WEAPON_PARAMS["small"]["weight"]
            self.price = rand.randint(self.WEAPON_PARAMS["small"]["min_price"],
                                      self.WEAPON_PARAMS["small"]["max_price"])

        if damage is not None:
            self.damage = damage
        if durability is not None:
            self.durability = durability
        if fast:
            self.speed = 99
