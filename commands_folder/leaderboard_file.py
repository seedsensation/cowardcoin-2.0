from global_context import *

async def leaderboard(ctx):
    file = open("files\\text files\\\coins.txt", "r")
    coins_string = file.read()
    file.close()
    coins = eval(coins_string)
    coindict = {}
    for item in coins:
        coindict[item] = coins[item][0]
    sortedcoindict = sorted(coindict.items(), key=lambda x:x[1])
    print(sortedcoindict)
    if len(sortedcoindict) > 5:
        max = 5
    else:
        max = len(sortedcoindict)
    output = "LEADERBOARD:\n"
    for x in range(1,max):
        user = await bot.fetch_user(sortedcoindict[-x][0])
        output += (str(x)+". "+str(user.display_name) + " - " + str(sortedcoindict[-x][1])+"\n")
    await ctx.send(output)

