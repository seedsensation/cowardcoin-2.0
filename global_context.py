import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

context = [
    "false",    # 0 - coin currently active
    "",         # 1 - created coin message ctx
    {},         # 2 - total number of coins
    0,          # 3 - time until next coin
    30,         # 4 - minimum number of seconds before next coin  (default: 30)
    1800,       # 5 - maximum number of seconds before next coin (default: 1800)
    True,       # 6 - does a coin need to be created?
    120,        # 7 - time until coin expires (default: 120)
    14400,      # 8 - minimum time between tricks in seconds (default: 14400) 
    25,         # 9 - upper bound for losing coins
    90,         # 10 - lower bound for doubling coins
    [0, 0],     # 11 - streak counter - [0] = user ID, [1] = streak count
    0,          # 12 - coin value - 0 = undefined, 1 = bronze, 2 = silver, 3 = gold, 4 = red
    [50,85,99], # 13 - coin variant rarities - random number gen 1-100, below [0] = bronze, below [1] = silver, below [2] = gold, else red
    False,      # 14 - TESTING MODE - DO NOT EVER ENABLE WHEN BOT IS LIVE
]

election = {

    "A":["Eat the Rich (NEW)", "*Redistribution.* \nOnce every week, the Collector with the most Coins in the Server will have all of their Coins redistributed to the rest of the Server."],
    "B":["StylePoints™ Redux™", "*Be the Very Best.* \nCreate tiers of rewards for Coin Tricks. Give StylePoints™ meaning."],
    "C":["Into Battle", "*Random Encounters.* \nMonsters will occasionally appear in <#813898229368094760>. Fight them off in **Turn-Based Combat** to earn their Treasure."],

}


# coin variants: [0] = display name, [1] = emote, [2] = file name (-.gif), [3] = value
coinrarities = {
    0   :   ["undefined","[error]","error",0],
    1   :   ["bronze","<a:bronzecoin:844545666201288755>","bronze",1],
    2   :   ["silver","<a:silvercoin:844545665911881788>","silver",5],
    3   :   ["gold","<a:goldcoin:813889535699189871>","gold",10],
    4   :   ["SUPER RARE red","<a:redcoin:844545670709772290>","ultrarare"]
}

insults = [
    "there is no coin. please.",
    "leave me alone. i'm trying to sleep.",
    "don't you have anything better to do?",
    "literally my only job is to give you coins when theres one available. there isn't one. i'm going back to sleep",
    "funny"

]

intents = discord.Intents.all()  # grant all permissions
bot = commands.Bot(command_prefix="!", intents=intents)  # sets the default prefix to "coin ", grants intents
client = discord.Client(intents=intents)

load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")  # retrieve token from .env file
CHANNEL = os.getenv("COIN_CHANNEL")
