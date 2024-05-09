import random

MAX_ROUNDS = 13
MIN_ROUNDS = 5
possibilities = ['r', 'p', 's']


def round_played():
    while True:
        rounds = input(f"How many rounds would you like to Play? ({MIN_ROUNDS}-{MAX_ROUNDS}): ")
        if rounds.isdigit():
            rounds = int(rounds)
            if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
                break
            else:
                print(f"Please enter value between {MIN_ROUNDS} and {MAX_ROUNDS}!")
        else:
            print("Please enter the valid number!!")
    return rounds


def play():
    print()
    print("Welcome to rock, paper and scissor! \n1.You can choose the number of rounds you wish to play.")
    print("2.The one who wins the most rounds, will be a winner!")
    print()
    input("Click enter to continue..")
    print()
    comp_count, user_count, tie_count = 0, 0, 0
    tot_round = round_played()
    for Round in range(tot_round):
        print()
        print(f"ROUND {Round + 1}:")
        while True:
            comp_guess = random.choice(["r", "p", "s"])
            user_guess = input("Guess 'r' as a ROCK or 'p' as a PAPER or 's' as a SCISSOR---> ").lower()
            if user_guess not in possibilities:
                print("Invalid!!!. Guess a valid value..!")
            else:
                if user_guess == comp_guess:
                    print(f"Comp = {comp_guess}\n<<<---TIE--->>>")
                    tie_count += 1
                    print(f"Number of ties: {tie_count}")
                    print(f"Number of wins by you: {user_count}")
                    print(f"Number of wins by comp: {comp_count}")
                    break
                elif is_win(user_guess, comp_guess):
                    print(f"Comp = {comp_guess}\n<<<---!!|YOU WIN|!!--->>>")
                    user_count += 1
                    print(f"Number of ties: {tie_count}")
                    print(f"Number of wins by you: {user_count}")
                    print(f"Number of wins by comp: {comp_count}")
                    break
                elif is_loss(user_guess, comp_guess):
                    print(f"Comp = {comp_guess}\n<<<---xxX-COMP WIN-Xxx--->>>")
                    comp_count += 1
                    print(f"Number of ties: {tie_count}")
                    print(f"Number of wins by you: {user_count}")
                    print(f"Number of wins by comp: {comp_count}")
                    break
    print()
    print(f"Computer = {comp_count}")
    print(f"You = {user_count}")
    print(f"Ties = {tie_count}")
    if comp_count > user_count:
        print(f"Total round = {tot_round}")
        print("Better luck next time..Computer has won the Game.....!!!")
    elif comp_count < user_count:
        print(f"Total round = {tot_round}")
        print("BANG!!!..You won the Game...!")
    elif comp_count == user_count:
        print(f"Total round = {tot_round}")
        print("The match was tie..!")


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or \
            (player == "s" and opponent == "p"):
        return True


def is_loss(player, opponent):
    if (player == "r" and opponent == "p") or (player == "p" and opponent == "s") or \
            (player == "s" and opponent == "r"):
        return True


play()
