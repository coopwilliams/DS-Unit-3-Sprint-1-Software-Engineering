from __future__ import print_function
import random

class Product():
    """ Class for ACME product"""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name=name
        self.price=price
        self.weight=weight
        self.flammability=flammability
        self.identifier=random.randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif (ratio >= 0.5) & (ratio < 1):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        ratio = self.flammability * self.weight
        if ratio < 10:
            return "...fizzle."
        elif (ratio >= 10) & (ratio < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    """ Boxing Glove. Subclass of ACME Products """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "... it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif (self.weight >= 5) & (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
