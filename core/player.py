from core.weapon import Weapon

__author__ = 'ejunior'


class Player:
    _npc_default_name_counter = 0

    def __str__(self):
        return "player({})-> ST({}), DX({}), IQ({}), HT({})".format(self.name, self.st, self.dx, self.iq, self.ht)

    def __init__(self, name=None, st=10, dx=10, iq=10, ht=10):
        if name is not None:
            self.name = name
        else:
            self.name = Player._get_a_default_name()

        self.weapon = None
        self._shield = None
        self._armor = None

        self.st = st
        self.dx = dx
        self.iq = iq
        self.ht = ht

    @staticmethod
    def _get_a_default_name():
        Player._npc_default_name_counter += 1
        return "NPC" + str(Player._npc_default_name_counter)

    @property
    def stats(self):
        return dict(ST=self.st, DX=self.dx, IQ=self.iq, HT=self.ht)

    #
    # Attack

    @property
    def base_attack_bonus(self):
        return self.dx // 2 - 5

    @property
    def attack_bonus(self):
        return self.base_attack_bonus if self.weapon is None \
            else self.base_attack_bonus + self.weapon.attack_bonus()  # consider to include modifiers

    def equip_primary_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def unequip_primary_weapon(self):
        self.weapon = None

    #
    # defense

    @property
    def base_defense_bonus(self) -> int:
        return self.dx // 2 - 5

    @property
    def defense_bonus(self):
        defense = 0 if self._armor is None else self._armor.defense_bonus
        defense += 0 if self._shield is None else self._shield.defense_bonus
        return defense + self.base_defense_bonus


class PlayerError(Exception):
    pass


class InvalidEquipmentError(PlayerError):
    pass
