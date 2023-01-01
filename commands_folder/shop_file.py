from global_context import *
from commands_folder.store_coins_file import savecoins

# Format for Store Dictionary:
# {"name (all lower case)":[cost (number), "emote ID", WRTVFC Role ID (number)])

store = \
    {
        "wayne" :   [25,"<:waynerTrick:726571399921139772>",1058908672278925393],
        "baaulp":   [25,"<:baaulpPasta:757624627299090502>",1058907806624919673],
        "holly" :   [25,"<:hollytonesBibi:757619654196985987>",1058907905795047576],
        "gir"   :   [25,"<:mastergirGirbot:757618605486637137>",1058908071738474526],
        "mira"  :   [25,"<:mirakuruPower:726574184452325517>",1058907897775525888],
        "socpens":  [25,"<:socpenBabie:757622293085159484>",1058907911214076015],
        "logmore":  [25,"<:logmorBanjo:757625482551230524>",1058908079514734643],
        "trog"  :   [25,"<:tr0gDog:757626204122513558>",1058908083981656074],
        "verified": [50,"<:verificationbadge:1058890128338194442>",1054736944099246100],
        "bitcoin":  [100,"<:waynerBitcoin:726571398641877002>",1058908085365780550]
    }

async def shop_command(ctx,args):
    rolelist = {}
    for item in store.keys():
        rolelist[store[item][2]] = item
    if len(args) == 1:
        output = "<a:gold:1038495846074941440> COIN STORE <a:gold:1038495846074941440>\nTo buy any of these, type `!coin shop [icon name]`.\nWARNING: Buying a new role icon will delete your previous ones - however, a refund will be provided.\n\n"
        for item in store.keys():
            output += f"{store[item][1]} {item.capitalize()} - {store[item][0]} Coins\n\n"
        await ctx.send(output)

    elif args[1].lower() in store:
        selected = args[1].lower()
        authorrolelist = []
        for role in ctx.author.roles:
            authorrolelist.append(role.id)
        if store[selected][2] not in authorrolelist:
            cost = 0
            for role in authorrolelist:
                print(role)
                if int(role) in rolelist.keys():
                    cost -= store[rolelist[role]][0]
            cost += store[selected][0]
            if context[2][ctx.author.id][0] >= cost:
                output = f"You got the {store[selected][1]} {selected.capitalize()} role.\n"
                if cost > 0 and cost != store[selected][0]:
                    output += f"You exchange your old role icon, meaning that this icon costs you {cost} coins."
                elif cost < 0:
                    output += f"You exchange your old role icon, meaning that you receive a refund of {-cost} coins."
                elif cost == 0:
                    output += f"You exchange your old role icon, meaning that this item is free."
                else:
                    output += f"This icon costs you {cost} coins."
                for role in authorrolelist:
                    print(role)
                    if int(role) in rolelist.keys():
                        await ctx.author.remove_roles(discord.utils.get(ctx.guild.roles, id=role))
                        
                print(rolelist)
                newrole = discord.utils.get(ctx.guild.roles, id=store[selected][2])
                await ctx.author.add_roles(newrole)
                context[2][ctx.author.id][0] -= cost
                await savecoins(ctx)

                output += f"\nYou now have {context[2][ctx.author.id][0]} coins."
                await ctx.send(output)

            else:
                await ctx.send("Unfortunately, you can't afford that.")
        else:
            await ctx.send("You already have that role!")



