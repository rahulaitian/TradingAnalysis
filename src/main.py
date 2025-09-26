import math
import cmath

class ScientificCalculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def log(self, num, base):
        return math.log(num, base)

    def sqrt(self, num):
        return math.sqrt(num)

    def sin(self, num):
        return math.sin(num)

    def cos(self, num):
        return math.cos(num)

    def tan(self, num):
        return math.tan(num)

    def sinh(self, num):
        return math.sinh(num)

    def cosh(self, num):
        return math.cosh(num)

    def tanh(self, num):
        return math.tanh(num)

    def asin(self, num):
        return math.asin(num)

    def acos(self, num):
        return math.acos(num)

    def atan(self, num):
        return math.atan(num)

    def factorial(self, num):
        return math.factorial(num)

    def abs(self, num):
        return abs(num)

    def complex_conjugate(self, num):
        return num.conjugate()
