from .player import Player
# Hold Grudges => Once opponent defects, you always defect


class Friedman(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)
        self.defected = False

    def play(self, opponent_prev_move):
        if self.round == 1:
            return 1
        elif self.defected:
            return 0
        elif opponent_prev_move == 0:
            self.defected = True
            return 0
        else:
            return 1

    def reset(self):
        self.defected = False
        self.round = 1
