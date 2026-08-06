weight = float(input("Masukkan berat: "))
unit = input("Masukkan berat dalam (Kg/L): ")

if unit == "Kg":
    weight = float(weight * 2.205)
    unit = "L"
elif unit == "L":
    weight = float(weight / 2.205)
    unit = "K"
else:
    print("invalid bang")

print(f"your weight is {weight} in {unit} ")