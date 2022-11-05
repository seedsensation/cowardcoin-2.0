import logging
import asyncio

from time import *
from global_context import *
from commands import *
from commands_folder.check_task import *

if not os.path.exists(strftime("logs\\%Y.%m.%d\\")):
    os.makedirs(strftime("logs\\%Y.%m.%d\\"))  # make a folder if it doesn't already exist with the name of today's date
logtime = strftime("%Y.%m.%d\\%H.%M.%S")
file = open("logs\\%s.txt" % logtime, "w")
file.close()
logging.basicConfig(filename="logs\\%s.txt" % logtime,
                    level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')  # activates logging


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await file_check()
    await bot.change_presence(activity=discord.Game(name="the economy 😎"))
    await create_coin()

    loop = asyncio.get_event_loop()
    task = loop.create_task(check())


@bot.command()
async def echo(ctx, arg):  # ctx = context of command, arg = second word
    await echo_send(ctx, arg)  # reply to the original message echoing back the second word


# TO-DO LIST
# 1. CREATE COIN FUNCTION

@bot.command()
async def create(ctx):
    await create_send(ctx)


# 2. GET COIN FUNCTION

@bot.command()
async def get(ctx):
    await get_send(ctx)


@bot.command()
async def debug(ctx):
    try:
        debugtemp = context[1].name
    except:
        debugtemp = ""
    debugcontext = context
    debugcontext[1] = debugtemp

    await ctx.send(str(context))

@bot.command()
async def leaderboard(ctx):
    await leaderboard_send(ctx)


bot.run(TOKEN)
