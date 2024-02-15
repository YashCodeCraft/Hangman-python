import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_list = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_list.append(line+1)
    return winnings, winning_list


def deposit():
    while True:
        amount = input("Enter the amount that you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("You shit. Amount must be grater than zero!")
        else:
            print("You should deposit a amount. Enter in number.")
    return amount


def get_bet():
    while True:
        amount = input("Enter the amount that you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else:
                print(f"You shit. Amount must be between ${MIN_BET}-${MAX_BET}!")
        else:
            print("You should bet a amount. Enter in number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines: (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("You shit. Line must be from 1 to 3!")
        else:
            print("Enter in number.")
    return lines


def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"The money is ${total_bet}. You dont have enough money to bet. You have ${balance}")
        else:
            break
    print(f"The total bet should be ${total_bet}")

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_list = check_winnings(slots, lines, bet, symbol_value)
    print(f"You have won ${winnings}")
    print("You won on lines", *winning_list)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is {balance}")
        answer = input("Click enter to play(q to quit).").lower()
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You have left ${balance}.")


main()
