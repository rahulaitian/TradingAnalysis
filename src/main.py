class Calculator:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by zero!")
        return a / b

    def cube(self, a):
        return a**3
