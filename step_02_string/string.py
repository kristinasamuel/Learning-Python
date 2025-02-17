# ---------------------------------------------------------------
# 1. String Concatenation
# ---------------------------------------------------------------
str_1 = "hello"
str_2 = "Python"
result = str_1 + " " + str_2  # Concatenate strings with a space in between
print(f"Concatenated Result: {result}")  # Output: hello Python

# ---------------------------------------------------------------
# 2. String Repetition
# ---------------------------------------------------------------
message = "learning Python"
repeat_message = message * 3  # Repeat the message 3 times
print(f"Repeated Message: {repeat_message}")  # Output: learning Pythonlearning Pythonlearning Python

# ---------------------------------------------------------------
# 3. Finding the Length of a String
# ---------------------------------------------------------------
new_message = "fun with python"
length = len(new_message)  # Get the length of the string
print(f"Length of the string: {length}")  # Output: 15

# ---------------------------------------------------------------
# 4. Changing Case (Uppercase & Lowercase)
# ---------------------------------------------------------------
# Uppercase
text = "learn python"
upper_text = text.upper()  # Convert text to uppercase
print(f"Uppercase Text: {upper_text}")  # Output: LEARN PYTHON

# Lowercase
lower_text = text.lower()  # Convert text to lowercase
print(f"Lowercase Text: {lower_text}")  # Output: learn python

# ---------------------------------------------------------------
# 5. String Splitting
# ---------------------------------------------------------------
sentence = "Python is awesome"
words = sentence.split()  # Split sentence into words
print(f"Splitting Sentence: {words}")  # Output: ['Python', 'is', 'awesome']

# ---------------------------------------------------------------
# 6. String Finding (Finding Substring)
# ---------------------------------------------------------------
msg = "Hello, Want to learn python!"
find = text.find("python")  # Find the position of 'python' in the string
print(f"Position of 'python': {find}")  # Output: 12

# ---------------------------------------------------------------
# 7. String Slicing
# ---------------------------------------------------------------
my_string = "python"
slicing = my_string[1:4]  # Slice the string from index 1 to 3
print(f"Sliced String: {slicing}")  # Output: yth

# ---------------------------------------------------------------
# 8. String Replacement
# ---------------------------------------------------------------
new_sentence = "Python is very easy"
modified_new_sentence = new_sentence.replace("Python", "Typescript")  # Replace "Python" with "Typescript"
print(f"Modified Sentence: {modified_new_sentence}")  # Output: Typescript is very easy

# ---------------------------------------------------------------
# 9. String Formatting (f-string)
# ---------------------------------------------------------------
name = "Kristina"
age = 20
greeting = f"Hello, My name is {name} and I am {age} years old."  # Use f-string for formatting
print(f"Formatted String: {greeting}")  # Output: Hello, My name is Kristina and I am 20 years old.

# Note: 'f' in f-strings is a reserved keyword used for string formatting.