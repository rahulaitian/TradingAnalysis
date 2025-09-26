```
import math

def scientific_calculator():

    function_dir = { '1':math.sin, '2':math.cos, '3':math.tan, '4':math.asin, '5':math.acos, '6':math.atan, 
                    '7':math.sinh, '8':math.cosh, '9':math.tanh, '10':math.sqrt, '11':math.log, '12':math.ceil,
                    '13':math.floor, '14':math.fabs, '15':math.factorial, '16':math.exp, '17':math.pow}

    while True:
        print("\nScientific Calculator Menu")
        print("""1.SIN\n2.COS\n3.TAN\n4.ASIN\n5.ACOS\n6.ATAN\n7.SINH\n8.COSH\n9.TANH\n10.Square Root\n11.LOG\n12.CEIL\n13.FLOOR\n14.Absolute\n15.Factorial
16.Exponent\n17.Power\n18.Exit\n""")

        choice = input("\nEnter your choice: ")

        if choice=="18":
            break
        elif choice in function_dir:
            if choice=='17':
                number1 = float(input("\nEnter first number: "))
                number2 = float(input("\nEnter second number: "))
                print("\nResult: ",function_dir[choice](number1, number2))
            else:
                number = float(input("\nEnter number: "))
                print("\nResult: ",function_dir[choice](number))
        else:
            print("\nInvalid Choice!")

if __name__ == "__main__":
    scientific_calculator()
```
This script forms a scientific calculator with the help of Python's math module. Users can make their choice from the menu, and the relevant math function will be applied to either a single number input by the user or two input numbers in the case of the power calculation.