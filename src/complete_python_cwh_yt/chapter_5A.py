# ------------------------------------------------------------------------------------------------------------------------------------------

# A dictionary in Python is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are mutable, meaning we can change their contents after they have been created. Dictionaries are an unordered collection, which means that the items do not have a defined order. Dictionaries are created using curly braces {} and key-value pairs are separated by a colon :. A dictionary in Python can not contain duplicate keys, but it can contain duplicate values. The keys in a dictionary must be of an immutable data type (like strings, numbers, or tuples), while the values can be of any data type.

sample_dict = {
    "name": "John",
    "age": 30,
    "alive": True,
    "height": 5.9,
    "hobbies": ["reading", "traveling", "swimming"],
    # "name": "Doe",  # This will overwrite the previous 'name' key and will not create a duplicate key.
    # ["key"]: "value",  # This will raise a TypeError because lists are mutable and cannot be used as keys in a dictionary.
}
print(
    f"Sample Dictionary: {sample_dict}"
)  # Output: {'name': 'John', 'age': 30, 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming']}
print(f"Type of Sample Dictionary: {type(sample_dict)}")  # Output: <class 'dict'>
print(f"Length of Sample Dictionary: {len(sample_dict)}")  # Output: 5
print()  # Just to add a newline for better readability

# When we need to access a value in a dictionary, we can use the key associated with that value. We can access values using square brackets [] or the get() method.

print(f"Name: {sample_dict['name']}")  # Output: John
print(f"Age: {sample_dict.get('age')}")  # Output: 30
print(f"Alive: {sample_dict['alive']}")  # Output: True
print(f"Height: {sample_dict.get('height')}")  # Output: 5.9
print(
    f"Hobbies: {sample_dict['hobbies']}"
)  # Output: ['reading', 'traveling', 'swimming']
print()  # Just to add a newline for better readability

# Dictionaries are mutable, which means we can change their contents after they have been created. We can add new key-value pairs, update existing values, or remove key-value pairs from a dictionary.

print(f"Original Dictionary: {sample_dict}")
sample_dict["name"] = "Doe"  # Update the value of the 'name' key
sample_dict["country"] = "USA"  # Add a new key-value pair
print(f"Updated Dictionary: {sample_dict}")
# Output: {'name': 'Doe', 'age': 30, 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'country': 'USA'}
del sample_dict["age"]  # Remove the 'age' key-value pair
del sample_dict["country"]  # Remove the 'country' key-value pair
print(f"Final Dictionary: {sample_dict}")
# Output: {'name': 'Doe', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming']}
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# Below are some common methods that can be used with dictionaries in Python:

print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'Doe', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming']}
print()  # Just to add a newline for better readability

# keys() method returns a view object that displays a list of all the keys in the dictionary. We can iterate over this view object to access the keys of the dictionary using a for loop or convert it to a list using the list() function. A view object is a dynamic view of the dictionary's entries, which means that if the dictionary changes, the view object will reflect those changes.

print(
    f"Keys: {sample_dict.keys()}"
)  # Output: dict_keys(['name', 'alive', 'height', 'hobbies'])
print(f"Type of Keys: {type(sample_dict.keys())}")  # Output: <class 'dict_keys'>
print()  # Just to add a newline for better readability

# values() method returns a view object that displays a list of all the values in the dictionary. We can iterate over this view object to access the values of the dictionary using a for loop or convert it to a list using the list() function. A view object is a dynamic view of the dictionary's entries, which means that if the dictionary changes, the view object will reflect those changes.

print(
    f"Values: {sample_dict.values()}"
)  # Output: dict_values(['Doe', True, 5.9, ['reading', 'traveling', 'swimming']])
print(f"Type of Values: {type(sample_dict.values())}")  # Output: <class 'dict_values'>
print()  # Just to add a newline for better readability

# items() method returns a view object that displays a list of all the key-value pairs in the dictionary as tuples. We can iterate over this view object to access the key-value pairs of the dictionary using a for loop or convert it to a list using the list() function. A view object is a dynamic view of the dictionary's entries, which means that if the dictionary changes, the view object will reflect those changes.

print(
    f"Items: {sample_dict.items()}"
)  # Output: dict_items([('name', 'Doe'), ('alive', True), ('height', 5.9), ('hobbies', ['reading', 'traveling', 'swimming'])])
print(f"Type of Items: {type(sample_dict.items())}")  # Output: <class 'dict_items'>
print()  # Just to add a newline for better readability

