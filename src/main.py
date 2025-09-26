```python
import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select operation:")
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
    
    choice = int(input("Enter choice(1/2/3/4/5/6/7/8/9/10): "))

    if choice in range(1, 12):
        num1 = float(input("Enter first number: "))
             
        if choice == 1:
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", num1 + num2)
                 
        elif choice == 2:
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", num1 - num2)
 
        elif choice == 3:
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", num1 * num2)
 
        elif choice == 4:
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", num1 / num2)

        elif choice == 5:
            num2 = float(input("Enter second number: "))
            print(num1, "^", num2, "=", math.pow(num1, num2))

        elif choice == 6:
            print("Square root of", num1, "=", math.sqrt(num1))

        elif choice == 7:
            print("Logarithm of", num1, "=", math.log(num1))

        elif choice == 8:
            print("Sine of", num1, "=", math.sin(num1))

        elif choice == 9:
            print("Cosine of", num1, "=", math.cos(num1))

        elif choice == 10:
            print("Tangent of", num1, "=", math.tan(num1))

        else:
            print("Invalid input")
    else:
        print("Invalid input")

scientific_calculator()
```