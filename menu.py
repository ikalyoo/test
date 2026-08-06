menu = {"pizza" : 300,
        "ikan" : 200,
        "laptop" : 1000,
        "ayam" : 200,
        "sttik" : 599,
        "gelas" : 100}

cart = []
total = 0 
print("--------------Menu---------------")
for key, value in menu.items():
    print(f"{key:5} : {value:.2f} Rupiah".lower())
print("--------------....---------------")


print("Pesen apa?")
while True: 
    food = input("mau pesen apa?: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = int(total + menu.get(food))


pajak = total * 0.10
after = total + pajak

print(f"your bill is {total} rupiah and with pajak jadi {after} ")
