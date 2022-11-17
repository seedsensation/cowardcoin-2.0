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
    if timediff < 21600:
        if timediff > 60:
            minutes = round(timediff/60,1)
            if minutes > 60:
                hours = round(minutes/60,1)
        
        output = ""
        if hours >= 1:
            minutes-=(hours*60)
            output+=str(hours)+" hours, "
        if minutes >= 1:
            seconds-=(minutes*60)
            output+=str(minutes)+" minutes, "
        if output != "":
            output+=" and "
        output+=seconds+" seconds"
        
        await ctx.send("You're too tired after your last trick! Give it "+output+". <:garaksus:963935108287582208> ")
    else:
        style = random.randint(1,100)
        print(str(style))
        if amount == 1 and style > 25:
            output = "You flip a coin.\n"
            result = random.choice(["heads","tails"])
            output += "It's "+result+"!\n"
            if style >= 90:
                output+="You do a sick ass backflip and still somehow manage to catch the coin! And...\nWhen you open your other hand, there's a coin in that one too!\nYou gain 1 coin and "+str(style)+" style points!\n"
                context[2][ctx.author.id][0] += 1
                output += "You now have "+str(context[2][ctx.author.id][0])+" coins.\n"

        elif amount == 1:
            output = "You flip a coin.\nYou drop it! It falls down the gutter... lost forever...\n"
            context[2][ctx.author.id][0] -= 1
        elif style <= 25:
            amountlost = math.ceil(amount/3)
            if amountlost == 1:
                plural = ""
            else:
                plural = "s"
            output = "You juggle "+str(amount)+" coins!\nBut... oh no! You get distracted, and send "+str(amountlost)+" coin"+plural+" flying!\n"
            context[2][ctx.author.id][0] -= amountlost
        elif style > 25 and style < 90:
            output = "You juggle " + str(amount) + " coins! It's cool as hell, and everyone is applauding.\n"
        else:
            output = "You juggle "+str(amount)+" coins! But... what's this? You kick off the wall and do a full somersault before catching all of the coins in your hand, and... there's twice as many in there than there were before?\nYou gained "+str(amount)+" coins!\n"
            context[2][ctx.author.id][0]+=amount



        context[2][ctx.author.id][1] += style
        output += "You gain "+str(style)+" Style Points™!\nYou now have "+str(context[2][ctx.author.id][1])+" Style Points™."
        await ctx.send(output)
        await savecoins(ctx)
        context[2][ctx.author.id][2] = time.time()
