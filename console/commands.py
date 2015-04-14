__author__ = 'ejunior'

from termcolor import colored
import os
print(os.name)

if os.name == "nt":
    from colorama import init
    init()

print(colored('Boo will miss you', 'red'))
# print(Back.GREEN + 'and with a green background')


class Command:
    def execute(self, context):
        pass

    def name(self):
        return self.__name__


class Context:
    def __init__(self):
        self.running = True


class Cls(Command):

    def execute(self, context):
        import os
        os.system('dir' if os.name == 'nt' else 'clear')
        return ''


class Exit(Command):

    def execute(self, context):
        context.running = False
        print(colored('Boo will miss you', 'red'))


_exit = Exit()

commandList = {
    "cls": Cls(),
    "exit": _exit,
    "quit": _exit  # alias
}