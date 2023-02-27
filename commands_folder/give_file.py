from global_context import *
from commands_folder.style_file import stylecalc
from commands_folder.store_coins_file import savecoins

async def give_command(ctx,args):
    print(args)
    if len(args)==3:
        try:
            if args[1][2] == "!":
                recipient = int(args[1][3:-1])
            else:
                recipient = int(args[1][2:-1])
            amount = args[2]
            if amount.isdigit():
                amount = int(amount)
                if amount > 1:
                    plural = "s"
                else:
                    plural = ""
                if context[2][ctx.author.id][0] < amount:
                    await ctx.send("You can't afford that!")
                else:
                    context[2][recipient][0] += amount
                    context[2][ctx.author.id][0] -= amount
                    recipientobject = bot.get_user(recipient)
                    if recipient == ctx.author.id:
                        await stylecalc([ctx,recipientobject,amount])
                    else:
                        await ctx.send("Sent "+str(amount)+" coin"+plural+" to "+recipientobject.display_name+". You now have "+str(context[2][ctx.author.id][0])+" coins.")
                        await savecoins(ctx)
                print(context[2][recipient][0])
            else:
                await ctx.send("Invalid amount given. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`\n- That you specifically gave a whole number for the amount.")

        except ValueError or KeyError:
            await ctx.send("An error occurred reading your message. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`\n- That the recipient is specifically tagged in the message")
    else:
        await ctx.send("Not enough arguments were given. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`")


'''async def stylecalc(args):
    ctx = args[0]
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
        context[2][ctx.author.id][2] = time.time()'''
