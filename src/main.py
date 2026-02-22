class Calculator:
    def __init__(self):
        self.history = []

    def perform_operation(self, a, b, operation):
        try:
            if operation == "addition":
                result = a + b
                self.history.append(f'{a} + {b} = {result}')
                return result

            elif operation == "subtraction":
                result = a - b
                self.history.append(f'{a} - {b} = {result}')
                return result

            elif operation == "multiplication":
                result = a * b
                self.history.append(f'{a} * {b} = {result}')
                return result

            elif operation == "division":
                result = a / b
                self.history.append(f'{a} / {b} = {result}')
                return result

            else:
                return "Invalid operation"

        except ZeroDivisionError:
            return "Cannot divide by zero"

    def print_history(self):
        for operation in self.history:
            print(operation)

cal = Calculator()
print(cal.perform_operation(10, 2, "addition"))
print(cal.perform_operation(10, 2, "subtraction"))
print(cal.perform_operation(10, 2, "multiplication"))
print(cal.perform_operation(10, 0, "division"))
cal.print_history()