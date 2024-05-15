import random

possibilities = [1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]


def game_user_bat(TotalBalls, Name):
    user_runs, comp_runs, user_scored, comp_scored, wick_count, tot_wick = 0, 0, 0, 0, 0, 2
    print()
    print(f"{Name} will bat first...")
    print()
    print("1ST INNINGS")
    for ball in TotalBalls:
        print(f"Ball {ball}")
        while True:
            comp_bowl = random.choice(possibilities)
            user_bat = input("Enter the number between (1 - 6) to hit: ")
            if user_bat.isdigit():
                user_bat = int(user_bat)
                if user_bat in possibilities:
                    print("Comp bowls:", comp_bowl)
                    if user_bat == comp_bowl:
                        wick_count += 1
                        print("Wicket!!")
                        print(f"{Name}'s Wicket number {wick_count}")
                        print(f"Your score by now: {user_scored}-{wick_count}")
                        if wick_count == 2:
                            print()
                            print(f"Oops!..you are out!!")
                            print()
                            break
                        else:
                            break
                    else:
                        user_scored += user_bat
                        user_runs += user_bat
                        print(f"Your score by now: {user_scored}-{wick_count}")
                        break
                else:
                    print("Please enter the value between 1 and 6")
            else:
                print("Please enter the valid input.")
        if wick_count == 2:
            break
        print()
    print(f"{Name} has totally Scored: {user_runs}-{wick_count}")

    print()
    print(f"comp need {user_runs + 1} RUNS to win in {len(TotalBalls)} BALLS!")
    wick_count = 0
    target_runs = user_runs + 1
    print()
    print("2ND INNINGS")
    for ball in TotalBalls:
        print(f"Ball {ball}")
        comp_bat = random.choice(possibilities)
        while True:
            user_bowl = input("Enter the number between (1 - 6) to Bowl: ")
            if user_bowl.isdigit():
                user_bowl = int(user_bowl)
                if user_bowl in possibilities:
                    print("computer strikes = ", comp_bat)
                    '''target_runs -= comp_bat'''
                    if user_bowl == comp_bat:
                        wick_count += 1
                        print("Wicket!!")
                        print(f"Comp's wicket no {wick_count}")
                        if wick_count == 2:
                            print("The computer was out!!")
                            print()
                            break
                        else:
                            print(f"Computer need {target_runs} more runs in {len(TotalBalls) - ball} balls!.")
                            print(f"Comp score by now: {comp_scored}-{wick_count}")
                            break
                    else:
                        target_runs -= comp_bat
                        comp_scored += comp_bat
                        comp_runs += comp_bat
                        print(f"Comp score by now: {comp_scored}-{wick_count}")
                        if comp_runs > user_runs:
                            break
                        else:
                            print(f"Computer need {target_runs} more runs in {len(TotalBalls) - ball} balls!.")
                        break
                elif user_bowl not in possibilities:
                    print("Please enter the value between 1 and 6")
            else:
                print('Please Enter a valid value!')
        if wick_count == 2:
            break
        elif comp_runs > user_runs:
            print(f"computer has chased {user_runs} Runs and won by {tot_wick - wick_count} wickets!!")
            break
        print()
    print(f"Computer scored: {comp_runs}-{wick_count}")
    print()
    if comp_runs < user_runs:
        print(f"{Name} won by {user_runs - comp_runs} Runs!!")
    elif user_runs == comp_runs:
        print(f"Match was tie.({comp_runs} Runs)!!")


