from math import floor
from global_context import bot

class collector():
    def __init__(self,ID):
        self.maxHP = 10
        self.XPtoLevel = 10
        self.XP = 0
        self.level = 1
        self.AC = 10
        self.inventory = []
        self.equipped = dict.fromkeys(["Head","Chest","Legs","Arms","Hands"])
        self.ID = ID

    def XPGain(self,XP):
        self.XP += XP
        if self.XP >= self.XPtoLevel:
            self.XP -= self.XPtoLevel
            self.level += 1
            self.AC += 1
            self.XPtoLevel = floor(self.XPtoLevel*1.5)

def CheckList():
    try:
        if collectorlist:
            pass
    except (KeyError,UnboundLocalError):
        collectorlist = []

    for guild in bot.guilds:
        for member in guild.members:
            match = False
            for collectoritem in collectorlist:
                if collectoritem.ID == member.ID:
                    match = True
                    break

            if not match:
                collectorlist.append(collector(member.id))

    return collectorlist