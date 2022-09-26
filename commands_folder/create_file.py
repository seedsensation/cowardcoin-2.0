from global_context import *
import time
from random import randint
import asyncio
async def create_command(ctx):
    if ctx == "":
        ctx = bot.get_channel(int(CHANNEL))
    delay = float(randint(5,10))
    await ctx.send("The coin will appear in the next 5-10 seconds.")
    print("Executing Coin Creation in "+str(delay)+" seconds.")
    await asyncio.sleep(delay)
    await create_coin(ctx)

async def create_coin(ctx):
    context[1] = await ctx.send("COIN ALERT! COIN ALERT!")
    print("Created Coin")
    context[0] = True
    await asyncio.sleep(30)
    if context[0]:
        await context[1].delete()
