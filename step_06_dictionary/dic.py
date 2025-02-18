
# 1. Creating a dictionary
product_dic = {
    "name": "Iphone",   # Product Name
    "price": 300,       # Product Price
    "is_avaiable": True # Availability status
}

# Display the product dictionary
print(f"Products: {product_dic}")  
# Output: Products: {'name': 'Iphone', 'price': 300, 'is_avaiable': True}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 2. Getting the length of the dictionary
dic_length = len(product_dic)
print(f"Length of the dictionary: {dic_length}")  
# Output: Length of the dictionary: 3

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 3. Copy of the dictionary
product_copy = product_dic.copy()
print(f"Copied product dictionary: {product_copy}")
# Output: Copied product dictionary: {'name': 'Iphone', 'price': 300, 'is_avaiable': True}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 4. Get the price of the product
product_price = product_dic.get("price")
print(f"Product price: {product_price}")
# Output: Product price: 300

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 5. Accessing a value using a key
get_product_name = product_dic["name"]
print("Name:", get_product_name)  # Output: Name: Iphone

get_product_is_available = product_dic["is_avaiable"]
print("Is Available:", get_product_is_available)  
# Output: Is Available: True

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 6. Modifying the value of an existing key
product_dic["price"] = 3900
print(f"New price of iPhone: {product_dic}")
# Output: New price of iPhone: {'name': 'Iphone', 'price': 3900, 'is_avaiable': True}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 7. Add new key-value pair to the dictionary
product_dic["color"] = "Gold"
print(f"Add new key-value pair in existing dictionary: {product_dic}") 
# Output: Add new key-value pair in existing dictionary: {'name': 'Iphone', 'price': 3900, 'is_avaiable': True, 'color': 'Gold'}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 8. Removing an element from the dictionary using pop()
remove_item = product_dic.pop("price")
print(f"Price element removed: {remove_item}")
print(f"Dictionary after removing the price element: {product_dic}")
# Output: Price element removed: 3900
# Output: Dictionary after removing the price element: {'name': 'Iphone', 'is_avaiable': True, 'color': 'Gold'}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 9. Using `del` to remove a specific item
del product_dic["color"]
print(f"Color element deleted: {product_dic}")
# Output: Color element deleted: {'name': 'Iphone', 'is_avaiable': True}

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 10. Checking if a key exists in the dictionary
if "name" in product_dic:
    print(f"The product name is {product_dic['name']}")
# Output: The product name is Iphone

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 11. Looping through a dictionary using items() 
for key, value in product_dic.items():
    print(f"{key}: {value}")
    # Output: name: Iphone, is_avaiable: True

# Looping through the dictionary keys
for key in product_dic:
    print(f"key: {key}")
    # Output: key: name, key: is_avaiable

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 12. Nested dictionary example
new_products = {
    "product_1": {
        "name": "Laptop 1",
        "company": "Dell",
        "price": 30000
    },
    "product_2": {
        "name": "Laptop 2",
        "company": "Lenovo",
        "price": 25000
    }
}

# Accessing nested dictionary values
new_laptop = new_products["product_1"]["name"]
print(f"Name of Product 1: {new_laptop}")
# Output: Name of Product 1: Laptop 1

# >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 

# 13. Merging two dictionaries
product_02 = {
    "name": "Laptop 3",
    "company": "HP",
    "price": 26000
}

# Update the new_products dictionary by merging product_02
new_products.update(product_02)
print(f"Merging 2 dictionaries: {new_products}")
# Output: Merging 2 dictionaries: {'product_1': {'name': 'Laptop 1', 'company': 'Dell', 'price': 30000}, 
# 'product_2': {'name': 'Laptop 2', 'company': 'Lenovo', 'price': 25000}, 
# 'name': 'Laptop 3', 'company': 'HP', 'price': 26000}