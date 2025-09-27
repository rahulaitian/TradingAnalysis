def calculator(operation, num1, num2):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
    else:
        return "Invalid operation"

# Examples of use:
print(calculator("addition", 10, 5))
print(calculator("subtraction", 10, 5))
print(calculator("multiplication", 10, 5))
print(calculator("division", 10, 5))
print(calculator("division", 10, 0))