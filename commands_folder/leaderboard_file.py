from global_context import *

async def leaderboard_command(ctx,args):
    if len(args) == 2 and args[1].lower() == "style":
        styles = context[2]
        styledict = {}
        for item in styles:
            styledict[item] = styles[item][1]
        sortedstyledict = sorted(styledict.items(), key=lambda x: x[1])
        print(sortedstyledict)
        if len(sortedstyledict) > 6:
            max = 6
        else:
            max = len(sortedstyledict)
        output = "<a:gold:1038495846074941440> **LEADERBOARD** <a:gold:1038495846074941440>\n"
        for x in range(1, max):
            user = await bot.fetch_user(sortedstyledict[-x][0])
            output += (str(x) + ". **" + str(user.display_name) + "** - " + str(sortedstyledict[-x][1]) + " StylePoints™\n")
        await ctx.send(output)

    else:
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
            output += (str(x)+". **"+str(user.display_name) + "** - " + str(sortedcoindict[-x][1])+" coins\n")
        await ctx.send(output)




