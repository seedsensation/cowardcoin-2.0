from global_context import *

async def count_coin(ctx):
    if ctx.author.id in context[2]:
        output = ("<a:gold:1038495846074941440> You have "+str(context[2][ctx.author.id][0])+" coins in your account.")
        if context[2][ctx.author.id][1] > 0:
            output += "\nYou also have "+str(context[2][ctx.author.id][1])+" Style Points™!"
        ctx.send(output)