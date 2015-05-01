import unittest
import re

from core.character import Character
from core.weapon import Weapon


__author__ = 'ejunior'


class InstanciarPlayerTest(unittest.TestCase):
    def testDefultInitiation(self):
        p1 = Character()
        p2 = Character()

        self.assertTrue(re.search("NPC[0-9]+", p1.name))
        self.assertEqual(p1.stats, dict(ST=10, DX=10, IQ=10, HT=10))
        self.assertTrue(re.search("NPC[0-9]+", p2.name))
        self.assertNotEqual(p1.name, p2.name)

    def testStatsInitiation(self):
        p1 = Character("zack", 12, 15, 10, 9)
        p2 = Character("noob", 10, 7, 10, 7)

        self.assertEqual(p1.name, "zack")
        self.assertEqual(p2.name, "noob")


class WeaponNotEquippedTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Character()

    def testNoWeaponEval(self):
        self.assertEqual(self.p1.attack_bonus, self.p1.base_attack_bonus)


class WeaponEquippedTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Character()
        w = Weapon("melee", 1, (1, 2))
        self.p1.equip_primary_weapon(w)

    def testEquip(self):
        self.assertEqual(self.p1.attack_bonus, 1)
        self.assertNotEqual(self.p1.attack_bonus, self.p1.base_attack_bonus)

    def testUnequipWrongWay(self):
        self.assertNotEqual(self.p1.base_attack_bonus, self.p1.attack_bonus)
        # self.assertRaises(InvalidEquipmentError, self.p1.equip_primary_weapon, None)
        self.assertNotEqual(self.p1.base_attack_bonus, self.p1.attack_bonus)

    def testUnequip(self):
        self.p1.unequip_primary_weapon()
        self.assertEqual(self.p1.base_attack_bonus, self.p1.attack_bonus)


# defense

class DefenseTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Character()

    def testBaseDef(self):
        self.assertEqual(self.p1.base_defense_bonus, 0)
        self.p1.dx = 20
        self.assertEqual(self.p1.base_defense_bonus, 5)

    def testDef(self):
        self.assertEqual(self.p1.defense_bonus, 0)