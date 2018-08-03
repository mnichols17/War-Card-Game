from player import Player

player_1 = Player()
player_2 = Player()

print("WAR SIMULATOR")

def compare_cards(points):
    card_1, player_1_left = player_1.get_card()
    card_2, player_2_left = player_2.get_card()
    name_1 = card_name(card_1)
    name_2 = card_name(card_2)

    print("Player 1: {} vs Player 2: {}".format(name_1, name_2))

    if(card_1 > card_2):
        player_1.add_score(points)
    elif(card_1 < card_2):
        player_2.add_score(points)
    else:
        print("TIE!. New cards will be picked and a win is now worth {}".format(points + 1))
        compare_cards(points + 1)

    return player_1_left

def scoreboard():
    print("Player 1: {}\nPlayer 2: {}".format(player_1.score, player_2.score))

def card_name(value):
    if(value == 1):
        return "Ace (1)"
    elif(value == 11):
        return "Jack (11)"
    elif(value == 12):
        return "Queen (12)"
    elif(value == 13):
        return "King (13)"
    else:
        return str(value)

def game_over(message):
    scoreboard()
    print(message, end=' ')
    if(player_1.score > player_2.score):
        print("Player 1 Wins!\n")
    elif(player_1.score < player_2.score):
        print("Player 2 Wins!\n")
    else:
        print("TIE!\n")

while True:
    print("\nThe battle is starting...")

    if (compare_cards(1) == 0):
        game_over("\nThere are no more cards left.")
        break
    else:
        scoreboard()
        print("Continue? (Y/N)")
        choice = input("> ")
        if ("N" in choice.upper()):
            game_over("\nYou ended the game.")
            break
