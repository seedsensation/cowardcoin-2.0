from global_context import *

async def leaderboard_command(ctx):
    coins = context[2]
    coindict = {}
    for item in coins:
        coindict[item] = coins[item][0]
    sortedcoindict = sorted(coindict.items(), key=lambda x:x[1])
    print(sortedcoindict)
    if len(sortedcoindict) > 6:
        max = 6
    else:
        max = len(sortedcoindict)
    output = "<a:gold:1038495846074941440> **LEADERBOARD** <a:gold:1038495846074941440>\n"
    for x in range(1,max):
        user = await bot.fetch_user(sortedcoindict[-x][0])
        output += (str(x)+". **"+str(user.display_name) + "** - " + str(sortedcoindict[-x][1])+"\n")
    await ctx.send(output)

