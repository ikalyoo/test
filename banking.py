def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit(balance):
    input_amount = float(input("Enter the amount to deposit: ")) 
    print(input_amount)

    if input_amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        print(f"You have deposited: ${input_amount:.2f}")
    return input_amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds. Please enter a valid amount.")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
 
    print(f"You have withdrawn: ${amount:.2f}")
    print(f"Your new balance is: ${balance:.2f}")
    return amount
    
def main():
    balance = 0
    is_running = True

    while is_running        :
        print("------------------------------")
        print("welcome to the banking app")
        print("------------------------------")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = balance + deposit(balance)
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thank you for using the banking app. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


main()

