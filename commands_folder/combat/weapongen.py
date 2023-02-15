from gibberish import Gibberish
from random import choice,randint

class item():
    def __init__(self,rarity):
        # rarity comes betweeon 1 and 20
        if rarity < 10:
            self.rarity = "Common"
        elif rarity < 14:
            self.rarity = "Rare"
        elif rarity < 17:
            self.rarity = "Super-Rare"
        elif rarity < 20:
            self.rarity = "Epic"
        elif rarity == 20:
            self.rarity = "Legendary"

        self.name = ""

        if rarity > 5:
            adjectives = ["Durable","Sharp","Bright","Flaming","Painful","Expensive"]
            self.adjective = choice(adjectives)
            self.name += self.adjective+" "
        else:
            self.adjective = ""
            self.name += "Common "

        if rarity == 20:
            gib = Gibberish()
            name = gib.generate_word(end_vowel=True,vowel_consonant_repeats=2)
            name = name.capitalize()
            self.name = f"The Legendary {name}r"
        else:
            weapontypes = ["Axe", "Sword", "Spear", "Bow", "Mace", "Dagger", "Wand", "Wooden Stick"]
            self.type = choice(weapontypes)

            self.name += f"{self.type}"

            if rarity > 10:
                origins = ["the Arcane","the Ancients","the Cosmos","the Stars","Flame","Ice","Poison"]
                self.origin = choice(origins)
                self.name += f" of {self.origin}"

        costlower = 25
        costupper = 100

        self.cost = randint(costlower,costupper)

        if self.adjective == "Expensive":
            self.cost = cost*1.5


class weapon(item):
    def __init__(self):
        weapontypes = ["Axe", "Sword", "Spear", "Bow", "Mace", "Dagger", "Wand", "Wooden Stick"]
        self.type = choice(weapontypes)


class armour(item):
    pass