from random import randint
from commands_folder.combat.collectorgen import ReadState,SaveState
from commands_folder.combat.monstergen import *
from commands_folder.combat.weapongen import item
from time import sleep
import os
import pickle
import asyncio
from global_context import context

class combat():
    def __init__(self):
        collectorlist = ReadState()
        levels = []
        for user in collectorlist:
            levels.append(collectorlist[user].level)
        maxlevel = max(levels)
        if maxlevel > 20:
            maxlevel = 20

        level = randint(1,maxlevel)
        self.round = 1
        self.enemy = monster(level)
        self.combatants = []
        self.downed = []

    def status(self):
        output = f"""
***TURN {self.round}***
    ENEMY: {self.enemy.name}
    ENEMY HEALTH: {self.enemy.healthbar(25)}      
    ENEMY AC: {self.enemy.AC}            
"""
        if self.enemy.status:
            output += f"    ENEMY STATUS EFFECTS: {self.enemy.status}"

        return output

    def attack(self,ctx):
        collectorlist = ReadState()
        print(self.combatants)
        attacker = collectorlist[ctx.author.id]
        output = ""
        if ctx.author.id not in self.combatants and ctx.author.id not in self.downed:
            self.combatants.append(ctx.author.id)

        if ctx.author.id in self.downed or collectorlist[ctx.author.id].HP <= 0:
            output = "You can't attack, you've already been downed! You will heal once the enemy leaves, or is downed itself."
            return output

        weapon = attacker.equipped["Weapon"]
        enemy = self.enemy
        if not weapon:
            weapon = item(0,"bare hands")
        output += f"You attack with your {weapon.name}.\n"

        basehitroll = randint(1,20)
        hitroll = basehitroll + floor(weapon.damage/2)
        output += f"You roll a {hitroll} ({basehitroll}+{floor(weapon.damage/2)}).\n"
        if hitroll >= enemy.AC and basehitroll != 20:
            output += f"HIT! You deal {weapon.damage}d3 damage.\n"
            damage = 0
            for x in range(0,weapon.damage):
                damage += randint(1,3)
            hit = True
        elif basehitroll == 20:
            damage = 3*weapon.damage
            output += f"CRITICAL HIT!!! You deal {damage} damage!"
            hit = True
        else:
            hit = False
        if hit:
            output+= f"The {enemy.name} takes {damage} damage!\n"
            enemy.HP -= damage
            if enemy.HP <= 0 and weapon.origin == "Poison":
                poisonroll = randint(1,5)
                if poisonroll == 5:
                    enemy.status = "Poisoned"


        else:
            output+= f"It's a miss!\n"

        if enemy.status:
            output += f"The {enemy.name} is {enemy.status}!\n"
            if enemy.status == "Poisoned":
                enemy.HP -= 3
                output += f"The {enemy.name} takes 3 damage from the poison!"

        if enemy.HP <= 0:
            output += self.end(ctx.author.id)
        else:
            output += enemy.attack(attacker)
            damage = randint(enemy.AttackLower,enemy.AttackHigher)
            basehitroll = randint(1,20)
            hitroll = (basehitroll+floor(damage/2))
            output += f"The {enemy.name} rolls a {hitroll} ({basehitroll}+{floor(damage / 2)}).\n"
            if hitroll >= attacker.AC:
                if basehitroll == 20:
                    output += "CRITICAL "
                    damage = damage*2
                output += f"HIT! It deals {damage} damage!\n"
                attacker.HP -= damage
                if attacker.HP <= 0:
                    attacker.HP = 0
                    output += f"{attacker.display_name} is down!\nThey can no longer receive rewards from this fight."
                    self.downed.append(attacker.id)
                    self.combatants.remove(attacker.id)
            else:
                output += f"It's a miss!"

        SaveState(collectorlist)
        return output

    def end(self,winner):
        collectorlist = ReadState()
        output = "***Collectors Win!***\n"
        individualXP = floor(self.enemy.XPGain / len(self.combatants))
        XPdiff = (len(self.combatants)*individualXP)
        if XPdiff:
            collectorlist[winner].XPGain(XPdiff)
        for collector in self.combatants:
            output += collectorlist[collector].XPGain(individualXP)
        self.itemreward = item(randint(1,min(ceil(self.enemy.CR*2),20)))
        output += f"The enemy drops a {self.itemreward.name}!\n"
        if len(self.combatants) > 1:
            output += f"The first person to type `!coin get` claims the item."
            SaveCombat(self)
            for collector in collectorlist.values():
                collector.HP = collector.maxHP

            SaveState(collectorlist)
        else:
            collectorlist[winner].inventory.append(self.itemreward)
            output += f"{collectorlist[winner].display_name} claims the item."
            for collector in collectorlist.values():
                collector.HP = collector.maxHP

            SaveState(collectorlist)





        return output


async def startcombat(ctx):
    collectorlist = ReadState()
    output = ""
    fight = combat()
    output += f"SURPRISE! A wild {fight.enemy.name} attacks!\n"
    output += f"{fight.enemy.healthbar(50)}\n"
    if os.path.exists("CombatState.bin"):
        os.remove("CombatState.bin")
    SaveCombat(fight)
    await ctx.send(output)
    await asyncio.sleep(context[7])
    state = await LoadCombat()
    if state.enemy.HP > 0:
        await ctx.send(f"The {fight.enemy.name} gets bored, and wanders off.")
        os.remove("CombatState.bin")
        for collector in collectorlist.values():
            collector.HP = collector.maxHP
        SaveState(collectorlist)

async def attack(ctx):
    collectorlist = ReadState()
    try:
        fight = await LoadCombat()
    except AttributeError as e:
        await ctx.send(e)
        return

    output = fight.attack(ctx)
    SaveCombat(fight)
    await ctx.send(output)

async def CombatState(ctx):
    try:
        fight = await LoadCombat()
    except AttributeError as e:
        await ctx.send(e)
        return
    output = fight.status()
    await ctx.send(output)


def SaveCombat(battle):
    with open("CombatState.bin","wb") as f:
        pickle.dump(battle, f)
    print(f"Saved State {battle}")

async def LoadCombat():
    collectorlist = ReadState()
    if os.path.exists("CombatState.bin"):
        with open("CombatState.bin", "rb") as f:
            battle = pickle.load(f)
        try:
            if battle.itemreward:
                return battle
        except AttributeError:
            if battle.enemy.HP <= 0:
                os.remove("CombatState.bin")
                raise AttributeError("There is no combat in progress.")

        return battle
    else:
        for collector in collectorlist.values():
            collector.HP = collector.maxHP
        SaveState(collectorlist)
        raise AttributeError("There is no combat in progress.")


