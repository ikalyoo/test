import random

options = ("rock", "paper", "scissor")

playing = True

while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter tastingtubas: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("draw")
    elif player == "rock" and computer == "scissor":
        print("you win")
    elif player == "scissor" and computer == "paper":
            print("you win")
    elif player == "paper" and computer == "rock":
            print("you win")
    else: 
         print("motherfucking you lose into a computer")

    udahan = input("Main lagi? (y/n): ").strip().lower()
    playing = udahan == "y"
    print()


