Sure, here is a basic implementation of a scientific calculator with a very simple console interface. It provides operations like addition, subtraction, multiplication, division, square root, power, sin, cos, tan, etc.

```python
import math

def scientific_calculator():
    print("Options: ")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'sqrt' for square root")
    print("Enter '**' for power")
    print("Enter 'sin' for sin")
    print("Enter 'cos' for cos")
    print("Enter 'tan' for tan")
    print("Enter 'exit' to quit")

    while True:
        operation = input("Enter operation: ")

        if operation == "+":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", num1 + num2)
        
        elif operation == "-":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", num1 - num2)

        elif operation == "*":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", num1 * num2)

        elif operation == "/":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result: ", num1 / num2)

        elif operation == "sqrt":
            num = float(input("Enter number: "))
            print("Result: ", math.sqrt(num))

        elif operation == "**":
            num1 = float(input("Enter the number: "))
            num2 = float(input("Enter the power: "))
            print("Result: ", math.pow(num1, num2))

        elif operation == "sin":
            num = float(input("Enter the number: "))
            print("Result: ", math.sin(math.radians(num))) 

        elif operation == "cos":
            num = float(input("Enter the number: "))
            print("Result: ", math.cos(math.radians(num)))

        elif operation == "tan":
            num = float(input("Enter the number: "))
            print("Result: ", math.tan(math.radians(num)))

        elif operation == "exit":
            print("Exiting the program...")
            break

        else:
            print("Invalid operation. Try again.")

scientific_calculator()
```
This code will work in Python 3+. For the trigonometric functions sin, cos, and tan, the input is converted from degrees to radians using math.radians() in order to use the math module's trigonometric functions. 

Remember to be careful when dividing, as dividing by zero will raise an error.

Please note that this