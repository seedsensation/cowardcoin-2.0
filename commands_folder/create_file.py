from global_context import *
from pathlib import *
from random import randint
import asyncio
from commands_folder.combat.battle import startcombat
async def create_command(ctx):
    context[6] = False
    if ctx == "":
        ctx = bot.get_channel(int(CHANNEL))
    context[3] = float(randint(context[4],context[5]))
    print("Executing Coin Creation in "+str(context[3])+" seconds.")
    await asyncio.sleep(context[3])
    await create_coin(ctx)

async def create_coin(ctx):
    combatdecider = randint(1,10)
    if combatdecider == 10:
        await startcombat(ctx)
    else:
        # generate coin variant
        variant = randint(0,100)
        varlist = context[13]
        if variant <= varlist[0]:
            context[12] = 1
        elif variant <= varlist[1]:
            context[12] = 2
        elif variant <= varlist[2]:
            context[12] = 3
        else:
            context[12] = 4

        with open(Path(f"files/images/{coinrarities[context[12]][2]}.gif"),"rb") as f:
            picture = discord.File(f)
        context[1] = await ctx.send(f"A new {coinrarities[context[12]][0]} coin has appeared!\nType `!coin get` to claim it!",file=picture)
        print("Created Coin")
        context[0] = True
        await asyncio.sleep(context[7])
        if context[0]:
            await context[1].delete()
            print("Image file deleted, new coin ready")
            escapemsg = await ctx.send(f"{coinrarities[context[12]][1]} The coin escaped...")
            context[6] = True
            context[0] = False
            if context[12] != 4:
                await asyncio.sleep(context[7])
                await escapemsg.delete()
                print("'Coin Escaped' message expired.")

        else:
            print("New coin ready")


async def view_coin(ctx):
    with open(Path("files/images/gold.gif"),"rb") as f:
        picture = discord.File(f)
    await ctx.send("A coin, for your viewing pleasure.",file=picture)
    await ctx.delete()
