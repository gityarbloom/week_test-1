from utils.deck import *

def create_player(name:str="AI"):
    player = {"player_name": name, "hand": [], "won_pile": []}
    return player


def init_game():
    player_1 = create_player("p1")
    player_2 = create_player()
    deck = create_deck()
    deck = shuffle(deck)
    player_1["hand"] = deck[:27]
    player_2["hand"] = deck[27:]
    game_dict = {"deck": deck, "player_1": player_1, "player_2": player_2}
    return game_dict


def play_round(player_1: dict, player_2: dict):
    p1_card = player_1["hand"].pop()
    p2_card = player_2["hand"].pop()
    the_winner = compare_cards(p1_card, p2_card)
    if the_winner == "p1":
        player_1["won_pile"].append(p1_card)
        player_1["won_pile"].append(p2_card)
        print("player_1 won")
    elif the_winner == "p2":
        player_2["won_pile"].append(p1_card)
        player_2["won_pile"].append(p1_card)
        print("player_2 won")
    return None
