from global_context import *
import random
from commands_folder.store_coins_file import savecoins
import math
import time

async def stylecalc(args):
    ctx = args[0]
    recipientobject = args[1]
    amount = args[2]
    currenttime = time.time()
    timediff = currenttime-context[2][ctx.author.id][2]
    print(timediff)
    if timediff < 86400:
        await ctx.send("You're too tired after your last trick! Give it another day or so <:garaksus:963935108287582208> ")
    else:
        style = random.randint(1,100)
        print(str(style))
        if amount == 1 and style > 25:
            output = "You flip a coin.\n"
            result = random.choice(["heads","tails"])
            output += "It's "+result+"!\n"
            if style >= 90:
                output+="You do a sick ass kickflip and still somehow manage to catch the coin! And...\nWhen you open your other hand, there's a coin in that one too!\nYou gain 1 coin and "+str(style)+" style points!\n"
                context[2][ctx.author.id][0] += 1
                output += "You now have "+str(context[2][ctx.author.id][0])+" coins.\n"

        elif amount == 1:
            output = "You flip a coin.\nYou drop it! It falls down the gutter... lost forever...\n"
            context[2][ctx.author.id][0] -= 1
        else:
            tricks = ["You juggle x coins while grinding on a rail!","You balance x coins on your head while doing a kickflip!","You jump in the air, throw your skateboard at a wall, bounce it off the wall and land back on it, with x coins in your mouth!"]
            output = random.choice(tricks)
            output.replace("x",str(amount))
            if style <= 25:
                amountlost = math.ceil(amount/3)
                if amountlost == 1:
                    plural = ""
                else:
                    plural = "s"
                output +="\nBut... oh no! You get distracted, and send "+str(amountlost)+" coin"+plural+" flying!\n"
                context[2][ctx.author.id][0] -= amountlost
            elif style > 25 and style < 90:
                output += "\nIt's cool as hell, and everyone is applauding.\n"
            else:
                output += "\nBut... what's this? You kick off the wall and do a full somersault before landing back on your skateboard and catching all of the coins in your hand, and... there's twice as many in there than there were before?\nYou gained "+str(amount)+" coins!\n"
                context[2][ctx.author.id][0]+=amount



        context[2][ctx.author.id][1] += style
        output += "You gain "+str(style)+" Style Points™!\nYou now have "+str(context[2][ctx.author.id][1])+" Style Points™."
        await ctx.send(output)
        await savecoins(ctx)
        context[2][ctx.author.id][2] = time.time()
