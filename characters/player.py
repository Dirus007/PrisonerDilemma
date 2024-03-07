class Player:
    def __init__(self, both_coop=None, both_cheat=None, you_cheat=None, they_cheat=None, rounds=None, noise=None, player=None, name=None):
        if player:
            self.both_coop = player.both_coop
            self.both_cheat = player.both_cheat
            self.you_cheat = player.you_cheat
            self.they_cheat = player.they_cheat
            self.rounds = player.rounds
            self.round = player.round
        else:
            self.both_coop = both_coop
            self.both_cheat = both_cheat
            self.you_cheat = you_cheat
            self.they_cheat = they_cheat
            self.rounds = rounds
            self.round = 1
        self.name = name
        self.noise = noise
        self.total_played = 0
        self.score_matrix = [[self.both_cheat, self.you_cheat], [self.they_cheat, self.both_coop]]

    def update_points(self, opponent_move, self_move):
        self.round += 1
        self.total_played += 1

        return self.score_matrix[self_move][opponent_move]

    def play(self, opponent_prev_move):
        raise NotImplementedError("This method should be overridden.")

    def reset_round(self):
        self.round = 1

    def announce_score(self):
        print(f'{self.name} Player Score : {self.score}')
