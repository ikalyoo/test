phone_number = input("Enter your phone number: ")

if len(phone_number) > 12:
    print("Invalid phone number.")
elif not phone_number.find(" ") == -1:
    print("balikan lagi bang")
#enakan pake elif " " in phone,number
elif not phone_number.isdigit() 
    print("gabisa ada huruf bang")
#OHH BERARTI JIKA DI PHONE NUMBER ADA YANG BUKAN DIGIT - - - 
#PRINT GABISA ADA HURUF BANG

else:
    print("valid phone number.")


