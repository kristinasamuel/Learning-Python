# ---------------------------------------------------------------
# 1. Creating a List
# ---------------------------------------------------------------
# Syntax to create a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(f"Fruits: {fruits}")  # Output: Fruits: ['Apple', 'Banana', 'Mango', 'Orange']

# ---------------------------------------------------------------
# 2. Accessing List Elements (Indexing)
# ---------------------------------------------------------------
# Accessing elements using their index (0-based index)
second_fruit = fruits[1]
print(f"Second element of the list: {second_fruit}")  # Output: Second element of the list: Banana

# ---------------------------------------------------------------
# 3. Modifying List Elements
# ---------------------------------------------------------------
# Lists are mutable; we can change elements by assigning a new value to an index
fruits[2] = "Strawberry"
print(f"Modified list: {fruits}")  # Output: Modified list: ['Apple', 'Banana', 'Strawberry', 'Orange']

# ---------------------------------------------------------------
# 4. Adding Elements to a List
# ---------------------------------------------------------------
# Use `append()` to add an element to the end of the list
fruits.append("Kiwi")
print(f"List after adding an element: {fruits}")  # Output: List after adding an element: ['Apple', 'Banana', 'Strawberry', 'Orange', 'Kiwi']

# ---------------------------------------------------------------
# 5. Removing Elements from a List
# ---------------------------------------------------------------
# Use `remove()` to remove a specific element from the list
fruits.remove("Orange")
print(f"List after removing 'Orange': {fruits}")  # Output: List after removing 'Orange': ['Apple', 'Banana', 'Strawberry', 'Kiwi']

# ---------------------------------------------------------------
# 6. Finding the Length of a List
# ---------------------------------------------------------------
# Use `len()` to find the number of items in the list
fruits_length = len(fruits)
print(f"Length of the list: {fruits_length}")  # Output: Length of the list: 4

# ---------------------------------------------------------------
# 7. List Slicing
# ---------------------------------------------------------------
# Slicing a list: Get elements from index 1 to 2 (3 is not included)
sliced_fruits = fruits[1:3]
print(f"Sliced list: {sliced_fruits}")  # Output: Sliced list: ['Banana', 'Strawberry']

# ---------------------------------------------------------------
# 8. Sorting a List
# ---------------------------------------------------------------
# Use `sort()` to sort the list in ascending order (alphabetically for strings)
fruits.sort()
print(f"Sorted list: {fruits}")  # Output: Sorted list: ['Apple', 'Banana', 'Kiwi', 'Strawberry']

# ---------------------------------------------------------------
# 9. Reversing a List
# ---------------------------------------------------------------
# Use `reverse()` to reverse the order of the list
fruits.reverse()
print(f"Reversed list: {fruits}")  # Output: Reversed list: ['Strawberry', 'Kiwi', 'Banana', 'Apple']

# ---------------------------------------------------------------
# 10.Add value (slicing)
# ---------------------------------------------------------------

# we can add value in list by using slice method

car_list = ["Civic" ,"Honda" , "Toyata" , "Suzuki" ]
car_list[1:2] = ["Heavy Bike"]
print(car_list)             # output ['Civic', 'Heavy Bike', 'Toyata', 'Suzuki']

# now  we can replace two value with slicing

colors_list = ["Red" , "Blue", "Pink" ,"Brown" ]
colors_list[1:3] = ["Green" , "yellow"]
print(colors_list)     # output  ['Red', 'Green', 'yellow', 'Brown']

# delete element with slicing

colors = ["Red" , "Blue", "Pink" ,"Brown" ]
colors[1:3] = []
print(colors)   # output ['Red', 'Brown']

# ---------------------------------------------------------------

# 11. insert in List

#  insert a new elemnet in a list we can use insert method
Mobiles_Phone = ["Samsung","Iphone" ,"Redmi"]
Mobiles_Phone.insert(1,"Nokia")
print(Mobiles_Phone)       # output ['Samsung', 'Nokia', 'Iphone', 'Redmi']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>