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
    if timediff < context[8]:
        timeleft = round(context[8]-timediff)
        output = ""
        hours = math.floor(timeleft/3600)
        if hours > 0:
            plural = ""
            timeleft-=(hours*3600)
            if hours != 1:
                plural = "s"
            output+=str(hours)+" hour"+plural+", "
        minutes = math.floor(timeleft/60)
        if minutes > 0:
            timeleft-=(minutes*60)
            plural = ""
            if minutes != 1:
                plural = "s"
            output+=str(minutes)+" minute"+plural+", "
        if hours > 0 or minutes > 0:
            output += "and "
        plural = ""
        if timeleft != 1:
            plural = "s"
        output += str(timeleft)+" second"+plural
        await ctx.send("You're too tired after your last trick! Give it another try in "+output+" 😎")
    else:
        max = 100
        if context[2][ctx.author.id][3] >= 1:
            max += context[2][ctx.author.id][3]
            context[2][ctx.author.id][3] = 0
        max += (context[2][ctx.author.id][4]*5)

        style = random.randint(1,max)
        if context[2][ctx.author.id][3] >= 1:
            style += context[2][ctx.author.id][3]
            context[2][ctx.author.id][3] = 0
        style += context[2][ctx.author.id][4]
        print(str(style))
        if amount == 1 and style > 25:
            output = "You flip a coin!\n"
            result = random.choice(["heads","tails"])
            output += "It's "+result+"!\n"
            if style >= 90:
                output+="You do a sick ass kickflip and still somehow manage to catch the coin! And...\nWhen you open your other hand, there's a coin in that one too!\nYou gain 1 coin and "+str(style)+" style points!\n"
                context[2][ctx.author.id][0] += 1
                output += "You now have "+str(context[2][ctx.author.id][0])+" coins.\n"

        else:
            tricks = ["You juggle x coins while grinding on a rail!","You balance x coins on your head while doing a kickflip!","You jump in the air, throw your skateboard at a wall, bounce it off the wall and land back on it, with x coins in your mouth!"]
            tricks = [t.replace('x', str(amount)) for t in tricks]
            output = random.choice(tricks)
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
                style += amount



        context[2][ctx.author.id][1] += style
        output += "You gain "+str(style)+" Style Points™!\nYou now have "+str(context[2][ctx.author.id][1])+" Style Points™."
        await ctx.send(output)
        await savecoins(ctx)
        context[2][ctx.author.id][2] = time.time()

async def eat_command(ctx):
    if context[2][ctx.author.id][0] >= 1:
        output = "You have eaten a coin!"
        context[2][ctx.author.id][0] -= 1
        context[2][ctx.author.id][3] += 1
        if context[2][ctx.author.id][3] == 5 and ctx.channel.id == 813898229368094760:
            output += ("\nCOIN FACT: You can also run commands by DMing me!")
        elif context[2][ctx.author.id][3] == (45+(context[2][ctx.author.id][4]*5)):
            output += ("\nYou feel extremely full...")
        elif context[2][ctx.author.id][3] == 45:
            output += ("\nYou can't eat any more coins or you feel like you'll explode...")
        elif context[2][ctx.author.id][3] == (50+(context[2][ctx.author.id][4]*5)):
            context[2][ctx.author.id][3] = 0
            context[2][ctx.author.id][4] += 1
            output += ("\nYou Ascend. You have reached peak Coin Eating. All coins in your stomach disappear. It is time for your task to begin anew.\nYou have reached Ascension Level "+str(context[2][ctx.author.id][4])+".")

        if context[2][ctx.author.id][3] == (50+(context[2][ctx.author.id][4]*5)) and context[2][ctx.author.id][4] == 25:
            output += ("\nYour ascension is complete. You are now the most powerful Coin-Eater in the galaxy.\nHowever, you can still improve...")
            
        if context[2][ctx.author.id][3] == (50+(context[2][ctx.author.id][4]*5)) and context[2][ctx.author.id][4] == 30:
            output += ("\nNo mere mortal has ever reached your heights of coin-eating. Your deeds shall live in infamy for the rest of time.\nHowever, if you continue to ascend, something in the dark may begin to notice.")
        
        if context[2][ctx.author.id][3] == (50+(context[2][ctx.author.id][4]*5)) and context[2][ctx.author.id][4] == 35:
            output += ("\nIn the darkness between the stars, a presence awakes.")
            
        if context[2][ctx.author.id][3] == (50+(context[2][ctx.author.id][4]*5)) and context[2][ctx.author.id][4] == 40:
            output += ("\nThe presence senses the sheer power of your coins, and space itself begins to shift as it begins to tread towards you.")

        await ctx.send(output)
        await savecoins(ctx)
