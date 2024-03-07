from .player import Player
# Tit for two tats => defects when 2 defects twice in a row


class Sample(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)
        self.defected1 = False
        self.defected2 = False

    def play(self, opponent_prev_move):
        self.defected2 = self.defected1
        self.defected1 = (opponent_prev_move == 0)
        if self.round == 1:
            return 1
        elif self.defected1 and self.defected2:
            return 0
        else:
            return 1

    def reset(self):
        self.defected1 = False
        self.defected2 = False
        self.round = 1
