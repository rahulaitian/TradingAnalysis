def basic_calculator(a, b, operation):
    try:
        if operation == "addition":
            return a + b
        elif operation == "subtraction":
            return a - b
        elif operation == "multiplication":
            return a * b
        elif operation == "division":
            return a / b
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(basic_calculator(10, 2, "addition"))
print(basic_calculator(10, 2, "subtraction"))
print(basic_calculator(10, 2, "multiplication"))
print(basic_calculator(10, 0, "division"))