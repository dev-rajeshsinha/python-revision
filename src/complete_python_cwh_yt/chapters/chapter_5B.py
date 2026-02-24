# ------------------------------------------------------------------------------------------------------------------------------------------

# Sets in Python are unordered collections of unique elements. They are mutable, meaning we can add or remove elements after the set has been created. Sets are created using curly braces {} or the set() function. Since sets do not allow duplicate elements, any duplicate elements added to a set will be automatically removed.

# set created using curly braces
sample_set = {1, 2, 3, 4, 5}
print(f"Original set: {sample_set}")  # Output: {1, 2, 3, 4, 5}

# set created using the set() function
sample_set = set([1, 2, 3, 4, 5])
print(f"Original set: {sample_set}")  # Output: {1, 2, 3, 4, 5}

# If we want to create an empty set, we must use the set() function, as using {} will create an empty dictionary instead.

empty_set = {}
print(f"Type of empty_set: {type(empty_set)}")  # Output: <class 'dict'>
empty_set = set()
print(f"Type of empty_set: {type(empty_set)}")  # Output: <class 'set'>

# If we want to create a set with duplicate elements, we can do so, but the duplicates will be automatically removed.

duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print(f"Set with duplicates removed: {duplicate_set}")  # Output: {1, 2, 3, 4, 5}

# A Set in Python is heterogeneous, meaning it can contain elements of different data types. For example, a set can contain integers, strings, and even other sets.

