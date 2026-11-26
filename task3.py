
import random

authorised_names = ["davut",'aylar' ]
authorised_passwords = ["aylar",'davut']


def authenticate(player_number):

    print("\nPlayer", player_number, "Login")

    attempts = 3

    while attempts > 0:

        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name in authorised_names:

            position = authorised_names.index(name)

            if password == authorised_passwords[position]:
                print("Login successful!")
                return name

        attempts = attempts - 1
        print("Incorrect details. Attempts left:", attempts)

    return ""


def create_deck():

    deck = []

    colours = ["Red", "Black", "Yellow"]

    for colour in colours:

        for number in range(1, 11):

            card = colour + " " + str(number)
            deck.append(card)

    random.shuffle(deck)

    return deck


def display_card(card):

    parts = card.split(" ")

    colour = parts[0]
    number = parts[1]

    print(colour, number)


def find_winner(card1, card2):

    parts1 = card1.split(" ")
    parts2 = card2.split(" ")

    colour1 = parts1[0]
    number1 = int(parts1[1])

    colour2 = parts2[0]
    number2 = int(parts2[1])

    if colour1 == colour2:

        if number1 > number2:
            return 1

        else:
            return 2

 
    elif (colour1 == "Red" and colour2 == "Black") or \
         (colour1 == "Yellow" and colour2 == "Red") or \
         (colour1 == "Black" and colour2 == "Yellow"):

        return 1

    else:
        return 2


def save_result(name, quantity):

    file = open("results.txt", "a")

    file.write(name + "," + str(quantity) + "\n")

    file.close()


def display_top_players():

    names = []
    quantities = []

    try:

        file = open("results.txt", "r")

        for line in file:

            line = line.strip()

            if line != "":

                parts = line.split(",")

                names.append(parts[0])
                quantities.append(int(parts[1]))

        file.close()

    except FileNotFoundError:

        print("No previous results found.")
        return

    for i in range(len(quantities)):

        for j in range(len(quantities) - 1):

            if quantities[j] < quantities[j + 1]:

                temp = quantities[j]
                quantities[j] = quantities[j + 1]
                quantities[j + 1] = temp

                temp = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temp

    print("\n===== TOP 5 PLAYERS =====")

    for i in range(min(5, len(names))):

        print(i + 1, ".", names[i], "-", quantities[i], "cards")



print("================================")
print("       CARD GAME")
print("================================")

player1 = authenticate(1)

if player1 != "":

    player2 = authenticate(2)

    if player2 != "" and player1 != player2:

        print("\nBoth players are authorised!")
        print("The game is starting...\n")

        deck = create_deck()

        player1_cards = []
        player2_cards = []

        round_number = 1

        while len(deck) >= 2:

            print("\n===== ROUND", round_number, "=====")

            card1 = deck.pop(0)
            card2 = deck.pop(0)

            print(player1, "draws:")
            display_card(card1)

            print(player2, "draws:")
            display_card(card2)

            winner = find_winner(card1, card2)

            if winner == 1:

                print(player1, "wins this round!")

                player1_cards.append(card1)
                player1_cards.append(card2)

            else:

                print(player2, "wins this round!")

                player2_cards.append(card1)
                player2_cards.append(card2)

            round_number = round_number + 1

        score1 = len(player1_cards)
        score2 = len(player2_cards)

        print("\n================================")
        print("          FINAL RESULTS")
        print("================================")

        print(player1, ":", score1, "cards")
        print(player2, ":", score2, "cards")

        if score1 > score2:

            winner_name = player1
            winner_cards = player1_cards

        else:

            winner_name = player2
            winner_cards = player2_cards

        print("\nThe overall winner is:", winner_name)

        print("\nCards held by", winner_name, ":")

        for card in winner_cards:

            display_card(card)

        save_result(winner_name, len(winner_cards))

        print("\nWinner's result saved successfully!")

        display_top_players()

    elif player2 == "":

        print("Player 2 authentication failed.")

    else:

        print("Two different players are required.")

else:

    print("Player 1 authentication failed.")
