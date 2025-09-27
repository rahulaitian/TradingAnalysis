class Calculator:
    def __init__(self):
        pass

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Can't divide by zero!"

    def cube(self, num):
        return num ** 3