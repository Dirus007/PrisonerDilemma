from .player import Player
import random


class Generous_Tit_For_Tat(Player):
    def __init__(self, player, generosity, name):
        super().__init__(player=player, name=name)
        self.generosity = generosity

    def play(self, opponent_prev_move):
        if self.round == 1:
            return 1
        else:
            if random.random() < self.generosity:
                return 1
            else:
                return opponent_prev_move

    def reset(self):
        self.round = 1
