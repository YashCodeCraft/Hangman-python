import random

MAX_ROUNDS = 11
MIN_ROUNDS = 3
possibilities = ['r', 'p', 's']


def round_played():
    while True:
        rounds = input(f"Total number of rounds you like to Play ({MIN_ROUNDS}-{MAX_ROUNDS}): ")
        if rounds.isdigit():
            rounds = int(rounds)
            if MIN_ROUNDS <= rounds <= MAX_ROUNDS:
                break
            else:
                print(f"you should enter between {MIN_ROUNDS} to {MAX_ROUNDS}!")
        else:
            print("Please enter in number!!")
    return rounds


def play():
    input("Welcome to rock, paper and scissor! Click enter to continue..")
    comp_count, user_count, tie_count = 0, 0, 0
    tot_round = round_played()
    for Round in range(tot_round):
        print()
        print(f"Round {Round + 1}:")
        comp_guess = random.choice(["r", "p", "s"])
        user_guess = input("Guess 'r' as a rock or 'p' as a paper or 's' as a scissor---> ").lower()
        if user_guess not in possibilities:
            print("Invalid!!!. Guess a valid value in Next round...")
        else:
            if user_guess == comp_guess:
                print(f"Comp = {comp_guess}\n<<<---TIE--->>>")
                tie_count += 1
                print(f"No of ties: {tie_count}")
                print(f"No of wins by you: {user_count}")
                print(f"No of wins by comp: {comp_count}")
            elif is_win(user_guess, comp_guess):
                print(f"Comp = {comp_guess}\n<<<---!!|YOU WIN|!!--->>>")
                user_count += 1
                print(f"No of ties: {tie_count}")
                print(f"No of wins by you: {user_count}")
                print(f"No of wins by comp: {comp_count}")
            elif is_loss(user_guess, comp_guess):
                print(f"Comp = {comp_guess}\n<<<---xxX-COMP WON-Xxx--->>>")
                comp_count += 1
                print(f"No of ties: {tie_count}")
                print(f"No of wins by you: {user_count}")
                print(f"No of wins by comp: {comp_count}")
    print()
    print(f"Computer = {comp_count}")
    print(f"You = {user_count}")
    print(f"Ties = {tie_count}")
    if comp_count > user_count:
        print(f"Total round = {tot_round}")
        print("Better luck next time..Computer has won the match.....!!!")
    elif comp_count < user_count:
        print(f"Total round = {tot_round}")
        print("BANG!!!..You won the match...!")
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
