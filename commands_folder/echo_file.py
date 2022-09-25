import discord
from discord.ext import commands


async def echo_command(ctx, arg):
    await ctx.send(arg)
