from global_context import *

commandsdefinition = {
    "get":"<a:gold:1038495846074941440> **GET**\nThis command collects any available coins.\nIf there are no coins available, the bot might be a little annoyed at being asked.",
    "leaderboard":"<a:gold:1038495846074941440> **LEADERBOARD**\nThis command shows you the users with the top 5 highest number of coins. Compare yourselves and fight with your friends :)",
    "help":"I don't think you really need help with that one..."
}

async def help_coin(ctx,arg):
    if len(arg)==1:
        result = ("""
<a:gold:1038495846074941440> Welcome to MarsupialCoin! <a:gold:1038495846074941440>
At a random interval between """+str(context[4])+" seconds and "+str(int(context[5]/60))+""" minutes, a coin will be created.
This is signalled by a message with an image of a giant coin.
At this point, you can type `!coin get` to collect the coin!
This coin will disappear after """+str(context[7])+""" seconds, so be quick!
    
Here is a list of every command available to use by the bot.
Type `!coin help [command]` to get a rundown on how to use that command.\n""")

        for command in commandsdefinition:
            result += "`!coin "+str(command)+"`\n"
        await ctx.send(result)
    elif arg[1] in commandsdefinition:
        await ctx.send(commandsdefinition[arg[1]])
    else:
        await ctx.send("I don't recognise that command, sorry...")