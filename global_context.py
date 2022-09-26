import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

context = [
    "false",  # coin currently active
    "",  # created coin message ctx
    {},  # total number of coins
    0,   # total delay
    30,   # minimum time to next coin
    60,  # maximum time to next coin
]

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="coin ", intents=intents)  # sets the default prefix to "coin ", grants intents

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file
CHANNEL = os.getenv("COIN_CHANNEL")