import logging

from commands_folder.create_file import *
from commands_folder.get_file import *
from commands_folder.leaderboard_file import *
from commands_folder.help_file import *
from commands_folder.give_file import *
from commands_folder.shop_file import *
from commands_folder.elections import *
from commands_folder.combat.weapongen import item
from random import randint
from time import *
from commands import *
from commands_folder.check_task import *
from pathlib import *
from discord.utils import get
from commands_folder.combat.collectorgen import *




if not os.path.exists(Path(strftime("logs/%Y.%m.%d/"))):
    os.makedirs(Path(strftime("logs/%Y.%m.%d/")))  # make a folder if it doesn't already exist with the name of today's date
logtime = strftime("%Y.%m.%d/%H.%M.%S")
file = open(Path("logs/%s.txt" % logtime), "w")
file.close()
logging.basicConfig(filename=Path("logs/%s.txt" % logtime),
                    level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')  # activates logging


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await file_check()
    await bot.change_presence(activity=discord.Game(name="the economy 😎"))
    print(CHANNEL)
    coinchannel = bot.get_channel(int(CHANNEL))
    await coinchannel.send("Restarted successfully!")
    print("Restarted successfully")
    global collectorlist
    try:
        collectorlist = CheckList(collectorlist)
    except:
        collectorlist = CheckList(False)
    print(collectorlist)

    newitem = item(randint(1, 20))
    collectorlist[431047023689596928].inventory.append(newitem)
    SaveState(collectorlist)



    collector1 = collectorlist[431047023689596928]

    print(f"ID: {collector1.id}\nAC: {collector1.AC}\nName: {collector1.display_name}\nInventory: {collector1.inventory}")

    await create_coin()




    loop = asyncio.get_event_loop()
    task = loop.create_task(check())

async def debug(ctx,arg):
    check_role = get(ctx.guild.roles, name="admins")
    if check_role not in ctx.author.roles and context[14]:
        await ctx.send("Admins only... sorry :(")
    elif context[14]:
        if len(arg) == 1:
            await ctx.send(str(context))
        else:
            exec(arg[1])

    else:
        await ctx.send("Currently not in maintenance mode")

async def echo_command(ctx,args):
    await ctx.send(args)

async def maintenancemode(ctx):
    check_role = get(ctx.guild.roles, name="admins")
    if check_role not in ctx.author.roles:
        await ctx.send("Admins only... sorry :(")
    else:
        context[14] = 1-(context[14])


commandslist = {"echo":[1,echo_command],"get":[0,get_command],"leaderboard":[1,leaderboard_command],"debug":[1,debug],"help":[1,help_coin],"count":[0,count_coin],"give":[1,give_command],"coin":[0,view_coin],"shop":[1,shop_command],"maintenance":[0,maintenancemode],"vote":[1,vote],"inventory":[1,InventoryDisplay],"equip":[1,equip],"status":[0,status]}
# 0 = needs no args
# 1 = needs args

@bot.command()
async def coin(ctx,*args):
    if args[0] in commandslist:
        print(args[0])
        if commandslist[args[0]][0]:
            await commandslist[args[0]][1](ctx,args)
        else:
            await commandslist[args[0]][1](ctx)
    elif args[0].lower() == "update" or args[0].lower() == "restart":
        if ctx.author.id == 431047023689596928:
            await ctx.send("Applying updates...")
            await asyncio.sleep(1)
            await ctx.send("Restarting...")
            exit()
        else:
            await ctx.send("Invalid permissions... sorry...")
    else:
        print("Invalid command by "+ctx.author.display_name+" - "+args[0])

bot.run(TOKEN)

