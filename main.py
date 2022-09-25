import logging
import os
from time import *
from commands import *
import discord
from discord.ext import commands
from dotenv import load_dotenv



load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file

if not os.path.exists(strftime("logs\\%Y.%m.%d\\")):
    os.makedirs(strftime("logs\\%Y.%m.%d\\"))  # make a folder if it doesn't already exist with the name of today's date
logtime = strftime("%Y.%m.%d\\%H.%M.%S")
file = open("logs\\%s.txt" % logtime, "w")
file.close()
logging.basicConfig(filename="logs\\%s.txt" % logtime,
                    level=logging.INFO,
                    format='%(levelname)s: %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')  # activates logging

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="coin ", intents=intents)  # sets the default prefix to "coin ", grants intents


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="the economy 😎"))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def echo(ctx, arg):  # ctx = context of command, arg = second word
    await echo_send(ctx, arg)  # reply to the original message echoing back the second word




bot.run(TOKEN)
