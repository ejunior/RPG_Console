__author__ = 'ejunior'

from console.commands import *


ctx = Context()

while ctx.running:

    try:
        command = input('RPG> ').strip().lower()
        if command in commandList:
            (commandList[command]).execute(ctx)
        else:
            print('Invalid Command.')
    except Exception:
        raise

