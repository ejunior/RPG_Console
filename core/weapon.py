__author__ = 'ejunior'
import random


class Weapon:

    def __init__(self, att_type, dmg, dmg_function, stat_list=None):
        self._att_type = att_type
        self._dmg = dmg
        self._dmg_func = dmg_function
        self._stat_list = stat_list

    def dmg(self, player):
        return self._dmg


sword = Weapon("melee", (6, 17), lambda p, w: p.str.mod + random.randrange(w.dmg[0], w.dmg[1]))
bow = Weapon("ranged",)
