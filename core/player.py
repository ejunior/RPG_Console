from core.weapon import sword

__author__ = 'ejunior'


class Player:

    def __init__(self):
        self._mod_list = []
        self._equip_weapon = None
        self._equip_equip_shield = None

    def equip_wepon(self, weapon):
        self._equip_weapon = weapon

        self._mod_list.extend(weapon.mods)
        print(weapon)
        print("wepon " + " equiped")


p = Player()
p.equip_wepon(sword)