import characters
import random
import copy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def tournament(players, times, noise, rounds):
    # Store unique player names only
    players_names = list(set([player.name for player in players]))
    df_scores = pd.DataFrame(index=players_names, columns=players_names)
    df_scores = df_scores.fillna(0)

    n = len(players)
    for _ in range(times):
        for i in range(n):
            for j in range(0, i+1):
                # make sure player_a and player_b are deep copies, not copy by refernce
                player_a = copy.deepcopy(players[i])
                player_b = copy.deepcopy(players[j])
                a_score, b_score = play_rounds(player_a, player_b, rounds, noise)
                df_scores.at[player_a.name, player_b.name] += a_score
                df_scores.at[player_b.name, player_a.name] += b_score

    return df_scores


def play_rounds(player1, player2, rounds, noise):
    player1_score = 0
    player2_score = 0
    player_1_prev_move = 1
    player_2_prev_move = 1
    for i in range(rounds):
        player1_move = player1.play(player_2_prev_move)
        player2_move = player2.play(player_1_prev_move)

        if random.random() < noise:
            player1_move = 1 - player1_move
        if random.random() < noise:
            player2_move = 1 - player2_move

        player1_score += player1.update_points(player2_move, player1_move)
        player2_score += player2.update_points(player1_move, player2_move)

        player_1_prev_move = player1_move
        player_2_prev_move = player2_move

    player1.reset()
    player2.reset()

    return player1_score, player2_score

def main():
    # Initialize base player with game settings
    total_rounds = 500
    base_player = characters.Player(both_coop=2, both_cheat=0, you_cheat=3, they_cheat=-1, rounds=total_rounds)
    noise = 0.1

    AlwaysCoop = characters.AlwaysCoop(base_player, name='AlwaysCoop')
    Cheater = characters.Cheater(base_player, name='Cheater')
    GTFT = characters.Generous_Tit_For_Tat(base_player, generosity=0.3, name='GTFT')
    TFT = characters.Tit_For_Tat(base_player, name='TFT')
    Random = characters.Random(base_player, name='Random')
    Friedman = characters.Friedman(base_player, name='Friedman')
    Sample = characters.Sample(base_player, name='Sample')
    Joss = characters.Joss(base_player, name='Joss', defect_prob=0.1)
    Tester = characters.Tester(base_player, name='Tester')

    players = [AlwaysCoop, Cheater, GTFT, TFT, Random,
               Friedman, Sample, Joss, Tester]

    # Play tournament
    df_scores = tournament(players, 10, noise, total_rounds)
    normalized_df = df_scores / df_scores.max().max()
    plt.figure(figsize=(10, 8))
    sns.heatmap(normalized_df, annot=True, cmap='viridis')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
    plt.yticks(rotation=0)  # Rotate y-axis labels
    plt.tight_layout()
    plt.title('Matrix of Player Performance')
    plt.show()


if __name__ == "__main__":
    main()
