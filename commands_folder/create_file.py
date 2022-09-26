from global_context import *
import time
from random import randint
import asyncio
async def create_command(ctx):
    if ctx == "":
        print(CHANNEL)
        ctx = bot.get_channel(int(CHANNEL))
        print(ctx)
    delay = float(randint(5,10))
    await ctx.send("The coin will appear in the next 5-10 seconds.")
    print("Executing Coin Creation in "+str(delay)+" seconds.")
    await asyncio.sleep(delay)
    await create_coin(ctx)

async def create_coin(ctx):
    await ctx.send("COIN ALERT! COIN ALERT!")
    print("Created Coin")
    context[0] = True
