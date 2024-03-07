from .player import Player


class Tit_For_Tat(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)

    def play(self, opponent_prev_move):
        if self.round == 1:
            return 1
        else:
            return opponent_prev_move

    def reset(self):
        self.round = 1
