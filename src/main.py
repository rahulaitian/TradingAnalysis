Here's a simple implementation of what the task might look like:

```python
class ScientificCalculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

    def power(self, num1, num2):
        return num1 ** num2

    def root(self, num, root):
        if root != 0:
            return num ** (1.0 / root)
        else:
            return "Error: Division by zero"

    def factorial(self, num):
        if num < 0:
            return "Error: Factorial of a negative number doesn't exist"
        elif num == 0:
            return 1
        else:
            current_product = 1
            for i in range(1, num + 1):
                current_product *= i
            return current_product

    def log(self, num, base):
        import math
        if num > 0 and base > 0:
            return math.log(num, base)
        else:
            return "Error: Logarithm undefined for given number"

cal = ScientificCalculator()
``` 

This defines a ScientificCalculator class with fundamental mathematical operations methods such as addition, subtraction, multiplication, division, power, root, factorial, and logarithm. Please implement more advanced methods and error checking mechanisms as needed for your use case.