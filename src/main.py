import math

def scientific_calculator():
    print("Scientific Calculator\n")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'sqr' for square")
    print("Enter 'sqrt' for square root")
    print("Enter 'exp' for exponent")
    print("Enter 'log' for logarithm")
    print("="*20)
    
    operation = input("Enter operation: ")

    if operation == 'add':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        result = n1 + n2
        print("Result: ", result)

    elif operation == 'sub':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        result = n1 - n2
        print("Result: ", result)

    elif operation == 'mul':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        result = n1 * n2
        print("Result: ", result)

    elif operation == 'div':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        result = n1 / n2
        print("Result: ", result)

    elif operation == 'sqr':
        n1 = float(input("Enter number: "))
        result = n1 ** 2
        print("Result: ", result)

    elif operation == 'sqrt':
        n1 = float(input("Enter number: "))
        result = math.sqrt(n1)
        print("Result: ", result)

    elif operation == 'exp':
        n1 = float(input("Enter base: "))
        n2 = float(input("Enter exponent: "))
        result = n1 ** n2
        print("Result: ", result)
        
    elif operation == 'log':
        n1 = float(input("Enter number: "))
        result = math.log(n1)
        print("Result: ", result)

    else:
        print("Invalid operation")

scientific_calculator()