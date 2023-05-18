import random


def print_intructions():
    print("\n--------------------------------------------------")
    print("Let's play Rock-Paper-Scissors!")
    print("Choose one: (R) Rock, (P) Paper, (S) Scissors")
    print("--------------------------------------------------\n")


def get_players_choice():
    return input("\nEnter your choice (R/P/S): ").upper()


def get_rps_outcome(bot_choice, player_choice):
    if bot_choice == player_choice:
        return "It's a tie!"
    elif (bot_choice == "S" and player_choice == "R") or \
         (bot_choice == "R" and player_choice == "P") or \
         (bot_choice == "P" and player_choice == "S"):
        return "Player Wins!"
    else:
        return "Bot Win! Haha, loser!"


def play_game():
    choices = ["R", "P", "S"]
    still_playing = True

    print_intructions()

    while still_playing:
        player_choice = get_players_choice()

        while player_choice not in choices:
            player_choice = get_players_choice()

        bot_choice = random.choice(choices)

        print("You chose:", player_choice)
        print("Computer chose:", bot_choice)
        print(get_rps_outcome(bot_choice, player_choice))

        still_playing = input("\nPlay again? (y/n): ")

        if still_playing.lower() != 'y':
            still_playing = False
    print("Game is ending.. thanks for playing!")


if __name__ == "__main__":
    play_game()
