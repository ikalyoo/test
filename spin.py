# Python slot machine
import random as rand
import time

def spin_row():
    icon = ["🍒", "🍋", "🍊"] 
    return [rand.choice(icon) for _ in range(3)] 


def print_row(row):
    print(" * ".join(row))


def get_payout(row, bet):
    payout_multipliers = {
        "🍒": 2,
        "🍋": 3,
        "🍊": 4,
        "🍉": 5,
        "🍇": 10,
        "⭐": 20,
        "💎": 100
    }

    if row[0] == row[1] == row[2]:
        multiplier = payout_multipliers.get(row[0], 0)
        payout = bet * multiplier
        print(f"You won! Payout: ${payout}")
        return payout

    print("No win this time. Better luck next spin!")
    print(f"You lost your bet of ${bet}.")
    return 0
    


def main():
    balance = 100

    print("------------------------------------")
    print("Welcome to the Python Slot Machine game!")
    print("------------------------------------")

    print(f"your balance is: ${balance}")


    while balance > 0:

        try: 
            bet = int(input("Enter your bet amount: "))
        except ValueError:
            print("Please enter a valid bet amount.")
            continue
        
        if bet > balance:
            print("You don't have enough balance to place that bet.")
            bet = int(input("Enter your bet amount: "))
    
        if bet <= 0:
            print("Please enter a valid bet amount.")
            bet = int(input("Enter your bet amount: "))

        balance -= bet
        row = spin_row()
        print("Spinning", end="", flush=True)

        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()     

        print_row(row)
        payout = get_payout(row, bet)
        balance += payout
        print(f"your balance is: ${balance}")

        if balance <= 0: 
            print("You have run out of balance. Game over!")
            break
        left = input("Do you want to play again? (y/n): ")
        if left.lower() != 'y':
            print("Thank you for playing! Goodbye!")
            break






        


if __name__ == "__main__":
    main()