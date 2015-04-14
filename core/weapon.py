__author__ = 'ejunior'

# todo: implement critical, status effects, magical effects, different damage types


class Weapon:

    def __str__(self):
        return "a " + self._att_type + " weapon"

    def __init__(self, att_type, att_bonus: int, dmg):
        self._att_type = att_type
        self._dmg = dmg
        # self._dmg_func = dmg_function
        # self._stat_list = stat_list
        self.mods = []
        self._attack_bonus = att_bonus


    def attack_bonus(self) -> object:
        return self._attack_bonus

    def dmg(self):
        return self._dmg

    def type(self):
        return self._att_type


sword = Weapon("melee", 1, (6, 17))
#bow = Weapon("ranged",)


# poisoned_plus_2 = (dmg, 2, weapon)
# pircing = (df, -1, dr)
