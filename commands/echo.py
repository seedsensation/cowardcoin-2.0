import discord
from discord.ext import commands

async def echo(ctx,arg):
    await ctx.send(arg)