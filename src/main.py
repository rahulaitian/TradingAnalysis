To create a basic scientific calculator in python, we could start with defining functions for basic arithmetic operations (+,-,*,/) as well as some scientific functions such as power, square root, etc. Here's the simplest way to do this using Python's `math` library:

```python
import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y != 0:
       return x / y
   else:
       return "You can't divide by zero!"

def power(x, y):
   return x ** y

def square_root(x):
   return math.sqrt(x)

def logarithm(x):
   return math.log(x)

def sine(x):
   return math.sin(x)

def cosine(x):
   return math.cos(x)

def tangent(x):
   return math.tan(x)

print('Select operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Power')
print('6. Square Root')
print('7. Logarithm')
print('8. Sine')
print('9. Cosine')
print('10. Tangent')

choice = input('Enter choice (1-10):')

x = float(input('Enter first number: '))
if choice != '6' and choice != '7' and choice != '8' and choice != '9' and choice != '10':
   y = float(input('Enter second number: '))

if choice == '1':
   print(add(x, y))

elif choice == '2':
   print(subtract(x, y))

elif choice == '3':
   print(multiply(x, y))

elif choice == '4':
   if y == 0:
       print('Error: Division by zero is not allowed!')
   else:
       print(divide(x, y))

elif choice == '5':
   print(power(x, y))

elif choice == '6':
   print(square_root(x))

elif choice == '7':
   if x <= 0:
       print('Error: Logarithm of number <= 0 is not defined!')
   else:
       print(logarithm(x))

elif choice == '8':
   print(sine(x))

elif choice == '9':
   print(cosine(x))

elif choice == '10':
   print(tangent(x))

else:
   print('Invalid input')
```

This code allows us to perform basic arithmetic calculations and some scientific functions on the numbers that we input. When defining your calculator functions, be sure to handle edge cases such as division by zero and logarithm of non-positive numbers.
Please note that the trigonometric values (sine, cosine and tangent) returned by this code will be in radians as Python math deals with radians by default.