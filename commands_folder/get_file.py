from global_context import *
from commands_folder import store_coins_file
from random import choice

async def get_command(ctx):
    if context[0]:
        context[6] = True
        context[0] = False
        await context[1].delete()
        context[2][ctx.author.id][0] += 1
        await ctx.send("<a:gold:1038495846074941440> You got a coin, " + ctx.author.display_name + "!\n<a:gold:1038495846074941440> You now have "+str(context[2][ctx.author.id][0])+" coins.")
        await ctx.delete()
        await store_coins_file.savecoins(ctx)
    else:
        await ctx.send(choice(insults))



