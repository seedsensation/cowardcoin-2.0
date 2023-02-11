from commands_folder import create_file
from commands_folder import store_coins_file
from commands_folder import leaderboard_file

async def create_send(ctx):
    await create_file.create_command(ctx)

async def create_coin():
    await create_file.create_command("")

async def get_send(ctx):
    await create_file.get_command(ctx)

async def file_check():
    await store_coins_file.filecheck()

async def save_coin_to_file(ctx):
    await store_coins_file.savecoins(ctx)

async def leaderboard_send(ctx):
    await leaderboard_file.leaderboard_command(ctx)

async def help_send(ctx):
    await help_file.help_command(ctx)