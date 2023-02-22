from random import randint,choice
from math import floor

class monster():
    def __init__(self):
        seed = randint(1,20)
        self.CR = seed
        self.difficulty = floor(seed/4)

        monsternames = {
            "town":{"Town Guard":"Spear","Villager":"Dagger","Peasant":"Pitchfork"},
            "wildlife":{"Wild Boar":"Claws","Pack of Wolves":"Teeth","Shark":"Teeth"},
            "spellcaster":{"Spellcaster":"Wand","Elemental Spellcaster":"Wand","Mage":"Staff","Spellslinger":"Wand",},
            "gunslinger":{"Gunslinger":"Pistol","Cowboy":"Pistol","Sniper":"Rifle"},
            "supernatural":{"Beholder":"Eye Beam","Dragon":"Breath"},
            "divinity":{"Fragment of a Forgotten God":"Sight","Lich":"Staff"}
        }

        self.tag = list(monsternames.keys())[floor(seed/4)]

        if self.tag == "town" or self.tag == "wildlife":
            self.ranged = False
        else:
            self.ranged = True

        type = choice(list(monsternames[self.tag].keys()))

        self.weapon = monsternames[self.tag][type]

        if "elemental" in type.lower():
            elements = ["Fire","Light","Shadow","Water","Earth","Air"]
            self.element = choice(elements)
        else:
            self.element = False

        self.name = ""

        if self.element:
            self.name += f"{self.element} "

        self.name += type

        print(self.name)

        HPLower = 25
        HPHigher = 50

        HPLower = floor(HPLower*(seed/10))*25
        HPHigher = floor(HPHigher*(seed/10))



        self.MaxHP = randint(HPLower,HPHigher)
        self.HP = self.MaxHP

        self.XPGain = randint(floor(seed/10*HPLower),floor(seed/10*HPHigher))

    def attack(self,ctx):
        if self.ranged:
            attacktype = "fires"
        else:
            attacktype = "swings"


        ctx.send(f"The {self.name} {attacktype} at {ctx.author.display_name} with its {self.weapon}!")
    
    def healthbar(self):
        output = "["        

        hp = (self.HP/self.MaxHP)*50

        for x in range(1,50):
            if hp > 0:
                hp -= 1
                output += "▓"
            else:
                output += "░"
        output += f"] - {self.HP}/{self.MaxHP}"
        return output

