from global_context import *

commandsdefinition = {
    "get":"<a:gold:1038495846074941440> **GET**\nThis command collects any available coins.\nIf there are no coins available, the bot might be a little annoyed at being asked.",
    "leaderboard":"<a:gold:1038495846074941440> **LEADERBOARD**\nThis command shows you the users with the top 5 highest number of coins. Compare yourselves and fight with your friends :)",
    "help":"I don't think you really need help with that one...",
    "style":"""<a:gold:1038495846074941440> **Style Points™**
    Style points are given out when you do cool Coin Tricks! You complete a coin trick by using the `!coin give` command to give yourself any amount of coins.
    This will award you a random amount of Style Points™ - ranging between 1 and 100.
    If you gain 90 or more Style Points™ in a single trick, the amount of coins you put into it will be doubled!
    However, if you gain 25 or less Style Points™ in a single trick, you will lose 1/3 of the coins you put in (rounded up).
    Also, you can only pull off one Coin Trick every 6 hours.
    If you want to see how many Style Points™ you have, you can simply do `!coin count`! This will display your Style Points™ along with your coins if you have any.
    If you want to compete, you can use `!coin leaderboard style` - this will display an alternate leaderboard for Style Points™ instead of coins."""
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
        for user in context[2].keys():
            if context[2][user][1] > 0:
                styleshow = True
                break
            else:
                styleshow = False
        for command in commandsdefinition:
            if (command == "style" and styleshow) or (command != "style"):
                result += "`!coin "+str(command)+"`\n"
        await ctx.send(result)
    elif arg[1] in commandsdefinition:
        await ctx.send(commandsdefinition[arg[1]])
    else:
        await ctx.send("I don't recognise that command, sorry...")
