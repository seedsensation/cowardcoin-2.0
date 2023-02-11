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
    elif len(args) == 2 and (args[1].lower() == "lowest" or args[1].lower() == "bottom" or args[1].lower() == "reverse"):
        coins = context[2]
        coindict = {}
        for item in coins:
            if coins[item][0] != 0:
                coindict[item] = coins[item][0]
        sortedcoindict = sorted(coindict.items(), key=lambda x: x[1], reverse=True)
        print(sortedcoindict)
        if len(sortedcoindict) > 6:
            max = 6
        else:
            max = len(sortedcoindict)
        output = "<a:gold:1038495846074941440> **BOTTOM "+str(max-1)+"** <a:gold:1038495846074941440>\n"
        print(sortedcoindict)
        for x in range(1, max):
            user = await bot.fetch_user(sortedcoindict[-x][0])
            if sortedcoindict[-x][1] == 1:
                plural = ""
            else:
                plural = "s"
            output += (str(x) + ". **" + str(user.display_name) + "** - " + str(sortedcoindict[-x][1]) + " coin"+plural+"\n")
        await ctx.send(output)
    elif len(args) == 2 and args[1].lower() == "full":
        coins = context[2]
        coindict = {}
        for item in coins:
            if coins[item][0] != 0:
                coindict[item] = coins[item][0]
        sortedcoindict = sorted(coindict.items(), key=lambda x: x[1], reverse=True)
        print(sortedcoindict)

        output = "<a:gold:1038495846074941440> **LEADERBOARD** <a:gold:1038495846074941440>\n"
        if len(sortedcoindict)==0:
            output +="The leaderboard is empty, sorry..."
        else:
            for x in range(0, len(sortedcoindict)):
                user = await bot.fetch_user(sortedcoindict[x][0])
                if sortedcoindict[x][1] == 1:
                    plural = ""
                else:
                    plural = "s"
                output += (str(x+1) + ". **" + str(user.display_name) + "** - " + str(sortedcoindict[x][1]) + " coin" + plural + "\n")
        await ctx.send(output)

    else:
        coins = context[2]
        coindict = {}
        output = ""
        for item in coins:
            if coins[item][0] != 0:
                print(item)
                coindict[item] = coins[item][0]

        sortedcoindict = sorted(coindict.items(), key=lambda x:x[1])
        print(sortedcoindict)
        if len(sortedcoindict)==0:
            output +="The leaderboard is empty, sorry..."
        else:
            if len(sortedcoindict) > 6:
                max = 6
            else:
                max = len(sortedcoindict)
            output = "<a:gold:1038495846074941440> **LEADERBOARD** <a:gold:1038495846074941440>\n"
            for x in range(0,max):
                user = await bot.fetch_user(sortedcoindict[-x][0])
                output += (str(x+1)+". **"+str(user.display_name) + "** - " + str(sortedcoindict[-x][1])+" coins\n")
        await ctx.send(output)




