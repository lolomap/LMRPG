import items.item as item
from EXTRA_FILES.extra_funcs import enum
import random as rand


class Stuff(item.Item):
    # ***Constants***
    POISION_NAMES = ("large heal", "small heal")
    MONEY_NAME = ("coin", "gem")

    STUFF_TYPES = ("poision", "money")

    STUFF_PARAMS = {"poision_lh": {"extra_param": 70, "weight": 3, "price": 30},
                    "poision_sh": {"extra_param": 20, "weight": 2, "price": 20},
                    "money": {"weight": 0.2, "min_price": 1, "max_price": 100}}

    def __init__(self):
        item.Item.__init__(self)
        self.item_type = rand.choice(self.STUFF_TYPES)
        if self.item_type == "poision":
            self.name = rand.choice(self.POISION_NAMES)
            if self.name == "large heal":
                self.extra_param = self.STUFF_PARAMS["poision_lh"]["extra_param"]
                self.weight = self.STUFF_PARAMS["poision_lh"]["weight"]
                self.price = self.STUFF_PARAMS["poision_lh"]["price"]
            elif self.name == "small heal":
                self.extra_param = self.STUFF_PARAMS["poision_sh"]["extra_param"]
                self.weight = self.STUFF_PARAMS["poision_sh"]["weight"]
                self.price = self.STUFF_PARAMS["poision_sh"]["price"]
        elif self.item_type == "money":
            self.name = rand.choice(self.MONEY_NAME)
            self.weight = self.STUFF_PARAMS["money"]["weight"]
            self.extra_param = None
            self.price = rand.randint(self.STUFF_PARAMS["money"]["min_price"], self.STUFF_PARAMS["money"]["max_price"])
