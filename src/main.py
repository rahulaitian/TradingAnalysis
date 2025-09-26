Sure, I will provide a simple text-based scientific calculator in Python where users can carry out basic scientific calculations like addition, subtraction, multiplication, division, finding the square root, power, and calculation of trigonometric functions.

```python
import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def square_root(x):
   return math.sqrt(x)

def power(x, y):
   return math.pow(x, y)

def sin(x):
   return math.sin(math.radians(x))

def cos(x):
   return math.cos(math.radians(x))

def tan(x):
   return math.tan(math.radians(x))

print("Select option.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square root")
print("6.Power")
print("7.Sin")
print("8.Cos")
print("9.Tan")

while True:
   choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

   if choice in ('1', '2', '3', '4', '5', '6'):
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
   
   if choice in ('7', '8', '9'):
      num1 = float(input("Enter the number: "))

   if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

   elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

   elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

   elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

   elif choice == '5':
      print("The square root of", num1, "is", square_root(num1))

   elif choice == '6':
      print(num1, "raised to the power", num2, "is", power(num1, num2))

   elif choice == '7':
      print("The Sin of", num1, "is", sin(num1))

   elif choice == '8':
      print("The Cos of", num1, "is", cos(num1))

   elif choice == '9':
      print("The Tan of", num1, "is", tan(num1))

   next_calculation = input("Let's do next calculation? (yes/no): ")
   if next_calculation == "no":
     break
```

Please note that Python's trigonometric functions require the input in radians whereas we commonly measure angles in degrees.