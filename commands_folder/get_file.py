from global_context import *
from commands_folder import store_coins_file
from random import choice

async def get_command(ctx):
    if context[0]:
        context[6] = True
        context[0] = False
        await context[1].delete()
        context[2][ctx.author.id][0] += 1
        await ctx.send("You got a coin, " + ctx.author.display_name + "!\nYou now have "+str(context[2][ctx.author.id][0])+" coins.")
        await store_coins_file.savecoins(ctx)
    else:
        await ctx.send(choice(insults))



