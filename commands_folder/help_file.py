from global_context import *

commandsdefinition = {
	"get":[1,"<a:gold:1038495846074941440> **GET**\nThis command collects any available coins.\nIf there are no coins available, the bot might be a little annoyed at being asked."],
	"leaderboard":[1,"<a:gold:1038495846074941440> **LEADERBOARD**\nThis command shows you the users with the top 5 highest number of coins. Compare yourselves and fight with your friends :)\nUse `!coin leaderboard full` to see the full leaderboard, and `!coin leaderboard bottom`/`!coin leaderboard reverse` to see the bottom 5."],
	"help":[0,"I don't think you really need help with that one..."],
    "give":[1, "Give coins to your friends! For example, type `!coin give @user 10` to give @user 10 coins. Make sure the user is specifically pinged in the message though, or else it won't work!"],
	"style":[1,"""<a:gold:1038495846074941440> **Style Points™**
    Style points are given out when you do cool Coin Tricks! You complete a coin trick by using the `!coin give` command to give yourself any amount of coins.
    This will award you a random amount of Style Points™ - ranging between 1 and 100.
    If you gain 90 or more Style Points™ in a single trick, the amount of coins you put into it will be doubled!
    However, if you gain 25 or less Style Points™ in a single trick, you will lose 1/3 of the coins you put in (rounded up).
    Also, you can only pull off one Coin Trick every """+str(context[8]/3600)+""" hours.
    If you want to see how many Style Points™ you have, you can simply do `!coin count`! This will display your Style Points™ along with your coins if you have any.
    If you want to compete, you can use `!coin leaderboard style` - this will display an alternate leaderboard for Style Points™ instead of coins."""],
    "shop":[1,"Buy cool role icons for yourself, using the command `!coin shop [name]`!\nYou can exchange icons you already have for a discount/refund when buying new ones - for example, if you own <:waynerTrick:726571399921139772> and want to change to <:socpenBabie:757622293085159484>, it will be free.\nOn the other hand, if you own <:verificationbadge:1058890128338194442> and want to buy <:waynerBitcoin:726571398641877002>, it will cost you 50 coins, instead of the usual 100."],
    "variants":[1,f"Coins come in 4 rarities - bronze, silver, gold, and RED. \nThe higher the rarity, the more coins you get from it - however, they become increasingly rare. \nBy default, a coin has a 50% chance of being bronze, compared to 1% for Red coins."],
    "eat":[1,"Type `!coin eat` to eat coins!\nThe more coins you eat, the more likely it is to double your coins by doing Skateboard Tricks™!\nHowever, **the counter resets with every trick you do** - so be careful."],
    "ascension":[1,"When you eat your 50th coin, you will Ascend. This has two effects -\n1. Increases how many coins it takes to Ascend by 5\n2. Adds a permanent +5 to the cap on StylePoints™ from doing Skateboard Tricks™, making it much more likely to double your coins."],
}

async def help_coin(ctx,arg):
    if len(arg)==1:
        result = ("""
<a:gold:1038495846074941440> Welcome to CowardCoin! <a:gold:1038495846074941440>
At a random interval between """+str(context[4])+" seconds and "+str(int(context[5]/60))+""" minutes, a coin will be created.
This is signalled by a message with an image of a giant coin.
At this point, you can type `!coin get` to collect the coin!
This coin will disappear after """+str(context[7])+""" seconds, so be quick!
    
Here is a list of what you can ask for help with.
Type `!coin help [command]` to get a short explanation of how it works.\n""")
        for user in context[2].keys():
            if context[2][user][1] > 0:
                commandsdefinition["style"][0] == 1
                break
            else:
                commandsdefinition["style"][0] == 0
        for command in commandsdefinition:
            if commandsdefinition[command][0]:
                result += "`!coin help "+str(command)+"`\n"
        await ctx.send(result)
    elif arg[1] in commandsdefinition:
        await ctx.send(commandsdefinition[arg[1]][1])
    else:
        await ctx.send("I don't recognise that command, sorry...")
