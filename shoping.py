foods = []
prices = []
total = 0

while True:
    food = input("what food do you want?:  (press q to exit)")
    if food == "q":
        break
    else: 
        price = float(input("enter the price: "))
        foods.append(food)
        prices.append(price)

print("---YOUR CART----")

for food in foods:
    print(food, end=" ")

print()
print()

for price in prices:
    total += price


print(f"your spend in this minimarket is {total}", end=" ")
