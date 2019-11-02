"""My responses for part one of unit 3 module 1 sprint challenge"""


class Product:
    """
    General input for a Product
    """
    from random import randint
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=(randint(1000000, 9999999))):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        price_by_weight = self.price / self.weight
        if price_by_weight < 0.5:
            return "Not so stealable..."
        elif (price_by_weight >= .05) & (price_by_weight < 1.0):
            return "Kinda stealable."
        else: #price_by_weight >= 1.0:
            return "Very stealable!"


    def explode(self):
        danger = self.flammability * self.weight
        if danger < 10:
            return  "...fizzle."
        elif (danger >= 10) & (danger < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):
    """subclass of Product called BoxingGlove"""

    from random import randint
    def __int__(self, name, price=10, weight=10, flammability=0.5, idenfifier=(randint(1000000, 9999999))):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        pain = self.weight
        if pain < 5:
            return  "That tickles."
        elif (pain >= 5) & (pain < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
