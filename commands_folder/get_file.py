from global_context import *
from commands_folder import store_coins_file

async def get_command(ctx):
    await ctx.send("You got coin, " + ctx.author.display_name + " (" + str(ctx.author.id) + ")")
    context[0] = False
    await context[1].delete()
    context[2][ctx.author.id][0] += 1
    await ctx.send("You now have "+str(context[2][ctx.author.id][0])+" coins.")
    await store_coins_file.savecoins(ctx)



