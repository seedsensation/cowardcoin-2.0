from global_context import *
from time import strftime
from pathlib import *

async def filecheck():
    try:
        file = open(Path("files/text files/coins.txt"), "r")
        coins_string = file.read()
        file.close()
        coins = eval(coins_string)
    except (FileNotFoundError, TypeError, SyntaxError):
        coins = {}
        for guild in bot.guilds:
            for member in guild.members:
                coins[member.id] = [0, 0, 0]

    for guild in bot.guilds:
        for member in guild.members:
            if member.id not in coins:
                coins[member.id] = [0, 0, 0]
    print(coins)
    file = open(Path("files/text files/coins.txt"), "w")
    file.write(str(coins))
    file.close()
    context[2] = coins


async def savecoins(ctx):
    if not os.path.exists(Path(strftime("backups/%Y.%m.%d/"))):
        os.makedirs(Path(strftime("backups/%Y.%m.%d/")))  # make a folder if it doesn't already exist with the name of
        # today's date
    backuptime = Path(strftime("%Y.%m.%d/%H.%M.%S"))
    file = open(Path("backups/%s.txt" % backuptime), "w")
    file.write(str(context[2]))
    file.close()
    print("Saved to backups/" + str(backuptime) + ": " + str(context[2]))
    file = open(Path("files/text files/coins.txt"), "w")
    file.write(str(context[2]))
    file.close()
    print("Saved to files/text files/coins.txt: " + str(context[2]))

async def count_coin(ctx):
    if ctx.author.id in context[2]:
        output = ("<a:gold:1038495846074941440> You have "+str(context[2][ctx.author.id][0])+" coins in your account.")
        if context[2][ctx.author.id][1] > 0:
            output += "\nYou also have "+str(context[2][ctx.author.id][1])+" Style Points™!"
        await ctx.send(output)