# -------------------------------------------------------------------------------------------------------------------------------------------

# 1. Can we have a set with two values 8 (as integer) and 8.0 (as float)?

# Yes, we can have a set with both 8 (as an integer) and 8.0 (as a float). However, since sets do not allow duplicate values and 8 and 8.0 are considered equal in Python, because 8 == 8.0 evaluates to True, so only one of them will be stored in the set. Now, which one will be stored depends on the order of insertion. If we insert 8 first, then 8.0 will not be added to the set because it is considered a duplicate. Conversely, if we insert 8.0 first, then 8 will not be added for the same reason.

sample_set = {8, 8.0}
print(f"Set with 8 and 8.0: {sample_set}")  # Output: {8}

# 2. Can we have a set with two values 8 (as integer) and "8" (as string)?

# Yes, we can have a set with both 8 (as an integer) and "8" (as a string). In this case, they are considered different values because they are of different data types. Therefore, both 8 and "8" will be stored in the set without any issues.

sample_set = {8, "8"}
print(f"Set with 8 and '8': {sample_set}")  # Output: {8, '8'}

# 3. If there is a list inside a set, can we change the values of that list?

# No, we cannot have a list inside a set because lists are mutable and sets require their elements to be immutable. If we try to add a list to a set, we will get a TypeError. However, if we have a tuple (which is immutable) inside a set, we can change the values of the tuple by creating a new tuple with the desired values and replacing the old one in the set.

# -------------------------------------------------------------------------------------------------------------------------------------------
