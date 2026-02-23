# ----------------------------------------------------------------------------------------------------------------------------------------

# A list in Python is a collection of items which can be of different types. Lists are ordered, changeable, and allow duplicate values. They are defined using square brackets [].

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(f"Sample List: {sample_list}")  # Output: [1, 2, 3, 'Hello', 4.5, True, None]

# We can access elements in a list using their index, which starts from 0. Unlike strings, lists in Python are mutable, meaning we can change their content after they have been created. We can access and modify elements in a list using their index.

print(f"sample_list[0]: {sample_list[0]}")  # Output: 1
print(f"sample_list[3]: {sample_list[3]}")  # Output: Hello
print()  # Just to add a newline for better readability of the output

sample_list[1] = "World"
print(
    f"Modified Sample List: {sample_list}"
)  # Output: [1, 'World', 3, 'Hello', 4.5, True, None]
print(f"Modified sample_list[1]: {sample_list[1]}")  # Output: World
print()  # Just to add a newline for better readability of the output

# -----------------------------------------------------------------------------------------------------------------------------------------

# Below are some of the important methods that can be used with lists in Python:

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]

# 1. append(): This method adds an element to the end of the list.

sample_list.append("New Element")
print(
    f"After append() of 'New Element': {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None, 'New Element']

# 2. insert(): This method inserts an element at a specified index.

sample_list.insert(2, "Inserted Element")
print(
    f"After insert() of 'Inserted Element' at index 2: {sample_list}"
)  # Output: [1, 2, 'Inserted Element', 3, 'Hello', 4.5, True, None, 'New Element']

# 3. remove(): This method removes the first occurrence of a specified value from the list. If the value is not found, it raises a ValueError. If the list is empty, it also raises a ValueError.

sample_list.remove("Hello")
print(
    f"After remove() of 'Hello': {sample_list}"
)  # Output: [1, 2, 'Inserted Element', 3, 4.5, True, None, 'New Element']
# sample_list.remove("Not In List")  # This will raise a ValueError since "Not In List" is not in the sample_list
# empty_list = []
# empty_list.remove("Any Element")  # This will raise a ValueError since the list is empty

# 4. pop(): This method removes and returns the element at a specified index. If no index is specified, it removes and returns the last element. If the index is out of range or if the list is empty, it raises an IndexError.

popped_element = sample_list.pop(3)
print(f"Popped Element From Index 3: {popped_element}")  # Output: 3
print(
    f"After pop(): {sample_list}"
)  # Output: [1, 2, 'Inserted Element', 4.5, True, None, 'New Element']
popped_element = sample_list.pop()
print(f"Popped Last Element: {popped_element}")  # Output: New Element
print(
    f"After pop() without index: {sample_list}"
)  # Output: [1, 2, 'Inserted Element', 4.5, True, None]
# sample_list.pop(10)  # This will raise an IndexError since index 10 is out of range
# empty_list = []
# empty_list.pop()  # This will raise an IndexError since the list is empty

# 5. clear(): This method removes all elements from the list.

sample_list.clear()
print(f"After clear(): {sample_list}")  # Output: []

# 6. index(): This method returns the index of the first occurrence of a specified value. If the value is not found, it raises a ValueError.

sample_list = [1, 2, "Inserted Element", 4.5, True, None]
print(
    f"Index of 'Inserted Element': {sample_list.index('Inserted Element')}"
)  # Output: 2
# sample_list.index("Not In List")  # This will raise a ValueError since "Not In List" is not in the sample_list

# 7. count(): This method returns the number of occurrences of a specified value in the list. If the value is not found, it returns 0.

sample_list.append("Inserted Element")
print(
    f"Count of 'Inserted Element': {sample_list.count('Inserted Element')}"
)  # Output: 2
print(f"Count of 'Not In List': {sample_list.count('Not In List')}")  # Output: 0

# 8. sort(): This method sorts the elements of the list in ascending order. If the list contains elements of different types, it will raise a TypeError. The sorting algorithm used by the sort() method is Timsort, which is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to perform well on many kinds of real-world data.

numeric_list = [3, 1, 4, 2]
print(f"Original Numeric List: {numeric_list}")  # Output: [3, 1, 4, 2]
numeric_list.sort()
print(f"Sorted Numeric List: {numeric_list}")  # Output: [1, 2, 3, 4]

# 9. reverse(): This method reverses the order of the elements in the list.

numeric_list = [1, 2, 3, 4]
print(f"Original Numeric List: {numeric_list}")  # Output: [1, 2, 3, 4]
numeric_list.reverse()
print(f"Reversed Numeric List: {numeric_list}")  # Output: [4, 3, 2, 1]

# 10. copy(): This method returns a shallow copy of the list. Changes made to the copied list will not affect the original list.

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(f"Original List: {original_list}")  # Output: [1, 2, 3]
print(f"Copied List: {copied_list}")  # Output: [1, 2, 3]
copied_list.append(4)
print(f"After appending 4 to Copied List: {copied_list}")  # Output: [1, 2, 3, 4]
print(
    f"Original List after modifying Copied List: {original_list}"
)  # Output: [1, 2, 3]

# 11. extend(): This method extends the list by appending all the items from another iterable (like another list).

list1 = [1, 2, 3]
print(f"Content of list1: {list1}")  # Output: [1, 2, 3]
list2 = [4, 5, 6]
print(f"Content of list2: {list2}")  # Output: [4, 5, 6]
list1.extend(list2)
print(
    f"Content of list1 after extend() of list2 into list1: {list1}"
)  # Output: [1, 2, 3, 4, 5, 6]
print(f"Content of list2 after extend() into list1: {list2}")  # Output: [4, 5, 6]
print()  # Just to add a newline for better readability of the output

# We can also use the + operator to concatenate two lists, which creates a new list that contains all the elements of both lists. The original lists remain unchanged.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(f"Content of list1: {list1}")  # Output: [1, 2, 3]
print(f"Content of list2: {list2}")  # Output: [4, 5, 6]
print(
    f"Concatenated List using + operator: {concatenated_list}"
)  # Output: [1, 2, 3, 4, 5, 6]

# We can also use the * operator to repeat a list a specified number of times, which creates a new list that contains the elements of the original list repeated the specified number of times. The original list remains unchanged.

list1 = [1, 2, 3]
repeated_list = list1 * 3
print(f"Content of list1: {list1}")  # Output: [1, 2, 3]
print(
    f"Repeated List using * operator: {repeated_list}"
)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
print()  # Just to add a newline for better readability of the output

# We can also use the in keyword to check if an element is present in a list. It returns True if the element is found in the list, and False otherwise.

print(f"Is 2 in list1? {'Yes' if 2 in list1 else 'No'}")  # Output: Yes
print(f"Is 4 in list1? {'Yes' if 4 in list1 else 'No'}")  # Output: No
print()  # Just to add a newline for better readability of the output

# ------------------------------------------------------------------------------------------------------------------------------------------

# We can use slicing to access a range of elements in a list. The syntax for slicing is list[start:stop:step], where start is the index to begin slicing, stop is the index to end slicing (exclusive), and step is the interval between elements to slice. If start is omitted, it defaults to 0. If stop is omitted, it defaults to the length of the list. If step is omitted, it defaults to 1.

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
print(f"sample_list[1:5]: {sample_list[1:5]}")  # Output: [2, 3, 'Hello', 4.5]
print(f"sample_list[:4]: {sample_list[:4]}")  # Output: [1, 2, 3, 'Hello']
print(f"sample_list[3:]: {sample_list[3:]}")  # Output: ['Hello', 4.5, True, None]
print(f"sample_list[::2]: {sample_list[::2]}")  # Output: [1, 3, 4.5, None]
print(f"sample_list[1:6:2]: {sample_list[1:6:2]}")  # Output: [2, 'Hello', True]

# We can also use negative indices in slicing to access elements from the end of the list. The syntax for negative slicing is the same as for positive slicing, but the indices are counted from the end of the list.
print(f"sample_list[-5:-1]: {sample_list[-5:-1]}")  # Output: [3, 'Hello', 4.5, True]
print(
    f"sample_list[::-1]: {sample_list[::-1]}"
)  # Output: [None, True, 4.5, 'Hello', 3, 2, 1]

# We can also use slicing to modify a range of elements in a list. The syntax for modifying a range of elements is list[start:stop] = new_values, where start is the index to begin modifying, stop is the index to end modifying (exclusive), and new_values is a list of new values to replace the old values. If the number of new values is different from the number of old values, the list will be resized accordingly.

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
sample_list[1:4] = ["New", "Values"]
print(
    f"After modifying sample_list[1:4] to ['New', 'Values']: {sample_list}"
)  # Output: [1, 'New', 'Values', 4.5, True, None]
sample_list[2:5] = [10, 20, 30, 40]
print(
    f"After modifying sample_list[2:5] to [10, 20, 30, 40]: {sample_list}"
)  # Output: [1, 'New', 10, 20, 30, 40, None]

# We can also use slicing to delete a range of elements from a list. The syntax for deleting a range of elements is del list[start:stop], where start is the index to begin deleting, and stop is the index to end deleting (exclusive).

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
del sample_list[1:4]
print(f"After deleting sample_list[1:4]: {sample_list}")  # Output: [1, 4.5, True, None]
del sample_list[:2]
print(f"After deleting sample_list[:2]: {sample_list}")  # Output: [True, None]
del sample_list[1:]
print(f"After deleting sample_list[1:]: {sample_list}")  # Output: [True]

# We can also use slicing to create a new list that is a subset of the original list. The syntax for creating a new list using slicing is new_list = original_list[start:stop:step], where start is the index to begin slicing, stop is the index to end slicing (exclusive), and step is the interval between elements to slice.

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
new_list = sample_list[1:5]
print(
    f"New List created from sample_list[1:5]: {new_list}"
)  # Output: [2, 3, 'Hello', 4.5]
new_list = sample_list[::2]
print(
    f"New List created from sample_list[::2]: {new_list}"
)  # Output: [1, 3, 4.5, None]
new_list = sample_list
print(
    f"New List created from sample_list: {new_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]

# We can also use slicing to reverse a list. The syntax for reversing a list using slicing is reversed_list = original_list[::-1], where original_list is the list to be reversed. This creates a new list that is a reversed version of the original list. The original list remains unchanged.

sample_list = [1, 2, 3, "Hello", 4.5, True, None]
print(
    f"Original Sample List: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
reversed_list = sample_list[::-1]
print(
    f"Reversed List created from sample_list: {reversed_list}"
)  # Output: [None, True, 4.5, 'Hello', 3, 2, 1]
print(
    f"Original Sample List after reversing: {sample_list}"
)  # Output: [1, 2, 3, 'Hello', 4.5, True, None]
print()  # Just to add a newline for better readability of the output

# ------------------------------------------------------------------------------------------------------------------------------------------
