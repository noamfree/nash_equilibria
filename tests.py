import unittest

from equilibria import *


class EquilibriaTest(unittest.TestCase):
    def setUp(self):
        self.opp = StrategyProfile(1)

    def test_payment(self):
        game = Game([[1]], payments={self.opp: (5,)})
        self.assertEqual(game.payment(self.opp), (5,))


    def test_one_palyer_one_strategy(self):
        game = Game([[1]],payments={self.opp:(5,)})
        self.assertEqual( game.check_if_equilibrium(self.opp), True)

    def test_creating_profile(self):
        profile = StrategyProfile(1, 5, 3)
        self.assertEqual(profile[1], 5)