__author__ = 'ejunior'

from commands.command import Command


class Cls(Command):

    def __repr__(self):
        print self.__class__.name()
        return ''

    def execute(self, context):
        import os
        os.system('dir' if os.name == 'nt' else 'clear')
        return ''


class Exit(Command):

    def execute(self):
        quit()
