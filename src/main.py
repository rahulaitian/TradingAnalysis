Here is your updated file:

```python

class ScientificCalculator:
    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Undefined"
    
    @staticmethod
    def square(x):
        return x**2
    
    @staticmethod
    def power(x, y):
        return x**y

    @staticmethod
    def root(x, y):
        return x**(1/y)

    @staticmethod
    def sine(x):
        import math
        return math.sin(x)
        
    @staticmethod
    def cosine(x):
        import math
        return math.cos(x)
        
    @staticmethod
    def tangent(x):
        import math
        return math.tan(x)

    @staticmethod
    def log_base_e(x):
        import math
        return math.log(x)

    @staticmethod
    def log_base_10(x):
        import math
        return math.log10(x)


if __name__ == "__main__":
    calculator = ScientificCalculator()
    print(calculator.add(5, 2))
    print(calculator.subtract(5, 2))
    print(calculator.multiply(5, 2))
    print(calculator.divide(5, 2))
    print(calculator.square(5))
    print(calculator.power(5, 2))
    print(calculator.root(4, 2))
    print(calculator.sine(30))
    print(calculator.cosine(30))
    print(calculator.tangent(30))
    print(calculator.log_base_e(10))
    print(calculator.log_base_10(100))
```
In this updated file, a class `ScientificCalculator` is created with several static methods, each representing a mathematical operation that a scientific calculator would execute, such as addition, subtract, multiplication, division, square, power, root, sine, cosine, tangent, and logarithm with base e and 10. In the main method, some of these operations are called for demonstration.
