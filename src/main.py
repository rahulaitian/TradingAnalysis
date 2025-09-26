import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       return 'Infinity'
   return x / y

def power(x, y):
   return x**y

def sqrt(x):
   return math.sqrt(x)

def ln(x):
   return math.log(x)

def log(x):
   return math.log10(x)

def trig_sin(x):
   return math.sin(x)

def trig_cos(x):
   return math.cos(x)

def trig_tan(x):
   return math.tan(x)

def calculate():
   operation = input('''
Please type in the math operation you would like to complete:
+  for addition
-  for subtraction
*  for multiplication
/  for division
^  for power
s  for sqrt root
ln for natural log
log for log base 10
sin for sine
cos for cosine
tan for tangent
''')

   if operation in ['+', '-', '*', '/', '^']:
       x = int(input('Enter your first number: '))
       y = int(input('Enter your second number: '))
       if operation == '+':
           print(add(x, y))
       elif operation == '-':
           print(subtract(x, y))
       elif operation == '*':
           print(multiply(x, y))
       elif operation == '/':
           print(divide(x, y))
       elif operation == '^':
           print(power(x, y))
   
   elif operation in ['s', 'ln', 'log', 'sin', 'cos', 'tan']:
       x = int(input('Enter your number: '))
       if operation == 's':
           print(sqrt(x))
       elif operation == 'ln':
           print(ln(x))
       elif operation == 'log':
           print(log(x))
       elif operation == 'sin':
           print(trig_sin(x))
       elif operation == 'cos':
           print(trig_cos(x))
       elif operation == 'tan':
           print(trig_tan(x))

   else:
       print('Invalid operation')
       
calculate()