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
                coins[member.id] = [0, 0, 0, 0]

    for guild in bot.guilds:
        for member in guild.members:
            if member.id not in coins:
                coins[member.id] = [0, 0, 0, 0]

            while len(coins[member.id]) < 4:
                coins[member.id].append(0)
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
