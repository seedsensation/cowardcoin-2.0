from gibberish import Gibberish
from random import choice,randint
from math import floor

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

        self.durability = randint(5,15)


        self.type = choice(["Weapon","Armor"])
        if self.type == "Weapon":

            self.damage = randint(4, 8)
            self.damage = floor(self.damage * (rarity / 10))

            self.AC = 0
            self.name = ""

            if rarity > 5:
                adjectives = ["Durable","Sharp","Bright","Flaming","Painful","Expensive"]
                self.adjective = choice(adjectives)
                self.name += self.adjective+" "
            else:
                self.adjective = ""
                self.name += "Common "

            if rarity == 20:
                chance = randint(1,20)
                if chance == 20:
                    self.name = "The Legendary Throngler"
                else:
                    gib = Gibberish()
                    name = gib.generate_word(end_vowel=True,vowel_consonant_repeats=2)
                    name = name.capitalize()
                    self.name = f"The Legendary {name}r"

            else:
                weapontypes = ["Axe", "Sword", "Spear", "Bow", "Mace", "Dagger", "Wand", "Wooden Stick"]
                self.weapontype = choice(weapontypes)

                self.name += f"{self.weapontype}"

                if rarity > 10:
                    origins = ["the Arcane","the Ancients","the Cosmos","the Stars","Flame","Ice","Poison"]
                    self.origin = choice(origins)
                    self.name += f" of {self.origin}"

            self.damagelower = floor(rarity/2)
            self.damagehigher = floor(rarity/2)*3

        else:

            self.name = ""
            self.AC = randint(2,5)
            self.AC = floor(self.AC*(rarity/10))
            self.damage = 0

            if rarity > 5:
                adjectives = ["Durable","Thorny","Blinding","Flaming","Expensive"]
                self.adjective = choice(adjectives)
                self.name += self.adjective+" "
            else:
                self.adjective = "Common"

            armortypes = ["Chestplate","Helmet","Leggings","Sleeves","Gauntlets"]
            self.armortype = choice(armortypes)


            self.name += f"{self.rarity} {self.armortype}"

        costlower = 25
        costupper = 50

        self.cost = randint(costlower,costupper)

        if self.adjective == "Expensive":
            self.cost = self.cost*1.5
        self.cost = floor(self.cost*(rarity/10))

        if self.adjective == "Durable":
            self.durability = floor(self.durability*1.5)

        if self.adjective == "Tough":
            self.AC = floor(self.AC*1.5)

        if self.adjective == "Sharp":
            self.damage = floor(self.damage*1.5)

    def Display(self):
        if self.type == "Weapon":
            displayattributes = ["name","cost","damage","durability","rarity"]
        else:
            displayattributes = ["name","cost","AC","durability","armortype","rarity"]
        output = ""
        for attribute in displayattributes:
            output += f"**{attribute.capitalize()}** - {getattr(self,attribute)}\n"

        return output



