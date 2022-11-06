import os

async def restart_command(ctx):
    await ctx.send("Restarting...")
    os.system("sudo execute.sh")
    exit()