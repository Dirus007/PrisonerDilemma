from .player import Player
# Always Cheats


class Cheater(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)

    def play(self, opponent_prev_move):
        return 0

    def reset(self):
        self.round = 1
