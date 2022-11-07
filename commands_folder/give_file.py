from global_context import *
from random import randint
from commands_folder.style_file import *
async def give_command(ctx,args):
    print(args)
    if len(args)==3:
        try:
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
                print(context[2][recipient][0])
            else:
                await ctx.send("Invalid amount given. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`\n- That you specifically gave a whole number for the amount.")

        except ValueError or KeyError:
            await ctx.send("An error occurred reading your message. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`\n- That the recipient is specifically tagged in the message")
    else:
        await ctx.send("Not enough arguments were given. Please check the following:\n- Your message is formatted `!coin give @recipient [amount]`")