__author__ = 'ejunior'

from commands.cls import *

keep_going = True

commandList = {
    "cls": Cls(),
    "exit": Exit()
}

context = classmethod
context.running = true

while keep_going:
    command = raw_input('RPG> ').strip()

    try:
        (commandList[command.lower()]).execute()
    except:
        print('Invalid Command.')