def game_comp_bat(TotalBalls, Name):
    user_runs, comp_runs, user_scored, comp_scored, wick_count, tot_wick = 0, 0, 0, 0, 0, 2
    print()
    print("Comp bat first...")
    print()
    print("1ST INNINGS")
    for ball in TotalBalls:
        print(f"Ball {ball}")
        comp_bat = random.choice(possibilities)
        while True:
            user_bowl = input("Enter the number between (1 - 6) to Bowl: ")
            if user_bowl.isdigit():
                user_bowl = int(user_bowl)
                if user_bowl in possibilities:
                    print("computer strikes = ", comp_bat)
                    if user_bowl == comp_bat:
                        wick_count += 1
                        print("Wicket!!")
                        print(f"Comp's wicket no {wick_count}")
                        print(f"Comp score by now: {comp_scored}-{wick_count}")
                        if wick_count == 2:
                            print("The computer was out!!")
                            print()
                            break
                        else:
                            break
                    else:
                        comp_scored += comp_bat
                        comp_runs += comp_bat
                        print(f"Comp score by now: {comp_scored}-{wick_count}")
                        break
                elif user_bowl not in possibilities:
                    print("Please enter the value between 1 and 6")
            else:
                print("Please enter the valid value!")
        if wick_count == 2:
            break
        print()
    print(f"Total runs by Comp: {comp_runs}-{wick_count}")

    print()
    print(f"{Name} need {comp_runs + 1} RUNS to win in {len(TotalBalls)} BALLS!")
    wick_count = 0
    target_runs = comp_runs + 1
    print()
    print("2ND INNINGS")
    for ball in TotalBalls:
        print(f"Ball {ball}")
        while True:
            comp_bowl = random.choice(possibilities)
            user_bat = input("Enter the number between (1 - 6) to hit: ")
            if user_bat.isdigit():
                user_bat = int(user_bat)
                if user_bat in possibilities:
                    print("Comp bowls:", comp_bowl)
                    if user_bat == comp_bowl:
                        wick_count += 1
                        print("Wicket!!")
                        print(f"{Name}'s Wicket number {wick_count}")
                        if wick_count == 2:
                            print(f"Oops!..you are out!!")
                            print()
                            break
                        else:
                            print(f"{Name} need {target_runs} more runs in {len(TotalBalls) - ball} balls!.")
                            print(f"Your score by now: {user_scored}-{wick_count}")
                            break
                    else:
                        target_runs -= user_bat
                        user_scored += user_bat
                        user_runs += user_bat
                        print(f"Your score by now: {user_scored}-{wick_count}")
                        if user_runs > comp_runs:
                            print(f"{Name} chased {comp_runs} Runs and won by {tot_wick - wick_count} wickets!!")
                            return
                        else:
                            print(f"{Name} need {target_runs} more runs in {len(TotalBalls) - ball} balls!.")
                        break
                else:
                    print("Please enter the value between 1 and 6")
            else:
                print("Please enter the valid input.")
        if wick_count == 2:
            break
        print()
    print(f"{Name} has totally Scored: {user_runs}-{wick_count}")
    print()
    if user_runs < comp_runs:
        print(f"Comp won by {comp_runs - user_runs} Runs!!")
    elif user_runs == comp_runs:
        print(f"Match was tie.({comp_runs} Runs)!!")


def user_won_toss(TotalBalls, Name):
    while True:
        user_dec = input(f"You've won the toss! Do you prefer to BAT (b) or BOWL (f)? ").lower()
        if user_dec == "b":
            game_user_bat(TotalBalls, Name)
            break
        elif user_dec == "f":
            game_comp_bat(TotalBalls, Name)
            break
        else:
            print("Please enter the valid input (b or f)")
            print()


def comp_won_toss(TotalBalls, Name):
    comp_dec = random.choice(["b", "f"])
    if comp_dec == "b":
        print("The computer has won the toss and elected to BAT first!")
        game_comp_bat(TotalBalls, Name)
    elif comp_dec == "f":
        print("The computer has won the toss and elected to BOWL first!")
        game_user_bat(TotalBalls, Name)


def play():
    global TotalBalls
    print()
    print("Lets play Hand Cricket with Computer..")
    name = input("Enter your team name: ")
    print()
    print("Instructions:")
    print("1.Each team has two wickets.")
    print("2.If the batsman and bowler both choose the same number, the batsman is dismissed.")
    print("3.Picking higher numbers (4s, 5s, and 6s) during batting increases the risk of losing a wicket.")
    print()
    input("Click enter to continue!! ")
    while True:
        no_of_overs = input("Choose the number of overs you'd like to play, from 1 to 4: ")
        if no_of_overs.isdigit():
            no_of_overs = int(no_of_overs)
            if 1 <= no_of_overs <= 4:
                if no_of_overs == 1:
                    TotalBalls = range(1, 6 + 1)
                elif no_of_overs == 2:
                    TotalBalls = range(1, 12 + 1)
                elif no_of_overs == 3:
                    TotalBalls = range(1, 18 + 1)
                elif no_of_overs == 4:
                    TotalBalls = range(1, 24 + 1)
                break
            else:
                print("Please input a number of overs between 1 and 4.")
        else:
            print("Please enter the valid value.")

    print()
    comp_toss = random.choice(possibilities)
    print(f"TOSS TIME!!\nEVEN - {name}, ODD - Computer")
    while True:
        user_toss = input("Guess the number between 1 and 6: ")
        if user_toss.isdigit():
            user_toss = int(user_toss)
            if 1 <= user_toss <= 6:
                break
            else:
                print("Please input a number of value between 1 and 6")
        else:
            print("Please enter the valid value.")
        print()
    add_or_even = comp_toss + user_toss
    if add_or_even % 2 == 0:
        print("Comp:", comp_toss)
        user_won_toss(TotalBalls, name)
    elif add_or_even % 2 != 0:
        print("Comp:", comp_toss)
        comp_won_toss(TotalBalls, name)
    return TotalBalls, name


play()
