from global_context import *

async def count_coin(ctx):
    if ctx.author.id in context[2]:
        if ctx.author.id == 1070754908845912154:
            count = "∞"
        else:
            count = context[2][ctx.author.id][0]
        output = ("<a:gold:1038495846074941440> You have "+str(count)+" coins in your account.")
        if context[2][ctx.author.id][1] > 0:
            output += "\nYou also have "+str(context[2][ctx.author.id][1])+" Style Points™!"
        if context[11][0] == ctx.author.id and context[11][1] > 1:
            output += "\nYou currently have a streak of "+str(context[11][1])+" coins in a row! 🔥"
        await ctx.send(output)