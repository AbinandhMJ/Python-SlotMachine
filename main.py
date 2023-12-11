import random
import datetime

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "💎": 5, "🍋": 7, "🍊": 6, "🍒": 4, "🍇": 3, "🔔": 2, "🎰": 1,
    "⭐": 2, "🍎": 5, "🍓": 6, "🍈": 4, "🍑": 3, "🍌": 2, "🍍": 1,
    "🍏": 3, "🍐": 4, "🍅": 5, "🌽": 6, "🥦": 7, "🍆": 8, "🥕": 7,
    "🍠": 6, "🥔": 5, "🌶": 4, "🍄": 3, "🌰": 2, "🍞": 1, "🧀": 2,
    "🍖": 3, "🍗": 4, "🍤": 3, "🍥": 2, "🍨": 1, "🍧": 2, "🍦": 3,
    "🍩": 4, "🍪": 5, "🍰": 6, "🎂": 7, "🍫": 8, "🍬": 9, "🍭": 8,
    "🍮": 7, "🍯": 6,
}

symbol_value = {symbol: random.randint(1, 5) for symbol in symbol_count}

timing = datetime.datetime.now()


# Check Winning
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Spin the Machine
def get_slot_machine_spin(rows, cols, symbols):
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


# Displaying Game
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# Deposit Amount for the game
def deposit():
    print("Welcome to SLOT MACHINE GAME 🎰")
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


# Get the Number of lines to bet
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


# Get the bet Amount
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


# Spin
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} 🤑")
    print(f"You won on lines:", *winning_lines)
    print(f"Winning Time ⏱️ {timing}")
    return winnings - total_bet


# Main Function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance} 💸")
        answer = input("Press Enter to play 🎮 or q to quit ✖️")
        if answer == "q" or answer == "Q":
            break
        balance += spin(balance)

    print(f"You left with ${balance} on ⏱️ {timing} \n Thankyou for Gaming with us!...")


main()
