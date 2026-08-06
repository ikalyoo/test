num_pad = [(1, 2, 3),
           (4, 5 , 6),
           (7, 9, 9),
           ("*", 0, "#")]

for asep in num_pad:
    for num in asep:
        print(num, end=" ")
    print(num)


#how the fuck human invent this logic   