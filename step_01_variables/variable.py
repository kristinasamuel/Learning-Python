# ---------------------------------------------------------------
# 1. Displaying simple variables and their values
# ---------------------------------------------------------------

# Variable assignments
x = 10
y = 30

# Printing variable values
print(f"x = {x}")
print(f"y = {y}")

# ---------------------------------------------------------------
# 2. Data Types in Python
# ---------------------------------------------------------------

# String, Integer, Float, and Boolean examples
name = "Alice"       # String
age = 12             # Integer
height = 4.9         # Float
is_student = True    # Boolean

# Printing the values of some variables
print(f"Age: {age}")
print(f"Is student: {is_student}")

# ---------------------------------------------------------------
# 3. Variable Data Types in Python
# ---------------------------------------------------------------

# Integer examples
z = 33
U = -5

# Float examples
pi = 3.14
temperature = -4.5

# String examples
greeting = "Hello, Python!"
name = "Kristina"
print(greeting)

# Boolean examples
is_boolean = False
is_happy = True

# Printing Boolean value
print(f"Is Happy: {is_happy}")

# ---------------------------------------------------------------
# 4. Collection Data Types
# ---------------------------------------------------------------

# List: Collection of items
fruits = ["Apple", "Mango", "Orange", "Guava"]

# Accessing list item by index (index starts from 0)
print(f"Fourth fruit in the list: {fruits[3]}")

# Dictionary: Collection of key-value pairs
product = {
    "name": "Iron",
    "warranty": 2033,
    "_is_available": True
}

print(f"Product details: {product}")

# Tuple: Immutable ordered collection of items
Numbers = (10, 30, 90)
print(f"Third number in tuple: {Numbers[2]}")

# ---------------------------------------------------------------
# 5. Mathematical Operators
# ---------------------------------------------------------------

# Arithmetic operations
a = 44
b = 12

# Addition
sum_result = a + b
print(f"Sum: {sum_result}")

# Subtraction
subtraction_result = a - b
print(f"Subtraction: {subtraction_result}")

# Multiplication
multiply_result = a * b
print(f"Multiplication: {multiply_result}")

# Division
quotient_result = a / b
print(f"Quotient: {quotient_result}")

# ---------------------------------------------------------------
# 6. User Input and Output
# ---------------------------------------------------------------

# Taking user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying a message using f-string for formatted output
print(f"Hello {name}, you are {age} years old.")

#  exmaple 2
name: str = input("enter your name: " )
age= int (input("enter your age: "))

print(f"Hi My name is {name} , and my age is {age}")