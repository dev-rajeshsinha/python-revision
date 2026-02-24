# -------------------------------------------------------------------------------------------------------------------------------------------

# Conditional Statements in Python are used to perform different actions based on different conditions. The most common conditional statements are if, elif, and else. The if statement is used to test a specific condition, and if that condition is true, the block of code inside the if statement will be executed. The elif statement is used to test multiple conditions, and it stands for "else if". If the condition in the if statement is false, the program will check the condition in the elif statement. If that condition is true, the block of code inside the elif statement will be executed. The else statement is used to execute a block of code when all previous conditions are false. The elif and else statements are optional, and we can have as many elif statements as needed, but only one else statement.

# We can also use nested if statements, which means we can have an if statement inside another if statement. This allows us to check for multiple conditions in a more complex way. Additionally, we can use logical operators (and, or, not) to combine multiple conditions in a single if statement.

age = input("Enter your age: ")

if age.isdigit():
    if int(age) < 18:
        print("You are a minor.")
    elif int(age) < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print(f"Invalid input: '{age}' is not a number.")
print()  # Just to add a newline for better readability of the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can also use the ternary operator in Python, which is a one-line conditional statement. It allows us to assign a value to a variable based on a condition. The syntax for the ternary operator is: `value_if_true if condition else value_if_false`. This can be useful for simple conditions where we want to assign a value based on whether a condition is true or false.

# We can use ternary operators inside a classical if-elif-else structure to make the code more concise. For example, we can determine the category of a person based on their age using a ternary operator.

age = input("Enter your age: ")

if age.isdigit():
    category = (
        "minor" if int(age) < 18 else "adult" if int(age) < 65 else "senior citizen"
    )
    print(f"You are a {category}.")
else:
    print(f"Invalid input: '{age}' is not a number.")
print()  # Just to add a newline for better readability of the output.

# We can also nest ternary operators, but it can make the code harder to read. It's important to use them judiciously and consider readability when using nested ternary operators.

age = input("Enter your age: ")

category = (
    "minor"
    if age.isdigit() and int(age) < 18
    else (
        "adult"
        if age.isdigit() and int(age) < 65
        else "senior citizen" if age.isdigit() else "invalid input"
    )
)
print(f"You are a {category}.")
print()  # Just to add a newline for better readability of the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Relational operators or Comparison operators in Python are used to compare values. They include:
# `==` (equal to): Returns True if the values on either side are equal
# `!=` (not equal to): Returns True if the values on either side are not equal
# `>` (greater than): Returns True if the value on the left is greater than the value on the right
# `<` (less than): Returns True if the value on the left is less than the value on the right
# `>=` (greater than or equal to): Returns True if the value on the left is greater than or equal to the value on the right
# `<=` (less than or equal to): Returns True if the value on the left is less than or equal to the value on the right

# We can use these relational operators in conditional statements (if, elif, else) to compare values and make decisions based on those comparisons.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Logical operators in Python are used to combine multiple conditions. They include:
# `and`: Returns True if both conditions are true
# `or`: Returns True if at least one of the conditions is true
# `not`: Returns True if the condition is false (negates the condition)

# We can use these logical operators in conditional statements (if, elif, else) to create more complex conditions.

# -------------------------------------------------------------------------------------------------------------------------------------------

# The pass statement in Python is a null statement that is used as a placeholder when a statement is required syntactically but no action is needed. It allows us to write code that is syntactically correct but does not perform any operation. This can be useful when we are writing code that is not yet complete or when we want to create a function or class that we will implement later.

# -------------------------------------------------------------------------------------------------------------------------------------------
