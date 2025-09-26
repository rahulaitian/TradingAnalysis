Here is a simple way to create a scientific calculator in Python, using functions and loops for handling the user interaction:

```Python
import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       return "Error! Division by zero is not allowed."
   return x / y

def exponent(x, y):
   return x ** y

def sqrt(x):
   return math.sqrt(x)

def log(x):
   return math.log(x)

def sin(x):
   return math.sin(x)

def cos(x):
   return math.cos(x)

def tan(x):
   return math.tan(x)

while True:
   print("\nChoose operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Power")
   print("6.Root")
   print("7.Logarithm")
   print("8.Sin")
   print("9.Cos")
   print("10.Tan")
   print("0.Exit")

   choice = input("\nEnter choice: ")

   if choice == '0':
       break

   num1 = float(input("\nEnter first number: "))

   if choice == '6' or choice == '7' or choice == '8' or choice == '9' or choice == '10':
       if num1 == 0:
           print("Invalid input for this operation.")
           continue
   else:
       num2 = float(input("\nEnter second number: "))

   if choice == '1':
       print("\nResult: ", add(num1, num2))
   elif choice == '2':
       print("\nResult: ", subtract(num1, num2))
   elif choice == '3':
       print("\nResult: ", multiply(num1, num2))
   elif choice == '4':
       print("\nResult: ", divide(num1, num2))
   elif choice == '5':
       print("\nResult: ", exponent(num1, num2))
   elif choice == '6':
       print("\nResult: ", sqrt(num1))
   elif choice == '7':
       print("\nResult: ", log(num1))
   elif choice == '8':
       print("\nResult: ", sin(num1)) 
   elif choice == '9':
       print("\nResult: ", cos(num1)) 
   elif choice == '10':
       print("\nResult: ", tan(num1)) 
   else:
       print("\nInvalid input!")
```

With the program above, you can perform basic operations such as addition, subtraction, multiplication, and division. And you can also perform scientific operations such as exponentiation (raising to a power), square root, logarithm, sine, cosine, and tangent