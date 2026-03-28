# -------------------------------------------------------------------------------------------------------------------------------------------

# 1. How can we use the while loop to iterate over a sequence?

# We can use a while loop to iterate over a sequence by maintaining an index variable that keeps track of our current position in the sequence. We can then use this index to access each element of the sequence until we have iterated through all of its elements.

print("Using a while loop to iterate over a list:")
fruits = ["apple", "banana", "cherry"]
index = 0
while index < len(fruits):
    print(f"Fruit: {fruits[index]}")
    index += 1  # Increment the index to move to the next element
print()  # Just to add a newline for better readability

# ----------------------------------------------------------------------------------------------------------------------------------------
