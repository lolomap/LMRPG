import items.item as item
import random as rand


class Armor(item.Item):
    # ***Constants***
    HELMET_NAMES = ("steel helmet", "leather helmet")
    CUIRASS_NAMES = ("chain mail", "steel cuirass", "leather cuirass")
    ARMOR_TYPES = ("helmet", "cuirass")

    ARMOR_PARAMS = {"steel helmet": {"defeat": 0.3, "durability": 10, "weight": 5, "price": 30},
                    "leather helmet": {"defeat": 0.2, "durability": 5, "weight": 2, "price": 10},
                    "chain mail": {"defeat": 0.5, "durability": 23, "weight": 17, "price": 75},
                    "steel cuirass": {"defeat": 0.75, "durability": 34, "weight": 34, "price": 140},
                    "leather cuirass": {"defeat": 0.3, "durability": 12, "weight": 12, "price": 20}}

    def __init__(self, durability=None, defeat=None):
        item.Item.__init__(self)

        self.item_type = rand.choice(self.ARMOR_TYPES)
        if self.item_type == "helmet":
            self.name = rand.choice(self.HELMET_NAMES)
            if self.name == "steel helmet":
                self.defeat = self.ARMOR_PARAMS["steel helmet"]["defeat"]
                self.durability = self.ARMOR_PARAMS["steel helmet"]["durability"]
                self.weight = self.ARMOR_PARAMS["steel helmet"]["weight"]
                self.price = self.ARMOR_PARAMS["steel helmet"]["price"]
            elif self.name == "leather helmet":
                self.defeat = self.ARMOR_PARAMS["leather helmet"]["defeat"]
                self.durability = self.ARMOR_PARAMS["leather helmet"]["durability"]
                self.weight = self.ARMOR_PARAMS["leather helmet"]["weight"]
                self.price = self.ARMOR_PARAMS["leather helmet"]["price"]
        elif self.item_type == "cuirass":
            self.name = rand.choice(self.CUIRASS_NAMES)
            if self.name == "chain mail":
                self.defeat = self.ARMOR_PARAMS["chain mail"]["defeat"]
                self.durability = self.ARMOR_PARAMS["chain mail"]["durability"]
                self.weight = self.ARMOR_PARAMS["chain mail"]["weight"]
                self.price = self.ARMOR_PARAMS["chain mail"]["price"]
            elif self.name == "steel cuirass":
                self.defeat = self.ARMOR_PARAMS["steel cuirass"]["defeat"]
                self.durability = self.ARMOR_PARAMS["steel cuirass"]["durability"]
                self.weight = self.ARMOR_PARAMS["steel cuirass"]["weight"]
                self.price = self.ARMOR_PARAMS["steel cuirass"]["price"]
            elif self.name == "leather cuirass":
                self.defeat = self.ARMOR_PARAMS["leather cuirass"]["defeat"]
                self.durability = self.ARMOR_PARAMS["leather cuirass"]["durability"]
                self.weight = self.ARMOR_PARAMS["leather cuirass"]["weight"]
                self.price = self.ARMOR_PARAMS["leather cuirass"]["price"]

        if durability is not None:
            self.durability = durability
        if defeat is not None:
            self.defeat = defeat
