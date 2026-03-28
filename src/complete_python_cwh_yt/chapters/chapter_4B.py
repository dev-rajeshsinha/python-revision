# ------------------------------------------------------------------------------------------------------------------------------------------

# A Tuple in Python is a collection of ordered and immutable elements. It is similar to a list, but unlike lists, tuples cannot be modified after they are created. Tuples are defined using parentheses () and can contain elements of different data types.

sample_tuple = (1, "Hello", 3.14, True)
print(f"Sample Tuple: {sample_tuple}")  # Output: (1, 'Hello', 3.14, True)

# If we want to create a tuple with only one element, we need to include a comma after the element to differentiate it from a regular parentheses. If we don't include the comma, it will be treated as a regular parentheses and not a tuple, and Python interprets it as a single value enclosed in parentheses.

single_element_tuple = 42  # This is not a tuple, it's just an integer in parentheses
print(f"Single Element Tuple (without comma): {single_element_tuple}")  # Output: 42
print(
    f"Type of single_element_tuple (without comma): {type(single_element_tuple)}"
)  # Output: <class 'int'>

single_element_tuple = (42,)
print(f"Single Element Tuple: {single_element_tuple}")  # Output: (42,)
print(
    f"Type of single_element_tuple: {type(single_element_tuple)}"
)  # Output: <class 'tuple'>

# Tuples are immutable, which means that once a tuple is created, its elements cannot be changed or new elements cannot be added. If we try to modify a tuple, we will get a TypeError.

# sample_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment
# sample_tuple.append(5)  # This will raise an AttributeError: 'tuple' object has no attribute 'append'
print()  # Just to add a new line for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# Below are some of the operations that can be performed on tuples:

print(f"Original Tuple: {sample_tuple}")  # Output: (1, 'Hello', 3.14, True)

# 1. Accessing Elements: We can access elements of a tuple using indexing, just like lists. We can also use negative indexing to access elements from the end of the tuple.

print(f"First Element: {sample_tuple[0]}")  # Output: 1
print(f"Second Element: {sample_tuple[1]}")  # Output: Hello
print(f"Last Element: {sample_tuple[-1]}")  # Output: True
print(f"Second Last Element: {sample_tuple[-2]}")  # Output: 3.14
print()  # Just to add a new line for better readability

# 2. Slicing: We can slice a tuple to get a subset of its elements. The syntax for slicing is similar to that of lists, which is tuple[start:stop:step]. The start index is inclusive, while the stop index is exclusive. If the start index is omitted, it defaults to 0. If the stop index is omitted, it defaults to the length of the tuple. If the step is omitted, it defaults to 1. We can also use negative index values to access elements from the end of the tuple. We can also use negative step to reverse the tuple.

print(f"Sliced Tuple (0:2): {sample_tuple[0:2]}")  # Output: (1, 'Hello')
print(f"Sliced Tuple (1:): {sample_tuple[1:]}")  # Output: ('Hello', 3.14, True)
print(f"Sliced Tuple (:3): {sample_tuple[:3]}")  # Output: (1, 'Hello', 3.14)
print(f"Sliced Tuple (0:4:2): {sample_tuple[0:4:2]}")  # Output: (1, 3.14)
print(
    f"Sliced Tuple (-1:-4:-1): {sample_tuple[-1:-4:-1]}"
)  # Output: (True, 3.14, 'Hello')
print(f"Sliced Tuple (::-1): {sample_tuple[::-1]}")  # Output: (True, 3.14, 'Hello', 1)
print()  # Just to add a new line for better readability

# 3. Concatenation: We can concatenate two or more tuples using the + operator.

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated Tuple: {concatenated_tuple}")  # Output: (1, 2, 3, 'a', 'b', 'c')
print()

# 4. Repetition: We can repeat a tuple a specified number of times using the * operator.

repeated_tuple = tuple1 * 3
print(f"Repeated Tuple: {repeated_tuple}")  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print()  # Just to add a new line for better readability

# 5. Membership Testing: We can check if an element is present in a tuple using the in keyword.

print(f"Is 2 in tuple1? {'Yes' if 2 in tuple1 else 'No'}")  # Output: Yes
print(f"Is 'd' in tuple2? {'Yes' if 'd' in tuple2 else 'No'}")  # Output: No
print()  # Just to add a new line for better readability

# 6. The count() method: We can use the count() method to count the number of occurrences of a specific element in a tuple. The syntax for the count() method is tuple.count(element). It returns the number of times the specified element appears in the tuple. If the element is not found in the tuple, it returns 0.

tuple3 = (1, 2, 3, 2, 4, 2)
count_of_2 = tuple3.count(2)
print(f"Original Tuple: {tuple3}")  # Output: (1, 2, 3, 2, 4, 2)
print(f"Count of 2 in tuple3: {count_of_2}")  # Output: 3
print(f"Count of 5 in tuple3: {tuple3.count(5)}")  # Output: 0
print()  # Just to add a new line for better readability

# 7. The index() method: We can use the index() method to find the index of the first occurrence of a specific element in a tuple. The syntax for the index() method is tuple.index(element). It returns the index of the first occurrence of the specified element in the tuple. If the element is not found in the tuple, it raises a ValueError.

tuple4 = ("a", "b", "c", "d", "e")
index_of_c = tuple4.index("c")
print(f"Original Tuple: {tuple4}")  # Output: ('a', 'b', 'c', 'd', 'e')
print(f"Index of 'c' in tuple4: {index_of_c}")  # Output: 2
# print(f"Index of 'f' in tuple4: {tuple4.index('f')}")  # This will raise a ValueError: 'f' is not in tuple
print()  # Just to add a new line for better readability

# A tuple can also be used to unpack values into variables. This is known as tuple unpacking. We can assign the elements of a tuple to individual variables in a single line of code.

person_info = ("Alice", 30, "Engineer")
name, age, profession = person_info
print(f"Person Info Tuple: {person_info}")  # Output: ('Alice', 30, 'Engineer')
print(f"Name: {name}")  # Output: Alice
print(f"Age: {age}")  # Output: 30
print(f"Profession: {profession}")  # Output: Engineer
print()  # Just to add a new line for better readability

# We can also use the * operator to unpack a tuple into a list of variables. This is known as extended unpacking. The syntax for extended unpacking is variable1, variable2, *variable3 = tuple. The * operator allows us to capture any remaining elements of the tuple into a list.

numbers_tuple = (1, 2, 3, 4, 5)
first, second, *rest = numbers_tuple
print(f"Numbers Tuple: {numbers_tuple}")  # Output: (1, 2, 3, 4, 5)
print(f"First: {first}")  # Output: 1
print(f"Second: {second}")  # Output: 2
print(f"Rest: {rest}")  # Output: [3, 4, 5]
print()  # Just to add a new line for better readability

# We can also use the * operator to unpack a tuple into a list of variables while ignoring some elements. This is known as extended unpacking with ignored values. The syntax for this is variable1, *_, variable2 = tuple. The * operator allows us to capture any remaining elements of the tuple into a list, and the _ variable is used to ignore those values.

numbers_tuple = (1, 2, 3, 4, 5)
first, *_, last = numbers_tuple
print(f"Numbers Tuple: {numbers_tuple}")  # Output: (1, 2, 3, 4, 5)
print(f"First: {first}")  # Output: 1
print(f"Last: {last}")  # Output: 5
print()  # Just to add a new line for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------
