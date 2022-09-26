import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

context = [
    "false",  # coin currently active
    "",  # created coin message ctx
    {},  # total number of coins
    0,  # time until next coin
    30,  # minimum number of seconds before next coin
    3600,  # maximum number of seconds before next coin
    True,  # does a coin need to be created?
]

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="!", intents=intents)  # sets the default prefix to "coin ", grants intents
client = discord.Client(intents=intents)

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file
CHANNEL = os.getenv("COIN_CHANNEL")