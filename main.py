from dotenv import load_dotenv
import os
import logging
import discord
import asyncio
from time import *
import datetime
from discord.ext import commands



load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")

if not os.path.exists(strftime("logs\\%Y.%m.%d\\")):
    os.makedirs(strftime("logs\\%Y.%m.%d\\"))
logtime = strftime("%Y.%m.%d\\%H.%M.%S")
file = open("logs\\%s.txt"% logtime,"w")
file.close()
logging.basicConfig(filename="logs\\%s.txt" % logtime,
                level=logging.INFO,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S')  # activates logging

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="coin ",intents=intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="the economy 😎"))

client.run(TOKEN)