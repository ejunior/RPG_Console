from core.weapon import Weapon

__author__ = 'ejunior'


class Character:
    """
    A Character Sheet should provide information about a character
    and could have a group of helper derivated info.

    Character Sheet
        Name
        Stats
            - ST
            - DX
            - IQ
            - HT
        Equipment
            Armor ? shold it be divided?
            Weapon
            Offhand (two handed alowed ?
            Unequiped (backpack)
        Movement list
            Attacks
            defenses

          WARN:  This is unffinished, and probabiliy should be completely recoded

    """
    name_gen_counter = 0

    def __str__(self):
        return "player({})-> ST({}), DX({}), IQ({}), HT({})" \
            .format(self.name, self.st, self.dx, self.iq, self.ht)

    def __init__(self, name=None, st=10, dx=10, iq=10, ht=10):
        if name is not None:
            self.name = name
        else:
            self.name = Character.default_name_gen()

        self.weapon = None
        self.shield = None
        self.armor = None

        self.st = st
        self.dx = dx
        self.iq = iq
        self.ht = ht

    @staticmethod
    def default_name_gen():
        Character.name_gen_counter += 1
        return "NPC" + str(Character.name_gen_counter)

    @property
    def stats(self):
        return dict(ST=self.st, DX=self.dx, IQ=self.iq, HT=self.ht)

    # Attack section

    @property
    def base_attack_bonus(self):
        return self.dx // 2 - 5

    @property
    def attack_bonus(self):
        return self.base_attack_bonus if self.weapon is None \
            else self.base_attack_bonus + self.weapon.attack_bonus()  # consider to include modifiers

    # defense section

    @property
    def base_defense_bonus(self) -> int:
        return self.dx // 2 - 5

    @property
    def defense_bonus(self):
        defense = 0 if self.armor is None else self.armor.defense_bonus
        defense += 0 if self.shield is None else self.shield.defense_bonus
        return defense + self.base_defense_bonus

    # equipment section

    def equip_primary_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def unequip_primary_weapon(self):
        self.weapon = None


class SimpleCharacter:
    """
        char_name
        stats
            hp
            attack
            defense
    """

    def __init__(self, name, hp, attack, defense, is_pc):
        self.name = name
        self.is_pc = is_pc

        self.hp = hp
        self.attack = attack
        self.defense = defense


# class PlayerError(Exception): pass
# class InvalidEquipmentError(PlayerError): pass
