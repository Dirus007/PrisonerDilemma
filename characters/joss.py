from .player import Player
import random
# Copies last move, defects at small prob


class Joss(Player):
    def __init__(self, player, name, defect_prob=0.1):
        super().__init__(player=player, name=name)
        self.defect_prob = defect_prob

    def play(self, opponent_prev_move):
        if self.round == 1:
            return 1
        if opponent_prev_move == 0:
            return 0
        else:
            return 0 if random.random() < self.defect_prob else 1

    def reset(self):
        self.round = 1
