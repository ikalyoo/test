#so, we want to make a fucking square okay with the custom widht and length
Length = int(input("Enter the length of the square: "))
Width = int(input("Enter the width of the square: "))

def draw_square(length, Width):
    for i in range(length):
        for j in range(Width):
            if i == 0 or i == length - 1:
                print("*", end="")
            else:
                if j == 0 or j == Width - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

draw_square(Length, Width)