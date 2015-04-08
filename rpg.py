__author__ = 'ejunior'

from commands.cls import *


keep_going = True

commandList = {
    "cls": Cls(),
    "exit": Exit()
}


class context:
    running = True


while keep_going:

    try:
        command = input('RPG> ').strip()
        (commandList[command.lower()]).execute()
    except:
        print('Invalid Command.')