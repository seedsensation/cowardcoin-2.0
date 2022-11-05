import logging

from commands_folder.echo_file import *
from commands_folder.create_file import *
from commands_folder.get_file import *
from commands_folder.leaderboard_file import *
from commands_folder.help_file import *

from time import *
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

async def debug(ctx):
    try:
        debugtemp = context[1].name
    except:
        debugtemp = ""
    debugcontext = context
    debugcontext[1] = debugtemp

    await ctx.send(str(context))

commandslist = {"echo":echo_command,"get":get_command,"leaderboard":leaderboard_command,"debug":debug,"help":help_coin}

@bot.command()
async def coin(ctx,*args):
    if args[0] in commandslist:
        if args[0].lower() == "echo" or (args[0].lower() == "help"):
            print("Hi")
            await commandslist[args[0]](ctx,args)
    else:
        print("Invalid command by "+ctx.author.display_name+" - "+args[0])

bot.run(TOKEN)
