from global_context import *
from commands_folder import store_coins_file
from random import choice,randint

async def get_command(ctx):
    if context[0]:
        context[6] = True
        context[0] = False
        await context[1].delete()
        if context[12] == 4:
            value = randint(20,50)
        else:
            value = coinrarities[context[12]][3]
        context[2][ctx.author.id][0] += value
        if value == 1:
            plural = ""
        else:
            plural = "s"
        output = (f"{coinrarities[context[12]][1]} You got {value} coin{plural}, " + ctx.author.display_name + "!")
        if context[11][0] == ctx.author.id:
            context[11][1] += 1
            if context[11][1] > 1:
                output += f'\n{coinrarities[context[12]][1]} You currently have a streak of {context[11][1]} coins in a row! 🔥 🔥 🔥'
                if context[11][1] % 5 == 0:
                    context[2][ctx.author.id][0] += context[11][1]
                    output += f'\n{coinrarities[context[12]][1]} You gained {context[11][1]} bonus coins from your streak!'

        else:
            context[11][0] = ctx.author.id
            context[11][1] = 1

        output += f"\n{coinrarities[context[12]][1]} You now have {str(context[2][ctx.author.id][0])} coins."

        await ctx.send(output)

        await store_coins_file.savecoins(ctx)
        await ctx.delete()
    else:
        output = choice(insults)
        if output == "funny":
            output = f"buddy. there's a big storm coming for you. if you don't stop typing !get coin, I'm going to bring all of the team fortress two mercenaries to your house, and they're going to shoot ***rockets*** at you, and beat you *and* your dog with hammers. yeah that's right. i know your dog's name. it's `[{ctx.author.display_name}'S DOG]`. yeah. that's right. you scared? you scared, fucker?"
        await ctx.send(output)



