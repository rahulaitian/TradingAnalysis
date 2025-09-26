import math

class ScientificCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed."

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Error: Square root of a negative number is not allowed."

    def factorial(self, n):
        if n >= 0:
            return math.factorial(n)
        else:
            return "Error: Factorial of a negative number is not allowed."

    def log(self, num, base):
        if num > 0 and base > 0:
            return math.log(num, base)
        else:
            return "Error: Log of zero or negative number is not allowed."

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def tan(self, x):
        return math.tan(x)