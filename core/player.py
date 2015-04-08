__author__ = 'ejunior'


class Player:

    def __init__(self):
        self._mod_list = []
        self._equip_weapon = None
        self._equip_equip_shield = None

    def equip_wepon(self,weapon):
        self._equip_weapon = weapon;
        self.mod_list.extend(weapon.mods)



