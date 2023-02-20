from math import floor
from global_context import bot
import pickle

class collector():
    global defaultattributes
    defaultattributes = {"maxHP": 10,
                         "HP": 10,
                         "xptolevel": 10,
                         "xp": 0,
                         "level": 1,
                         "AC": 10,
                         "inventory": [],
                         "equipped": dict.fromkeys(["Head", "Chest", "Legs", "Arms", "Hands", "Weapon"]),
                         "test":1
                         }

    def __init__(self,user):
        for attr in defaultattributes:
            setattr(self,attr,defaultattributes[attr])
        self.id = user.id
        self.display_name = user.display_name

    def XPGain(self,XP):
        self.XP += XP
        if self.XP >= self.XPtoLevel:
            self.XP -= self.XPtoLevel
            self.level += 1
            self.AC += 1
            self.XPtoLevel = floor(self.XPtoLevel*1.5)

    def UpdateStats(self):
        attrlist = [a for a in dir(self) if not a.startswith("__")]
        for attribute in defaultattributes:
            if attribute not in attrlist:
                setattr(self,attribute,defaultattributes[attribute])

    def inventoryshow(self,ctx):
        global collectorlist
        output = "1. "
        counter = 0
        for item in self.inventory:
            counter += 1
            output += item.Display()
        return output

def CheckList():
    try:
        if collectorlist:
            pass
    except (KeyError,UnboundLocalError):
        collectorlist = {}

    for guild in bot.guilds:
        for member in guild.members:
            print(member.id)
            match = False
            if member.id in collectorlist:
                print("Collector already exists")

            if not match:
                print(f"Creating object for collector {member.id}")
                collectorlist[member.id] = collector(member)

    for user in collectorlist.values():
        print(user.display_name)
        user.UpdateStats()
        print(user.test)

    SaveState(collectorlist)

    return collectorlist

def SaveState(collectorlist):
    with open("GameState.bin","wb") as f:
        pickle.dump(collectorlist, f)

def ReadState():
    with open("GameState.bin","rb") as f:
        collectorlist = pickle.load(f)
    return collectorlist

async def equip(ctx,args):
    global collectorlist
    output = ""
    if len(args) == 1:
        output += "Type '!coin inventory' to view what items you have in your inventory, and then  '!coin equip 1' to equip the item in Slot 1."
    else:
        user = collectorlist(ctx.author.id)


    await ctx.send(output)

