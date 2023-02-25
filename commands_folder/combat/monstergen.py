from random import randint,choice
from math import floor,ceil

class monster():
    def __init__(self,seed):
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

        HPLower = 5
        HPHigher = 15

        HPLower = HPLower*seed
        HPHigher = HPHigher*seed

        self.AC = 10+seed

        self.MaxHP = randint(HPLower,HPHigher)
        self.HP = self.MaxHP

        self.AttackLower = seed
        self.AttackHigher = 5*seed



        self.XPGain = randint(ceil(seed/10*HPLower),ceil(seed/10*HPHigher))

        self.status = ""

    def attack(self,attacker):
        if self.ranged:
            attacktype = "fires"
        else:
            attacktype = "swings"


        output = (f"The {self.name} {attacktype}with its {self.weapon} at {attacker.display_name}!\n")

        return output
    
    def healthbar(self,percent):
        output = "["        


        hp = (self.HP/self.MaxHP)*percent

        for x in range(1,percent):
            if hp > 0:
                hp -= 1
                output += "▓"
            else:
                output += "░"

        output += f"] - {self.HP}/{self.MaxHP}"
        return output

