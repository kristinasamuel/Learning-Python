# 1. Creating a Tuple
# Syntax: A tuple is created using parentheses ()
fruit = ("Apple", "Grapes", "Kiwi", "Guava")
print(f"Fruits in Tuple: {fruit}")
# Output: Fruits in Tuple: ('Apple', 'Grapes', 'Kiwi', 'Guava')

#  >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 2. Accessing Tuple Elements (Indexing)
# Accessing elements using indexing (0-based index)
second_element = fruit[1]
print(f"Second element: {second_element}")
# Output: Second element: Grapes

#   >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 3. Tuple Length
# Getting the number of elements in the tuple using len()
fruits_length = len(fruit)
print(f"Fruits length: {fruits_length}")
# Output: Fruits length: 4

#   >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 4. Slicing a Tuple
# Slicing the tuple to get a portion of it
slice_elements = fruit[1:3]
print(f"Sliced Tuple: {slice_elements}")
# Output: Sliced Tuple: ('Grapes', 'Kiwi')

#   >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 5. Tuple with Different Data Types
# A tuple can hold mixed data types
mixed_tuple = (1, "Ali", 234, False, "Hina")
print(f"Mixed Tuple: {mixed_tuple}")
# Output: Mixed Tuple: (1, 'Ali', 234, False, 'Hina')

#  >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 6. Nested Tuple
# A tuple inside another tuple (nested tuple)
nested_tuple = (1, (2, 3), 4)
element = nested_tuple[1]
print(f"Nested tuple: {element}")
# Output: Nested tuple: (2, 3)

