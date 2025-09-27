def calculator(operation, num1, num2):
    if operation == 'addition':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiplication':
        return num1 * num2
    elif operation == 'division':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return num1 / num2

print(calculator('addition', 2, 3))  # Output: 5
print(calculator('subtraction', 7, 5))  # Output: 2
print(calculator('multiplication', 2, 3))  # Output: 6
print(calculator('division', 10, 0))  # Output: 'Error: Division by Zero'
print(calculator('division', 10, 2))  # Output: 5.0