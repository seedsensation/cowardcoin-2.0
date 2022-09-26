from global_context import *
import time
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
    context[1] = await ctx.send("COIN ALERT! COIN ALERT!")
    print("Created Coin")
    context[0] = True
    await asyncio.sleep(30)
    if context[0]:
        await context[1].delete()
        print("Image file deleted, new coin ready")
        context[6] = True
    else:
        print("New coin ready")
