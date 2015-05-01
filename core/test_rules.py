"""

print("p1 base attack %+d " % p1.base_attack_bonus)
print("p2 base attack %+d" % p2.base_attack_bonus)

p1.equip_weapon(sword)
print(p1.weapon_full_attack(p2))
print(p2.weapon_full_attack(p1))

"""
import unittest

from core.character import Character
from core import rules
from core.weapon import dagger, long_sword


class JRPGAttackTests(unittest.TestCase):
    def setUp(self):
        self.p1 = Character()
        self.p2 = Character()
        self.mwfar = rules.JRRPGRules.attack_resolution
        # d20 =   MagicMock(return_value=19) just not to forget

    def test_main_weapon_full_attack_resolution_barehands(self):
        rules.d20 = object()
        rules.d20 = 3
        self.assertEqual(self.mwfar(self.p1, self.p2), (-7, "miss"))

        rules.d20 = 10
        self.assertEqual(self.mwfar(self.p1, self.p2), (0, "hit"))

        rules.d20 = 20
        self.assertEqual(self.mwfar(self.p1, self.p2), (10, "critical hit"))

        rules.d20 = 1  # mocking
        self.assertEqual(self.mwfar(self.p1, self.p2), (-9, "critical miss"))

    def test_dagger_full_attack(self):
        self.p1.equip_primary_weapon(dagger)
        rules.d20 = 19
        self.assertEqual(self.mwfar(self.p1, self.p2), (9, "critical hit"))

    def test_long_sword_full_attack(self):
        self.p1.equip_primary_weapon(long_sword)
        rules.d20 = 19
        self.assertEqual(self.mwfar(self.p1, self.p2), (10, "hit"))