from global_context import *
from commands_folder.store_coins_file import *
from discord.utils import get

async def tip_command(ctx,args):
    check_role = get(ctx.guild.roles, name="admins")
    if check_role not in ctx.author.roles:
        await ctx.send("Admins only... sorry :(")
    else:
        try:
            if args[1][2] == "!":
                recipient = int(args[1][3:-1])
            else:
                recipient = int(args[1][2:-1])
            amount = args[2]
            if amount.isdigit():
                amount = int(amount)
                if amount > 1:
                    plural = "s"
                else:
                    plural = ""

                context[2][recipient][1] += amount
                recipientobject = bot.get_user(recipient)
                await ctx.send("Tipped " + str(amount) + " StylePoint"+str(plural)+"™ to " + recipientobject.display_name + ". "+ recipientobject.display_name + " now has " + str(context[2][recipientobject.id][1]) + " StylePoints™.")
                print(context[2][recipient][0])
            else:
                await ctx.send("Invalid amount given. Please check the following:\n- Your message is formatted `!coin tip @recipient [amount]`\n- That you specifically gave a whole number for the amount.")

        except ValueError or KeyError:
            await ctx.send("An error occurred reading your message. Please check the following:\n- Your message is formatted `!coin tip @recipient [amount]`\n- That the recipient is specifically tagged in the message")

        await savecoins(ctx)
