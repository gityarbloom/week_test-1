from game_logic.game import play_round, init_game
def start_game():
    new_game = init_game()
    while new_game["player_1"]["hand"] and new_game["player_2"]["hand"]:
        input()
        play_round(new_game["player_1"], new_game["player_2"])
    if len(new_game["player_1"]["won_pile"]) > len(new_game["player_2"]["won_pile"]):
        return "player_1 won finiatly"
    elif len(new_game["player_2"]["won_pile"]) > len(new_game["player_1"]["won_pile"]):
        return "player_2 won finiatly"
    return "there is no a winner"

if __name__ == "__main__":
    print(start_game())