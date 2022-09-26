from global_context import *
from time import strftime

async def filecheck():
    file = open("files\\text files\\\coins.txt","r")
    coins_string = file.read()
    file.close()
    try:
        coins = eval(coins_string)
    except (FileNotFoundError,TypeError,SyntaxError):
        coins = {}
        for guild in bot.guilds:
            for member in guild.members:
                coins[member.id] = [0,0]
    print(coins)
    file = open("files\\text files\\\coins.txt","w")
    file.write(str(coins))
    file.close()
    context[2] = coins

async def savecoins(ctx):
    if not os.path.exists(strftime("backups\\%Y.%m.%d\\")):
        os.makedirs(strftime("backups\\%Y.%m.%d\\"))  # make a folder if it doesn't already exist with the name of today's date
    backuptime = strftime("%Y.%m.%d\\%H.%M.%S")
    file = open("backups\\%s.txt" % backuptime, "w")
    file.write(str(context[2]))
    file.close()
    print("Saved to backups\\"+str(backuptime)+": "+str(context[2]))
    file = open("files\\text files\\coins.txt","w")
    file.write(str(context[2]))
    file.close()
    print("Saved to files\\text files\\coins.txt: "+str(context[2]))

