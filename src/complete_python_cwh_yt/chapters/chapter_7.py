# -------------------------------------------------------------------------------------------------------------------------------------------

# Loops in Python are used to execute a block of code repeatedly until a certain condition is met. There are two main types of loops in Python: for loops and while loops. A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects, where the number of iterations is known beforehand. A while loop is used to execute a block of code as long as a specified condition is true. A while loop is primarily used when the number of iterations is not known beforehand.

# -------------------------------------------------------------------------------------------------------------------------------------------

# A for loop is constructed using the 'for' keyword, followed by a variable name, the 'in' keyword, and the sequence to iterate over. The block of code to be executed for each item in the sequence is indented under the for statement. The sequence a for loop iterates over can be a list, tuple, string, or any other iterable object. The for loop will execute the block of code once for each item in the sequence, with the variable taking on the value of each item in turn.

print("Iterating over a list of fruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
print()  # Just to add a newline for better readability

# We can also iterate over a range of numbers using the range() function, which generates a sequence of numbers. The range() function can take one, two, or three arguments: start, stop, and step. If only one argument is provided, it is treated as the stop value, and the start value defaults to 0. If two arguments are provided, they are treated as the start and stop values. If three arguments are provided, they are treated as the start, stop, and step values.

print("Using range() with one argument:")
for i in range(5):
    print(f"Number: {i}")
print()  # Just to add a newline for better readability

print("Using range() with two arguments:")
for i in range(1, 6):
    print(f"Number: {i}")
print()  # Just to add a newline for better readability

print("Using range() with three arguments:")
for i in range(0, 10, 2):
    print(f"Even Number: {i}")
print()  # Just to add a newline for better readability

# We can also use the range() function to iterate over a sequence of numbers in reverse order by providing a negative step value.

print("Using range() to iterate in reverse order:")
for i in range(10, 0, -1):
    print(f"Number: {i}")
print()  # Just to add a newline for better readability

# We can also use the range() function to iterate over a sequence of items based on their index. This is useful when we need to access both the index and the value of each item in the sequence.

print("Iterating over a list with index using range():")
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index: {i}, Fruit: {fruits[i]}")
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# A while loop is constructed using the 'while' keyword, followed by a condition. The block of code to be executed as long as the condition is true is indented under the while statement. The while loop will continue to execute the block of code until the condition becomes false. It is important to ensure that the condition will eventually become false, otherwise, the loop will run indefinitely, which is also known as an infinite loop.

print("Using a while loop to count from 1 to 5:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the count to avoid an infinite loop
print()  # Just to add a newline for better readability

# We can also use a while loop to create an infinite loop by not providing a condition that becomes false. This can be useful in certain scenarios, such as when we want to continuously accept user input until a specific condition is met.

# print("Using a while loop to create an infinite loop (press Ctrl+C to stop):")
# Uncomment the following lines to see the infinite loop in action
# while True:
#     user_input = input("Enter something (type 'exit' to stop): ")
#     if user_input.lower() == 'exit':
#         break  # Exit the loop if the user types 'exit'
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can use the 'break' statement to exit a loop prematurely when a certain condition is met. Whereas, the 'continue' statement can be used to skip the current iteration of the loop and move on to the next iteration. These statements can be used in both for and while loops to control the flow of the loop based on specific conditions.

print("Using break in a for loop:")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i = 5")
        break  # Exit the loop when i is 5
    print(f"Number: {i}")
print()  # Just to add a newline for better readability

print("Using continue in a for loop:")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue  # Skip the rest of the loop for even numbers
    print(f"Number: {i}")
print()  # Just to add a newline for better readability

print("Using break in a while loop:")
count = 1
while count <= 10:
    if count == 5:
        print("Breaking the loop at count = 5")
        break  # Exit the loop when count is 5
    print(f"Count: {count}")
    count += 1
print()  # Just to add a newline for better readability

print("Using continue in a while loop:")
count = 1
while count <= 10:
    if count % 2 == 0:
        print(f"Skipping even count: {count}")
        count += 1
        continue  # Skip the rest of the loop for even counts
    print(f"Count: {count}")
    count += 1
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can use the word 'else' in conjunction with loops to execute a block of code after the loop has completed its iterations. The 'else' block will only be executed if the loop was not terminated by a 'break' statement. This can be useful for scenarios where we want to perform some action after successfully completing the loop without any interruptions.

print("Using else with a for loop:")
for i in range(1, 5):
    print(f"Number: {i}")
else:
    print("Loop completed without break.")
print()  # Just to add a newline for better readability

print("Using else with a while loop:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
else:
    print("While loop completed without break.")
print()  # Just to add a newline for better readability

print("Using else with a for loop that has a break:")
for i in range(1, 5):
    if i == 3:
        print("Breaking the loop at i = 3")
        break  # Exit the loop when i is 3
    print(f"Number: {i}")
else:
    print("This will not be printed because the loop was broken.")
print()  # Just to add a newline for better readability

print("Using else with a while loop that has a break:")
count = 1
while count <= 5:
    if count == 3:
        print("Breaking the loop at count = 3")
        break  # Exit the loop when count is 3
    print(f"Count: {count}")
    count += 1
else:
    print("This will not be printed because the loop was broken.")
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------

# Both for and while loops can be used as well to iterate over a string, which is a sequence of characters. When we iterate over a string using a loop, we can access each character in the string one by one.

print("Using a for loop to iterate over a string:")
text = "Hello"
for char in text:
    print(f"Character: {char}")
print()  # Just to add a newline for better readability

print("Using a while loop to iterate over a string:")
index = 0
while index < len(text):
    print(f"Character: {text[index]}")
    index += 1
print()  # Just to add a newline for better readability

# -------------------------------------------------------------------------------------------------------------------------------------------
