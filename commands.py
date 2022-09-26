from commands_folder import echo_file
from commands_folder import create_file
async def echo_send(ctx,arg):
    await echo_file.echo_command(ctx,arg)

async def create_send(ctx):
    await create_file.create_command(ctx)