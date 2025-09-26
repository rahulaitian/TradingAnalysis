Sure, here is a simple calculator program in Python that performs addition, subtraction, division, and multiplication.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    choice = input("\nEnter your choice(1/4): ")

    num1 = int(input("\nEnter first number: "))
    num2 = int(input("\nEnter second number: "))

    if choice == '1':
        print("\nThe result is: ", add(num1, num2))

    elif choice == '2':
        print("\nThe result is: ", subtract(num1, num2))

    elif choice == '3':
        print("\nThe result is: ", multiply(num1, num2))

    elif choice == '4':
        print("\nThe result is: ", divide(num1, num2))

    else:
        print("\nInvalid input")

calculator()
```

In the above code, first we've defined separate functions for addition, subtraction, multiplication, and division. Then inside the `calculator` function, we take the user's choice of operation and the two numbers as input, perform the chosen operation using the appropriate function, and print the result. This code will keep running until it's manually stopped.