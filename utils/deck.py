from random import randint

def create_card(rank:str, suite:str):
    card = {"rank": rank, "suite": suite}
    if card["rank"] == "J":
        card["value"] = 11
    elif card["rank"] == "Q":
        card["value"] = 12
    elif card["rank"] == "K":
        card["value"] = 13
    elif card["rank"] == "A":
        card["value"] = 14
    else:
        card["value"] = int(card["rank"])
    return card


def compare_cards(p1_card:dict, p2_card:dict):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    return "WAR"



def create_deck():
    packet = []
    suits_cards = ["H", "C", "D", "S"]
    for suit in suits_cards:
        for rank in range(2, 15):
            if rank < 11:
                new_card = create_card(str(rank), suit)
            else:
                if rank == 11:
                    new_card = create_card("J", suit)
                elif rank == 12:
                    new_card = create_card("Q", suit)
                elif rank == 13:
                    new_card = create_card("K", suit)
                else:
                    new_card = create_card("A", suit)
            packet.append(new_card)
    return packet


def shuffle(deck: list[dict]):
    for i in range(1000):
        index1 = randint(0, 51)
        index2 = randint(0, 51)
        if index1 == index2:
            continue
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck

# unmixed_cards_deck = create_deck()
# mixed_cards_deck = shuffle(unmixed_cards_deck)
