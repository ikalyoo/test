# MADE A FUCKING SQUARE WITH DOT AND CHANGEABLE.
# AND OFCOURSE IT USE THE FUCKING LOOP MOTHERFUCKER
def square (size):
    center = size // 2

    for i in range(size):
        for j in range(size):
            if i == center and j == center:
                print("0", end =" ")

            elif i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("-", end=" ")
            else:
                print(" ", end=" ")

        print()
square(16)