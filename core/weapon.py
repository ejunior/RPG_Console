__author__ = 'ejunior'

# todo: implement critical, status effects, magical effects, different damage types


class Weapon:
    def __str__(self):
        return "a " + self._att_type + " weapon"

    def __init__(self, att_type, att_bonus: int, dmg, crit_chance=(20,), critdmgmod_fx=lambda dmg: max(dmg)):

        self._att_type = att_type
        self._dmg = dmg
        # self._dmg_func = dmg_function
        self.mods = []
        self._attack_bonus = att_bonus
        self.critical_chance = crit_chance
        self.crit_dmg = critdmgmod_fx

    def attack_bonus(self) -> object:
        return self._attack_bonus

    def dmg(self):
        return self._dmg

    def type(self):
        return self._att_type


dagger = Weapon("melee", 0, (1, 4), (18, 19, 20), lambda dmg: 2 * dmg)
short_sword = Weapon("melee", 0, (1, 6), (19, 20), )
long_sword = Weapon("melee", 1, (1, 10), (20,), lambda dmg: 2 * dmg)

# poisoned_plus_2 = (dmg, 2, weapon)
# pircing = (df, -1, dr)
