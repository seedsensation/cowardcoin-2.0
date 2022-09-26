from global_context import *

async def get_command(ctx):
    await ctx.send("You got coin, "+ctx.author.display_name+" ("+str(ctx.author.id)+")")
    context[0] = False
    await context[1].delete()