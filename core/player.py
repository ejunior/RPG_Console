from core.rules import d20
from core.weapon import sword, Weapon

__author__ = 'ejunior'


class Player:
    def __str__(self):
        return "player({})-> ST({}), DX({}), IQ({}), HT({})".format(self._name, self._ST, self._DX, self._IQ, self._HT)

    def __init__(self, name: str, st=10, dx=10, iq=10, ht=10):
        self._name = name
        self._mod_list = []
        self._weapon = None
        self._shield = None
        self._Armor = None
        self._ST = st
        self._DX = dx
        self._IQ = iq
        self._HT = ht

    @property
    def base_attack_bonus(self):
        return self._DX // 2 - 5

    @property
    def full_attack_bonus(self):
        if self._weapon is not None:
            return self.base_attack_bonus + self._weapon.attack_bonus()  # consider to include modifiers
        else:
            return self.base_attack_bonus

    def equip_weapon(self, weapon: Weapon):
        self._weapon = weapon
        self._mod_list.extend(weapon.mods)
        print(weapon.type() + " weapon equiped")

    def weapon_full_attack(self, enemy):
        return enemy.defense - self.full_attack_bonus + d20

    @property
    def base_defense_bonus(self) -> int:
        return self._DX // 2 - 5

    @property
    def defense(self):
        defense = 0
        if self._Armor is not None:
            defense = self._Armor.defense_bonus
        if self._shield is not None:
            defense += self._shield.defense_bonus
        return defense + self.base_defense_bonus


p1 = Player("zack", 12, 15, 10, 9)
p2 = Player("noob", 10, 7, 10, 7)

p1.equip_weapon(sword)
print(p1.weapon_full_attack(p2))
print(p2.weapon_full_attack(p1))

print("p1 base attack %+d " % p1.base_attack_bonus)
print("p2 base attack %+d" % p2.base_attack_bonus)
print(p1)
print(p2)
print(p2.weapon_full_attack(p1))
