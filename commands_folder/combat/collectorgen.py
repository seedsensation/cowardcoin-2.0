from math import floor
from global_context import bot
import pickle
import os
import discord
import time


class collector():
    global defaultattributes
    defaultattributes = {"maxHP": 10,
                         "HP": 10,
                         "xptolevel": 10,
                         "xp": 0,
                         "level": 1,
                         "AC": 10,
                         "test":1,
                         "damage":1,
                         "bonusdamage":0,
                         "bonusAC":0,
                         }

    def __init__(self,user):
        for attr in defaultattributes:
            setattr(self,attr,defaultattributes[attr])
        self.id = user.id
        self.display_name = user.display_name
        self.inventory = []
        self.equipped = dict.fromkeys(["Head","Chest","Legs","Arms","Hands","Weapon"])

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
        output = ""
        counter = 0
        for item in self.inventory:
            counter += 1
            output += f"{counter}. {item.Display()}\n"
        return output

    def statshow(self):
        output = f"""
        ***Your Current Stats***
        Level: {self.level}
        XP: {self.xp}/{self.xptolevel}
        HP: {self.HP}/{self.maxHP} 
        AC: {self.AC} (of which is from armor: {self.bonusAC})
        Damage: {self.damage} (of which is from weapons: {self.bonusdamage})
        """
        return output

# "maxHP": 10,
 # "HP": 10,
 # "xptolevel": 10,
 # "xp": 0,
 # "level": 1,
 # "AC": 10,
 # "test":1,
 # "damage":1,
 # "bonusdamage":0,
 # "bonusAC":0,
def CheckList(collectorlist):
    try:
        if collectorlist:
            pass
        else:
            collectorlist = {}
    except (KeyError,UnboundLocalError):
        collectorlist = {}


    for guild in bot.guilds:
        for member in guild.members:
            print(member.id)
            match = False
            if member.id in list(collectorlist.keys()):
                print(f"Collector {member.display_name} already exists")
                match = True

            if not match:
                print(f"Creating object for collector {member.display_name}")
                collectorlist[member.id] = collector(member)

    for user in collectorlist.values():
        print(user.display_name)
        user.UpdateStats()
        print(user.inventory)

    SaveState(collectorlist)

    return collectorlist

def SaveState(collectorlist):
    with open("GameState.bin","wb") as f:
        pickle.dump(collectorlist, f)
    print(f"Saved State {collectorlist}")

def ReadState():
    with open("GameState.bin","rb") as f:
        collectorlist = pickle.load(f)
    return collectorlist



async def InventoryDisplay(ctx,args):
    collectorlist = ReadState()
    user = collectorlist[ctx.author.id]
    output = ""

    if len(args) == 1:


        equippedcount = 0
        tempoutput = ""
        for slot in user.equipped:
            if user.equipped[slot]:
                equippedcount += 1
                tempoutput += f"{slot} - **{user.equipped[slot].name}**\n"
        if equippedcount:
            s = "s" if equippedcount != 1 else ""

            output += f"You have {equippedcount} item{s} equipped:\n"
            output += tempoutput+"\n\n"

        s = "s" if len(user.inventory) != 1 else ""
        output += f"Your inventory has {len(user.inventory)} item{s}.\n"




        print(user.inventory)
        for item in user.inventory:
            print(item.name)
        output += user.inventoryshow(ctx)
        if len(user.inventory) == 0:
            output = "Your inventory is empty... Try heading to the market, or fighting some monsters!"
        if len(output) < 2000:
            await ctx.send(output)
        else:
            messages = []
            lines = output.splitlines()
            newoutput = ""
            for line in lines:
                if len(newoutput+line+"\n") >= 2000:
                    print(len(newoutput),len(line))
                    print(f"Appending '{line}' to 'messages'.")
                    messages.append(newoutput)
                    while newoutput not in messages:
                        messages.append(newoutput)
                    print(messages[-1])
                    newoutput = line+"\n"
                else:
                    newoutput += line+"\n"
            for message in messages:
                await ctx.send(message)
            print(messages)
