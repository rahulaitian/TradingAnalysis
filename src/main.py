import math

def scientific_calculator():
    operation = input("Enter +, -, *, /, sin, cos, tan, sqrt: ")
    if operation in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        else:
            result = num1 / num2

    elif operation in ['sin', 'cos', 'tan']:
        num = float(input("Enter the number: "))
        if operation == 'sin':
            result = math.sin(num)
        elif operation == 'cos':
            result = math.cos(num)
        else:
            result = math.tan(num)

    else:
        num = float(input("Enter the number: "))
        result = math.sqrt(num)

    print("Result: ", result)
    return result

scientific_calculator()