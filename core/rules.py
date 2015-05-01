import random

from core.character import Character, SimpleCharacter


__author__ = 'ejunior'


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


d20 = _Dice(20)
d6 = _Dice(6)


class GurpsDiceRules:
    """
        just wanted to do this :)
        print(GurpsDiceRules.skillroll(5))
    """

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
    """
    Dinamics of the game

    Option1:  not good enough, but works om persentile not skill based rpgs
        roll against
            if roll less than defense roll
                defended or miss
            if roll higher than defense roll
                hit

    Option2: tooo simple
        Defense Roll if possible
        atack roll > defense roll
            hit
        else
            miss

    Option3: skill based, preferred (needs bounded roll D20 or 3D6 rolls)
        roll agains attack skill
        if not succedded
            miss
        else
            subtrack de difference from defese roll
            roll defense
            if succedded
                defended (save difference to attack bonus) -> attacker better use a defense roll next turn
            else
                hit

    The Problem is that skill base rpg are too hard to code

    say what? i'll do some basic stuff, just to keep rolling.


        Separate
            Defense
            Damage Resistence


        skill list
        sword
        bow
        magic
        shield
        (...)

"""
    @staticmethod
    def attack_resolution(attacker: Character, adversary: Character):
        """
        combat attack resolution, using weapon in hand

        Must return a tuple result
        example: (diceRoll, critical, dmg)
                 (diceRoll, failure)
        """

        # getting critcal rolls numbers
        critical_chance = (20,) if attacker.weapon is None else attacker.weapon.critical_chance
        critical_chance += (1,)

        df = 10 + adversary.defense_bonus

        roll = d20
        # print("d20 roll", roll)
        att = attacker.attack_bonus + roll
        # print("attacker.attack (+", attacker.attack_bonus, " attack bonus) ", att)

        resolution = "critical " if roll in critical_chance else ""
        resolution += "hit" if att >= df else "miss"
        return att - df, resolution

    def attack(self):
        pass


class SimpleRules:
    def __init__(self, a: SimpleCharacter, d: SimpleCharacter):
        self.p1 = a
        self.p2 = d

    def attack(self):
        pass

    def defense(self):
        pass


class Encounter:
    def __init__(self, *members):
        self.turn_players_list = []
        self.turn = 0
        self.combatants = []
        for m in members:
            self.combatants.append(m)

    def roll_initiative(self):
        self.turn = 1
        l = []
        for c in self.combatants:
            l.append((d20, c))  # put the d20 roll and a character sheet on a sorted list
        l.sort(key=lambda tup: tup[0], reverse=True)  # sort by initiative roll
        self.turn_players_list = l

    def get_player_in_turn(self):
        return self.turn_players_list.pop()
