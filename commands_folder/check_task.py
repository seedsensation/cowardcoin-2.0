import asyncio
from commands_folder.create_file import create_command
from global_context import *

async def check():
    while True:
        print("RUNNING CHECK")
        if context[6]:
            print("COIN CREATION REQUIRED")
            await create_command("")
        else:
            print("COIN CREATION NOT REQUIRED")
        await asyncio.sleep(10)

def stop():
    task.cancel()



