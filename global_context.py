import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

context = [
    "false",  # coin currently active
    "",  # created coin message ctx
    {},  # total number of coins
    0,  # time until next coin
    30,  # minimum number of seconds before next coin  (default: 30)
    3600,  # maximum number of seconds before next coin (default: 3600)
    True,  # does a coin need to be created?
    60, # time until coin expires
]

insults = [
    "there is no coin. please.",
    "look around you. do you see a coin? i don't.",
    "leave me alone. i'm trying to sleep.",
    "i know the old one did, but i'm not going to give you a coin out of pity if you keep asking.",
    "zzzzzzzzzzZZZZZZZZZZZZZZZZzzzzzzzzzzzzzzzzz",
    "don't you have anything better to do?",
    "literally my only job is to give you coins when theres one available. there isn't one. i'm going back to sleep"

]

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="!", intents=intents)  # sets the default prefix to "coin ", grants intents
client = discord.Client(intents=intents)

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file
CHANNEL = os.getenv("COIN_CHANNEL")