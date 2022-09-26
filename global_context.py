import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

context = [
    "false",  # coin currently active
    ""  # created coin message ctx
]

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="coin ", intents=intents)  # sets the default prefix to "coin ", grants intents

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file
CHANNEL = os.getenv("COIN_CHANNEL")