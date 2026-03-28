# -------------------------------------------------------------------------------------------------------------------------------------------

# Exception Handling in Python is a powerful mechanism to handle errors gracefully and maintain the flow of the program. It allows developers to catch and manage exceptions that may occur during the execution of a program, preventing it from crashing and providing an opportunity to respond to errors in a controlled manner. If we don't handle exceptions, our program may terminate abruptly when an error occurs, leading to a poor user experience and potential data loss. By using exception handling, we can ensure that our program continues to run smoothly even when unexpected situations arise.

# To handle exceptions in Python, we use the try-except block. The code that may raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block. We can also use multiple except blocks to handle different types of exceptions separately. Additionally, we can use the finally block to execute code that must run regardless of whether an exception occurred or not.

# Example of exception handling in Python:

try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This block will always execute, regardless of exceptions.")
    print()  # Just to add a newline for better readability

# In this example, we are trying to divide two numbers input by the user. If the user enters zero as the second number, a ZeroDivisionError will be raised, and we handle it in the first except block. If the user enters a non-integer value, a ValueError will be raised, and we handle it in the second except block. The third except block is a catch-all for any other unexpected exceptions that may occur as we have used the base Exception class which acts as a universal exception handler that can catch any exception that is not caught by the previous except blocks. The finally block ensures that a message is printed regardless of whether an exception occurred or not, demonstrating the use of the finally block in exception handling.

# We can also raise exceptions intentionally using the raise statement. This is useful when we want to enforce certain conditions in our code or when we want to create custom exceptions for specific error handling scenarios.


def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Age is valid.")


try:
    user_age = int(input("Enter your age: "))
    validate_age(user_age)
except ValueError as ve:
    print(f"Validation error: {ve}")
print()  # Just to add a newline for better readability of the output.

# In this example, we have a function validate_age that checks if the age provided is valid. If the age is negative or less than 18, it raises a ValueError with an appropriate message. We then call this function inside a try block and catch any ValueError that may be raised, printing the error message to the user. This demonstrates how we can use the raise statement to create custom exceptions and handle them effectively in our code.

# We can combine multiple exceptions in a single except block by using a tuple to specify the exceptions we want to catch. This can help simplify our code when we want to handle multiple exceptions in the same way.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
print()  # Just to add a newline for better readability of the output.

# We can also use the else block in a try-except structure, which will execute if no exceptions were raised in the try block. This can be useful for code that should only run if the try block was successful.

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result of {num1} divided by {num2} is: {result}")
print()  # Just to add a newline for better readability of the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can create custom exceptions in Python by defining a new class that inherits from the built-in Exception class. This allows us to create specific error types that can be used to handle particular situations in our code.


class CustomError(Exception):
    """Custom exception for specific error handling."""

    pass


def risky_function(value):
    if value < 0:
        raise CustomError("Value cannot be negative.")
    elif value == 0:
        raise CustomError("Value cannot be zero.")
    else:
        print(f"Value {value} is valid.")


try:
    user_value = int(input("Enter a value: "))
    risky_function(user_value)
except CustomError as ce:
    print(f"Custom error occurred: {ce}")
print()  # Just to add a newline for better readability of the output.

# In this example, we define a custom exception called CustomError that inherits from the Exception class. The risky_function raises a CustomError if the input value is negative or zero. We then call this function inside a try block and catch any CustomError that may be raised, printing the error message to the user. This demonstrates how we can create and use custom exceptions to handle specific error scenarios in our code.

# ----------------------------------------------------------------------------------------------------------------------------------------------
