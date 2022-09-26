from global_context import *

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

