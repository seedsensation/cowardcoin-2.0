from global_context import *
from commands_folder import store_coins_file
from random import choice

async def get_command(ctx):
    if context[0]:
        context[6] = True
        context[0] = False
        await context[1].delete()
        context[2][ctx.author.id][0] += 1
        output = ("<a:gold:1038495846074941440> You got a coin, " + ctx.author.display_name + "!\n<a:gold:1038495846074941440> You now have "+str(context[2][ctx.author.id][0])+" coins.")
        if context[11][0] == ctx.author.id:
            context[11][1] += 1
            if context[11][1] > 1:
                output += f'You currently have a streak of {context[11][1]} coins in a row! 🔥 🔥 🔥'
                if context[11][1] % 5 == 0:
                    context[2][ctx.author.id][0] += context[11][1]
                    output += f'\nYou gained {context[11][1]} coins!\nYou now have {context[2][ctx.author.id][0]} coins!'
        else:
            context[11][0] = ctx.author.id
            context[11][1] = 1

        await ctx.send(output)

        await store_coins_file.savecoins(ctx)
        await ctx.delete()
    else:
        await ctx.send(choice(insults))



