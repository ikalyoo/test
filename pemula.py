operator = input("Choice operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))



def apabila(operator, num1, num2):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(num1 / num2)
    else:
        print(f"{operator} is not a valid operator. Please choose from (+, -, *, /).")

apabila(operator, num1, num2)