# get() method is used to retrieve the value associated with a specific key in the dictionary. It takes the key as an argument and returns the corresponding value. If the key is not found in the dictionary, it returns None by default, or we can specify a custom default value as a second argument.

print(f"Name: {sample_dict.get('name')}")  # Output: Doe
print(
    f"Age: {sample_dict.get('age')}"
)  # Output: None (since 'age' key has been deleted)
print(
    f"Age with default value: {sample_dict.get('age', 'Not Found')}"
)  # Output: Not Found (since 'age' key has been deleted)
print()  # Just to add a newline for better readability

# While extracting values from a dictionary, if we try to access a key that does not exist using square brackets [], it will raise a KeyError. However, if we use the get() method to access a key that does not exist, it will return None (or a specified default value) instead of raising an error. This makes the get() method a safer way to access values in a dictionary when we are not sure if the key exists.

# update() method is used to update the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs. If a key in the original dictionary already exists in the dictionary being updated, its value will be overwritten by the value from the dictionary being updated. If a key does not exist in the original dictionary, it will be added to the original dictionary.

new_dict = {"name": "John", "age": 30, "country": "USA"}
print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'Doe', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming']}
print(
    f"New Dictionary: {new_dict}"
)  # Output: {'name': 'John', 'age': 30, 'country': 'USA'}
sample_dict.update(new_dict)
print(f"Updated Dictionary: {sample_dict}")
# Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
print()  # Just to add a newline for better readability

# copy() method is used to create a shallow copy of the dictionary. A shallow copy means that it creates a new dictionary object, but the keys and values are not copied recursively. If the original dictionary contains mutable objects (like lists or other dictionaries), the copied dictionary will reference the same mutable objects. Therefore, changes made to mutable objects in the original dictionary will affect the copied dictionary and vice versa.

copied_dict = sample_dict.copy()
print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
print(
    f"Copied Dictionary: {copied_dict}"
)  # Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading, 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
copied_dict["name"] = (
    "Doe"  # Update the value of the 'name' key in the copied dictionary
)
print(f"Updated Copied Dictionary: {copied_dict}")
# Output: {'name': 'Doe', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
print(f"Original Dictionary after updating copied dictionary: {sample_dict}")
# Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
print()  # Just to add a newline for better readability

# fromkeys() method is used to create a new dictionary from a sequence of keys, with a specified value for all keys. The fromkeys() method takes two arguments: the first argument is an iterable (like a list or a tuple) containing the keys for the new dictionary, and the second argument is the value that will be assigned to all the keys in the new dictionary. If the second argument is not provided, it defaults to None.

keys = ["name", "age", "country"]
value = "Unknown"
new_dict_from_keys = dict.fromkeys(keys, value)
print(
    f"New Dictionary from Keys: {new_dict_from_keys}"
)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'country': 'Unknown'}
print()  # Just to add a newline for better readability

# pop() method is used to remove a key-value pair from the dictionary based on the specified key and return the value associated with that key. If the key is not found in the dictionary, it raises a KeyError unless a default value is provided as a second argument.

print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
popped_value = sample_dict.pop("age", "Not Found")
print(f"Popped Value: {popped_value}")  # Output: 30
print(f"Dictionary after popping 'age': {sample_dict}")
# Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'country': 'USA'}
popped_value_not_found = sample_dict.pop("age", "Not Found")
print(
    f"Popped Value for non-existent key: {popped_value_not_found}"
)  # Output: Not Found (since 'age' key has already been popped)
print()  # Just to add a newline for better readability

# popitem() method is used to remove and return the last inserted key-value pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.

print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'country': 'USA'}
popped_item = sample_dict.popitem()
print(f"Popped Item: {popped_item}")  # Output: ('country', 'USA')
print(f"Dictionary after popping an item: {sample_dict}")
# Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming']}
print()  # Just to add a newline for better readability

# clear() method is used to remove all the key-value pairs from the dictionary, leaving it empty.

print(
    f"Original Dictionary: {sample_dict}"
)  # Output: {'name': 'John', 'alive': True, 'height': 5.9, 'hobbies': ['reading', 'traveling', 'swimming'], 'age': 30, 'country': 'USA'}
sample_dict.clear()
print(f"Cleared Dictionary: {sample_dict}")  # Output: {}
print()  # Just to add a newline for better readability

# ------------------------------------------------------------------------------------------------------------------------------------------
