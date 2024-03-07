from .player import Player
# Start by defecting, if opponent retaliate apologize


class Tester(Player):
    def __init__(self, player, name):
        super().__init__(player=player, name=name)
        self.take_benefit = False

    def play(self, opponent_prev_move):
        if self.round == 1:
            return 0
        elif self.round == 2:
            if opponent_prev_move == 0:
                self.take_benefit = False
                return 1
            else:
                self.take_benefit = True
                return 0

        elif self.take_benefit:
            return 0
        else:
            return opponent_prev_move

    def reset(self):
        self.take_benefit = False
        self.round = 1

