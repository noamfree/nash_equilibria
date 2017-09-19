"""
author: noam.freeman
"""
from copy import copy


class StrategyProfile:
    def __init__(self, *strategies):
        self.strategies = list(strategies)

    def __getitem__(self, item):
        return self.strategies[item]

    def __setitem__(self, key, value):
        self.strategies[key] = value

    def __len__(self):
        return self.strategies.__len__()

    def __eq__(self, other):
        print(self)
        print(other)
        return self.strategies == other .strategies

    def __hash__(self):
        return hash(tuple(self.strategies))

    def __repr__(self):
        return "Stratege Profile" + str(self.strategies)

    def replace_single_strategy_in_profile(self, player_replacing_strategy,
                                           replacing_strategy):
        new_profile = copy(self)
        new_profile[player_replacing_strategy] = replacing_strategy
        return new_profile


class Game:
    """
    represents a game in the game theory sense.
    a game has N players.
    each player has a set of strategies he can choose to play.
    when each of the players "chooses" a strategy - we get a
    strategy-profile.

    additionally, the game has a payment-table, which says what is the
    payment of each player, at each strategy-profile.
    """
    def __init__(self, strategies, payments):
        self.num_of_players = len(strategies)
        self.strategies = strategies
        self.payments = payments

    def check_if_equilibrium(self, strategy_profile: StrategyProfile):
        for player in range(self.num_of_players):
            if self.find_better_option(player, strategy_profile):
                return False
        return True

    def payment(self, strategy_profile: StrategyProfile):
        return self.payments[strategy_profile]

    def find_better_option(self, player, strategy_profile: StrategyProfile):
        """
        find a better stategy for a player, given a profile
        :param player:
        :param strategy_profile:
        :return: returns a better strategy if thers is. None else
        """
        current_payment = self.payment(strategy_profile)
        player_strategies = self.get_strategies_of_player(player)
        for strategy in player_strategies:
            new_profile = strategy_profile.\
                replace_single_strategy_in_profile(player, strategy)
            new_payment = self.payment(new_profile)
            if new_payment > current_payment:
                return strategy
        return None

    def get_strategies_of_player(self, player):
        return self.strategies[player]