heterogeneous_set = {1, "Hello", 3.14, (1, 2), frozenset({5, 6})}
print(
    f"Heterogeneous set: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6})}

# -------------------------------------------------------------------------------------------------------------------------------------------

# Below are some of the key methods and operations that can be performed on sets in Python:

print(
    f"Original set: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6})}

# add() method is used to add a single element to a set. If the element already exists in the set, it will not be added again.

heterogeneous_set.add("New Element")
print(
    f"Set after adding a new element: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element'}
heterogeneous_set.add(1)  # This will not be added as 1 already exists in the set
print(
    f"Set after trying to add a duplicate element (1): {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element'}
print()  # Just to add a newline for better readability

# update() method is used to add multiple elements to a set. It can take an iterable (like a list, tuple, or another set) as an argument and add all the elements from that iterable to the set. If any of the elements already exist in the set, they will not be added again.

print(
    f"Set before updating with multiple elements: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element'}
heterogeneous_set.update([7, 8, 9])
print(
    f"Set after updating with multiple elements: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element', 7, 8, 9}
heterogeneous_set.update({10, 11, 12})
print(
    f"Set after updating with another set: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element', 7, 8, 9, 10, 11, 12}
print()  # Just to add a newline for better readability

# remove() method is used to remove a specific element from a set. If the element does not exist in the set, it will raise a KeyError.

print(
    f"Set before removing an element: {heterogeneous_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element', 7, 8, 9, 10, 11, 12}
heterogeneous_set.remove(3.14)
print(
    f"Set after removing an element (3.14): {heterogeneous_set}"
)  # Output: {1, 'Hello', (1, 2), frozenset({5, 6}), 'New Element', 7, 8, 9, 10, 11, 12}
# heterogeneous_set.remove(3.14)  # This will raise a KeyError as 3.14 has already been removed from the set
print()  # Just to add a newline for better readability

# discard() method is used to remove a specific element from a set. If the element does not exist in the set, it will not raise an error and will simply do nothing.

print(
    f"Set before discarding an element: {heterogeneous_set}"
)  # Output: {1, 'Hello', (1, 2), frozenset({5, 6}), 'New Element', 7, 8, 9, 10, 11, 12}
heterogeneous_set.discard(7)
print(
    f"Set after discarding an element (7): {heterogeneous_set}"
)  # Output: {1, 'Hello', (1, 2), frozenset({5, 6}), 'New Element', 8, 9, 10, 11, 12}
heterogeneous_set.discard(
    7
)  # This will not raise an error as 7 has already been discarded from the set
print(
    f"Set after trying to discard a non-existent element (7): {heterogeneous_set}"
)  # Output: {1, 'Hello', (1, 2), frozenset({5, 6}), 'New Element', 8, 9, 10, 11, 12}
print()  # Just to add a newline for better readability

# pop() method is used to remove and return an arbitrary element from the set. Since sets are unordered, we cannot predict which element will be removed. If the set is empty, it will raise a KeyError.

print(
    f"Set before popping an element: {heterogeneous_set}"
)  # Output: {1, 'Hello', (1, 2), frozenset({5, 6}), 'New Element', 8, 9, 10, 11, 12}
popped_element = heterogeneous_set.pop()
print(
    f"Popped element: {popped_element}"
)  # Output: (An arbitrary element from the set)
print(
    f"Set after popping an element: {heterogeneous_set}"
)  # Output: (The set with the popped element removed)
print()  # Just to add a newline for better readability

# clear() method is used to remove all elements from the set, resulting in an empty set.

print(
    f"Set before clearing: {heterogeneous_set}"
)  # Output: (The current state of the set)
heterogeneous_set.clear()
print(f"Set after clearing: {heterogeneous_set}")  # Output: set()
print()  # Just to add a newline for better readability

# union() method is used to return a new set that contains all the elements from both sets. The union of two sets A and B is denoted as A ∪ B.

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Set A: {set_a}")  # Output: {1, 2, 3}
print(f"Set B: {set_b}")  # Output: {3, 4, 5}
union_set = set_a.union(set_b)
print(f"Union of Set A and Set B: {union_set}")  # Output: {1, 2, 3, 4, 5}
print()  # Just to add a newline for better readability

# intersection() method is used to return a new set that contains only the elements that are present in both sets. The intersection of two sets A and B is denoted as A ∩ B.

intersection_set = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection_set}")  # Output: {3}
print()  # Just to add a newline for better readability

# difference() method is used to return a new set that contains the elements that are present in the first set but not in the second set. The difference of two sets A and B is denoted as A - B.

difference_set = set_a.difference(set_b)
print(f"Difference of Set A and Set B (A - B): {difference_set}")  # Output: {1, 2}
difference_set = set_b.difference(set_a)
print(f"Difference of Set B and Set A (B - A): {difference_set}")  # Output: {4, 5}
print()  # Just to add a newline for better readability

# symmetric_difference() method is used to return a new set that contains the elements that are present in either of the sets but not in both. The symmetric difference of two sets A and B is denoted as A Δ B.

symmetric_difference_set = set_a.symmetric_difference(set_b)
print(
    f"Symmetric difference of Set A and Set B: {symmetric_difference_set}"
)  # Output: {1, 2, 4, 5}
print()  # Just to add a newline for better readability

# issubset() method is used to check if all elements of the first set are present in the second set. It returns True if the first set is a subset of the second set, and False otherwise.

subset_set = {1, 2}
print(f"Subset set: {subset_set}")  # Output: {1, 2}
print(f"Is Subset set a subset of Set A? {subset_set.issubset(set_a)}")  # Output: True
print(f"Is Subset set a subset of Set B? {subset_set.issubset(set_b)}")  # Output: False
print()  # Just to add a newline for better readability

# issuperset() method is used to check if all elements of the second set are present in the first set. It returns True if the first set is a superset of the second set, and False otherwise.

print(
    f"Is Set A a superset of Subset set? {set_a.issuperset(subset_set)}"
)  # Output: True
print(
    f"Is Set B a superset of Subset set? {set_b.issuperset(subset_set)}"
)  # Output: False
print()  # Just to add a newline for better readability

# isdisjoint() method is used to check if two sets have no elements in common. It returns True if the sets are disjoint (i.e., they have no common elements), and False otherwise.

print(f"Is Set A disjoint with Set B? {set_a.isdisjoint(set_b)}")  # Output: False
set_c = {6, 7, 8}
print(f"Set C: {set_c}")  # Output: {6, 7, 8}
print(f"Is Set A disjoint with Set C? {set_a.isdisjoint(set_c)}")  # Output: True
print(f"Is Set B disjoint with Set C? {set_b.isdisjoint(set_c)}")  # Output: True
print()  # Just to add a newline for better readability

# copy() method is used to create a shallow copy of a set. It returns a new set that contains the same elements as the original set. If the original set is modified after copying, the copied set will not be affected, and vice versa.

original_set = {1, "Hello", 3.14, (1, 2), frozenset({5, 6})}
copied_set = original_set.copy()
print(
    f"Original set: {original_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6})}
print(
    f"Copied set: {copied_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6})}
original_set.add("New Element")
print(
    f"Original set after modification: {original_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6}), 'New Element'}
print(
    f"Copied set after original set modification: {copied_set}"
)  # Output: {1, 'Hello', 3.14, (1, 2), frozenset({5, 6})}
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------
