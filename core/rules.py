import random

from core.player import Player


__author__ = 'ejunior'

'''

print(GurpsDiceRules.skillroll(5))

'''


class _Dice:
    def __init__(self, s):
        self._sides = s

    def __str__(self):
        return str(self.__call__)

    def __repr__(self):
        return self.__call__

    @property
    def __call__(self):
        _var = random.randrange(1, self._sides + 1)
        print("roll ", _var)
        return _var

    def __add__(self, other):
        # print("add ", other)
        return other + self.__call__

    def __radd__(self, other):
        return other + self.__call__

    def __rmul__(self, other):
        pool = 0
        for _ in range(other):
            pool += self.__call__
            # print("pool", pool)
        # print("mult ", pool)
        return pool


class GurpsDiceRules:
    d6 = _Dice(6)

    @staticmethod
    def skillroll(skill):
        _pool = 3 * d6
        _status = ""
        # A roll of 3 or 4 is always a critical success.
        if _pool <= 4:
            _status += "critical "
        # A roll of 5 is a critical success if your effective skill is 15+
        elif _pool == 5 and skill >= 15:
            _status += "critical "
        # A roll of 6 is a critical success if your effective skill is 16+
        elif _pool == 6 and skill >= 16:
            _status += "critical "
        elif _pool == 18:
            _status += "critical "
        # A roll of 17 is a critical failure if your effective
        # skill is 15 or less; otherwise, it is an ordinary failure.
        elif _pool == 17 and skill <= 15:
            _status += "critical "
        # Any roll of 10 or more greater than your effective skill
        # is a critical failure: 16 on a skill of 6, 15 on a skill of 5, and so on.
        elif _pool >= skill + 10:
            _status += "critical "

        if _pool <= skill:
            _status += "success"
        elif _pool > skill:
            _status += "faliure"
        return _pool, _status


class JRRPGRules:
    @staticmethod
    def main_weapon_full_attack_resolution(attacker: Player, adversary: Player):
        """
        Must return a tuple result
        example: (diceRoll, critical)
                 (diceRoll, failure)
        """

        critical_chance = (20,) if attacker.weapon is None else attacker.weapon.critical_chance
        critical_chance += (1,)
        # print("critical_chance", critical_chance)

        df = 10 + adversary.defense_bonus
        # print("adversary.defense ", df)
        roll = d20()
        # print("d20 roll", roll)
        att = attacker.attack_bonus + roll
        # print("attacker.attack (+", attacker.attack_bonus, " attack bonus) ", att)

        resolution = "critical " if roll in critical_chance else ""
        resolution += "hit" if att >= df else "miss"
        return att - df, resolution


d20 = _Dice(20)
d6 = _Dice(6)
