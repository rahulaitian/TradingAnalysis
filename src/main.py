Here is the updated Python file for the task of creating a scientific calculator:

```python
# import the necessary library
import math

def scientific_calculator():

    print("\nWelcome to the Scientific Calculator! Available operations:")
    print("""
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Square root
          6. Power
          7. Logarithm
          8. Sine
          9. Cosine
          10. Tangent
    """)

    # take user inputs
    choice = int(input("Select operations: "))

    if choice >= 1 and choice <= 4:
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())

    if choice >= 5 and choice <= 7:
        print("Enter one number: ")
        num1 = int(input())

    if choice >=8 and choice <= 10:
        print("Enter the angle in degree: ")
        num1 = int(input())
        num1 = math.radians(num1) # converting degree to radian

    # perform calculations based on user's choice
    if choice == 1:
        res = num1 + num2
    elif choice == 2:
        res = num1 - num2
    elif choice == 3:
        res = num1 * num2
    elif choice == 4:
        res = num1 / num2
    elif choice == 5:
        res = math.sqrt(num1)
    elif choice == 6:
        print("Enter the power: ")
        num2 = int(input())
        res = math.pow(num1, num2)
    elif choice == 7:
        res = math.log(num1)
    elif choice == 8:
        res = math.sin(num1)
    elif choice == 9:
        res = math.cos(num1)
    elif choice == 10:
        res = math.tan(num1)
    else:
        print("Invalid input!")

    print("\nThe result is ", res)


# call the calculator function
if __name__ == "__main__":
    scientific_calculator()
```
This calculator takes inputs from the user and performs simple arithmetic operations, square root, power, logarithm, and trigonometric calculations.