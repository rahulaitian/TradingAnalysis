Sure, I can help you with this. Here is your Python file content updated to create a scientific calculator:

```python
import math

class ScientificCalculator:
    #initialization
    def __init__(self):
        pass

    #addition
    def add(self, a, b):
        return a+b

    #subtraction
    def subtract(self, a, b):
        return a-b

    #multiplication
    def multiply(self, a, b):
        return a*b

    #division
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return float(a)/float(b)

    #square root
    def sqrt(self, num):
        if num < 0:
            return "Error! Square root of negative number is not allowed."
        return math.sqrt(num)

    #exponential
    def exponential(self, a, b):
        return math.pow(a, b)

    #sine
    def sine(self, deg):
        return math.sin(math.radians(deg))

    #cosine
    def cosine(self, deg):
        return math.cos(math.radians(deg))

    #tangent
    def tangent(self, deg):
        return math.tan(math.radians(deg))

# Initializing the calculator
calculator = ScientificCalculator()

# Test the calculator with some basic operations
print(calculator.add(5,3))        # Output: 8
print(calculator.subtract(5,3))   # Output: 2
print(calculator.multiply(5,3))   # Output: 15
print(calculator.divide(6,3))     # Output: 2.0
print(calculator.sqrt(9))         # Output: 3.0
print(calculator.exponential(2,3)) # Output: 8.0
print(calculator.sine(90))        # Output: 1.0
print(calculator.cosine(0))       # Output: 1.0
print(calculator.tangent(45))     # Output: 1.0
```

This script now performs the basic calculator operations (addition, subtraction, multiplication, and division) as well as some common scientific calculator functions (square root, exponentiation, sine, cosine, and tangent).