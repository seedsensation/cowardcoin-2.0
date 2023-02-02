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
        if context[2][ctx.author.id][4] > 0:
            output += "\nYou have reached Ascension Level "+str(context[2][ctx.author.id][4])+"."
        if ctx.author.id == 1070754908845912154:
            output += "\nYou currently own `95%` of Shares of CowardCoin."
        elif ctx.author.id == 431047023689596928:
            output += "\nYou currently own `5%` of Shares of CowardCoin."
        await ctx.send(output)