### THE ABOVE CODE BREAKS IF YOU HAVE MORE THAN ~40 ITEMS. I HAVE NO IDEA WHY. COME BACK HERE IF IT STOPS WORKING FOR ANYONE IN THE SERVER

    else:
        if len(args) == 2:
            try:
                item = await InventoryNumberCheck(ctx,args[1])
            except ValueError as e:
                await ctx.send(str(e))
                return
            if item:
                print(item.name)
                await ctx.send(item.Display())
        else:
            if args[1] == "give":
                if ctx.message.mentions:
                    recipient = ctx.message.mentions[0]
                    recipientobj = collectorlist[recipient.id]
                    found = False
                    for cmd in args:
                        try:
                            item = await InventoryNumberCheck(ctx,cmd)
                        except ValueError:
                            continue
                        found = True
                        break

                    if not found:
                        await ctx.send("Item not found...")
                    else:
                        if item in user.equipped.values():
                            await ctx.send("You can't give out items that you have equipped! Try equipping something else first.")
                            return
                        print(user.inventory)
                        print(item)
                        print(item.name)
                        success = False
                        for x in user.inventory:
                            if item == x:
                                item = x
                                success = True
                                break

                        if success:

                            user.inventory.remove(item)
                            recipientobj.inventory.append(item)
                            await ctx.send(f"Transferred your {item.name} to {recipient.display_name}!")
                        else:
                            print("error.")
                else:
                    await ctx.send("Try @-mentioning someone in your message.")
            else:
                print(f"Unrecognised command {args[1]}")

    SaveState(collectorlist)

async def equip(ctx,args):
    collectorlist = ReadState()
    user = collectorlist[ctx.author.id]

    output = ""
    if len(args) == 1:
        equippedcount = 0
        tempoutput = ""
        for slot in user.equipped:
            if user.equipped[slot]:
                equippedcount += 1
                tempoutput += f"{slot} - **{user.equipped[slot].name}**\n"
        if equippedcount:
            s = "s" if equippedcount != 1 else ""

            output += f"You have {equippedcount} item{s} equipped:\n"
            output += tempoutput + "\n\n"
        else:
            output += "Type '!coin inventory' to view what items you have in your inventory, and then  '!coin equip 1' to equip the item in Slot 1."
    else:
        for cmd in args:
            try:
                item = await InventoryNumberCheck(ctx, cmd)
            except ValueError:
                continue
            found = True
            break
        if not found:
            output = ("Item not found... Make sure an item number is somewhere in your message.")
        else:
            if item.type == "Weapon":
                slot = "Weapon"
            else:
                types = {"Chestplate":"Chest","Helmet":"Head","Leggings":"Legs","Sleeves":"Arms","Gauntlets":"Hands"}
                if item.armortype in types:
                    slot = types[item.armortype]
                else:
                    output = ("An unknown error occurred equipping this item. Please contact Mercury for assistance.")

            if slot:
                if user.equipped[slot] == item:
                    output = "You already have that item equipped!"
                if user.equipped[slot]:
                    output = (f"You swap your {user.equipped[slot].name} for your {item.name}.")
                    if slot == "Weapon":
                        user.damage -= user.bonusdamage
                    else:
                        user.AC -= user.bonusAC
                else:
                    output = (f"You equip your {item.name}.")
                    if slot == "Weapon":
                        user.bonusdamage = item.damage
                        user.damage += user.bonusdamage
                    else:
                        user.bonusAC = item.AC
                        user.AC += user.bonusAC
                user.equipped[slot] = item
            else:
                output = ("An unknown error occurred equipping this item. Please contact Mercury for assistance.")


# ["Head","Chest","Legs","Arms","Hands","Weapon"]




    SaveState(collectorlist)
    await ctx.send(output)



async def InventoryNumberCheck(ctx,itemno):
    collectorlist = ReadState()

    user = collectorlist[ctx.author.id]

    try:
        choice = int(itemno) if not float(itemno) % 1 else ValueError
    except ValueError:
        raise ValueError("Inventory item must be a whole number")

    choice -= 1
    if (choice) <= len(user.inventory):
        return user.inventory[choice]
    else:
        raise ValueError("Item choice must be within range.")

async def status(ctx):
    collectorlist = ReadState()
    user = collectorlist[ctx.author.id]
    await ctx.send(user.statshow())

global collectorlist

if os.path.isfile("GameState.bin"):
    collectorlist = ReadState()
    print(collectorlist)
    print(collectorlist[431047023689596928].display_name)
    collectorlist[431047023689596928].UpdateStats()