import math

class ScientificCalculator:

    def __init__(self):
        pass

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        else:
            return a / b

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    def sqrt(self, a):
        if a < 0:
            return "Error: Negative input!"
        else:
            return math.sqrt(a)

    def power(self, a, b):
        return math.pow(a, b)

    def log(self, a, b):
        return math.log(a, b)

    def exp(self, a):
        return math.exp(a)

calculator = ScientificCalculator()
print(calculator.addition(5,5))
print(calculator.subtraction(10,5))
print(calculator.multiplication(5,5))
print(calculator.division(10,5))
print(calculator.sin(30))
print(calculator.cos(60))
print(calculator.tan(45))
print(calculator.sqrt(16))
print(calculator.power(2,3))
print(calculator.log(100,10))
print(calculator.exp(2))