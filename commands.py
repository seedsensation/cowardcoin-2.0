from commands_folder import echo_file

async def echo_send(ctx,arg):
    await echo_file.echo_command(ctx,arg)