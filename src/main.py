class Calculator: 
    def multiply(self, num1, num2): 
        return num1 * num2

    def divide(self, num1, num2): 
        if num2 == 0: 
            return "Error: Division by zero is not allowed"
        return num1 / num2

    def cube(self, num):
        return num ** 3