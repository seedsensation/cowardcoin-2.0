from global_context import *
from pathlib import *
from random import randint
import asyncio
async def create_command(ctx):
    context[6] = False
    if ctx == "":
        ctx = bot.get_channel(int(CHANNEL))
    context[3] = float(randint(context[4],context[5]))
    print("Executing Coin Creation in "+str(context[3])+" seconds.")
    await asyncio.sleep(context[3])
    await create_coin(ctx)

async def create_coin(ctx):
    with open(Path("files/images/gold.gif","rb")) as f:
        picture = discord.File(f)
    context[1] = await ctx.send("A new coin has appeared!\nType !coin get to claim it!",file=picture)
    print("Created Coin")
    context[0] = True
    await asyncio.sleep(context[7])
    if context[0]:
        await context[1].delete()
        print("Image file deleted, new coin ready")
        await ctx.send("The coin escaped...")
        context[6] = True
        context[0] = False
    else:
        print("New coin ready")
