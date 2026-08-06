unit = input("kamu mau konversi F atau C? (F/C): ")
suhu = float(input("masukkan suhu: "))

if unit == "C":
    suhu = (suhu * 9/5) + 32
    print(F"jadi suhu kamu adalah {suhu} dalam fahrenheit")
elif unit == "F":
    suhu = (suhu - 32) * 5/9
    print(f"jadi suhu kamu adalah {suhu} dalam celsius")
else:
    print("invalid bang")
c