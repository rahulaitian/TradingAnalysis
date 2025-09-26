import math

def calculator():
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")

    choice = input("Choose an option: ")

    if choice == "1":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x + y)

    elif choice == "2":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x - y)

    elif choice == "3":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x * y)

    elif choice == "4":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(x / y)

    elif choice == "5":
        x = int(input("Enter a number: "))
        y = int(input("Enter the power: "))
        print(math.pow(x, y))

    elif choice == "6":
        x = int(input("Enter a number: "))
        print(math.sqrt(x))

    elif choice == "7":
        x = int(input("Enter a number: "))
        print(math.log(x))

    elif choice == "8":
        x = int(input("Enter a number: "))
        print(math.sin(math.radians(x)))

    elif choice == "9":
        x = int(input("Enter a number: "))
        print(math.cos(math.radians(x)))

    elif choice == "10":
        x = int(input("Enter a number: "))
        print(math.tan(math.radians(x)))

    else:
        print("Invalid input")

calculator()