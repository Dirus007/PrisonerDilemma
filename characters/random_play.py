import random
from .player import Player


class Random(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)

    def play(self, opponent_prev_move):
        return 1 if random.random() < 0.5 else 0

    def reset(self):
        self.round = 1
