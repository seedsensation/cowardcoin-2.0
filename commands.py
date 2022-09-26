from commands_folder import echo_file
from commands_folder import create_file
from commands_folder import get_file


async def echo_send(ctx,arg):
    await echo_file.echo_command(ctx,arg)

async def create_send(ctx):
    await create_file.create_command(ctx)

async def create_coin():
    await create_file.create_command("")

async def get_send(ctx):
    await get_file.get_command(ctx)