import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    
    operations = {'1': 'Addition', '2': 'Subtraction', '3': 'Multiplication', 
                  '4': 'Division', '5': 'Exponent', '6': 'Square Root', 
                  '7': 'Logarithm', '8': 'Sine', '9': 'Cosine', '10': 'Tangent'}

    while True:
        for key, value in operations.items():
            print(f"{key}. {value}")
        operation = input("Please select an operation (1-10): ")
        if operation not in operations:
            print("Invalid input. Please try again.")
            continue
            
        if operation in ['8', '9', '10']:
            num1 = float(input("Enter a number (in degrees): "))
        elif operation == '7':
            num1 = float(input("Enter a number (greater than 0): "))
            if num1 <= 0:
                print("Invalid input. Please try again.")
                continue
        else:
            num1 = float(input("Enter the first number: "))

        if operation not in ['6', '7', '8', '9', '10']:
            num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = num1 + num2
        elif operation == '2':
            result = num1 - num2
        elif operation == '3':
            result = num1 * num2
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero. Please try again.")
                continue
        elif operation == '5':
            result = num1 ** num2
        elif operation == '6':
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                print("Cannot take square root of negative number. Please try again.")
                continue
        elif operation == '7':
            result = math.log(num1)
        elif operation == '8':
            result = math.sin(math.radians(num1))
        elif operation == '9':
            result = math.cos(math.radians(num1))
        elif operation == '10':
            result = math.tan(math.radians(num1))

        print(f"The result is: {result}\n")
        continue_operation = input("Do you want to perform another operation? (yes/no): ")
        if continue_operation.lower() != 'yes':
            break

scientific_calculator()