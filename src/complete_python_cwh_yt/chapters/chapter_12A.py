# -------------------------------------------------------------------------------------------------------------------------------------------

# The walrus operator in Python, denoted by :=, is a new assignment expression introduced in Python 3.8. It allows us to assign a value to a variable as part of an expression. This can be particularly useful in situations where we want to use the value of a variable immediately after assigning it, without needing to write a separate line of code for the assignment. The walrus operator can help make code more concise and readable by reducing the need for temporary variables and allowing for more compact expressions.

# Using the walrus operator in a while loop

starting_value = 0
while (current_value := starting_value) < 5:
    print(f"Square of {current_value} is {current_value ** 2}")
    starting_value += 1
print()  # Just to add a newline for better readability of the output.

# In this example, we use the walrus operator to assign the value of starting_value to current_value within the while loop condition. This allows us to check if current_value is less than 5 and print its square without needing a separate line for the assignment. The loop continues until current_value reaches 5, at which point it will stop executing.

# If we wouldn't have used the walrus operator, we would have needed to write something like this:

starting_value = 0
while starting_value < 5:
    current_value = starting_value
    print(f"Square of {current_value} is {current_value ** 2}")
    starting_value += 1
print()  # Just to add a newline for better readability of the output.

# As we can see, the walrus operator allows us to combine the assignment and the condition check into a single line, making the code more concise and easier to read. We can use this operator in various contexts, such as in list comprehensions, if statements, and more, to improve the efficiency and readability of our code.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Type hinting in Python is a feature that allows developers to indicate the expected data types of variables, function parameters, and return values. This can help improve code readability and maintainability by providing clear information about the types of data being used. Type hints are not enforced at runtime, but they can be checked using static type checkers like mypy. Type hinting can be particularly useful in larger codebases or when working in teams, as it helps to catch potential type-related errors early in the development process. It also serves as documentation for other developers who may be working with the code, making it easier to understand the intended use of variables and functions.

# Example of type hinting for variables

age: int = 25
name: str = "Alice"
height: float = 5.6
is_alive: bool = True
hobbies: list[str] = ["reading", "coding", "hiking"]
parents: dict[str, str] = {"father": "John", "mother": "Jane"}
birth_date: tuple[int, int, int] = (1995, 5, 15)


# Example of type hinting in a function


def greet(name: str) -> str:
    return f"Hello, {name}!"


# In this example, we have a function called greet that takes a parameter name, which is expected to be of type str (string), and the function itself is expected to return a value of type str. The type hints provide information about the expected types of the input and output, making it easier for developers to understand how to use the function correctly. If we were to call this function with an argument that is not a string, a static type checker would raise an error, helping us catch potential issues before they occur at runtime.

# For example, if we try to call the greet function with an integer instead of a string:

# greet(123)  # This will raise a type error when checked with a static type checker, though it will not raise an error at runtime.

# We can use type hinting in various contexts, such as for variables, function parameters, and return types, to improve the clarity and maintainability of our code. It is a powerful tool that can help developers write more robust and error-free code by providing clear expectations about the types of data being used.

# While declaring a list, dictionary, or tuple, we can also use the corresponding classes from the typing module to provide more specific type hints. However, this approach is not recommended now, as we can use the built-in types with square brackets for type hinting, which is more concise and easier to read. The typing module's classes like List, Dict, and Tuple were used in earlier versions of Python for type hinting, but with the introduction of PEP 585 in Python 3.9, we can now use the built-in types directly for type hinting.

from typing import List, Dict, Tuple

my_list: List[int] = [
    1,
    2,
    3,
    4,
    5,
]  # Rather than using List[int], we can simply use list[int] in Python 3.9 and later.
my_dict: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
}  # Rather than using Dict[str, int], we can simply use dict[str, int] in Python 3.9 and later.
my_tuple: Tuple[int, str, float] = (
    1,
    "hello",
    3.14,
)  # Rather than using Tuple[int, str, float], we can simply use tuple[int, str, float] in Python 3.9 and later.

# There is also some other type hinting syntax that we can use, such as Union, Optional, and Any, which are part of the typing module. These can be used to indicate that a variable or function parameter can accept multiple types or that a value can be of any type.

from typing import Union, Optional, Any

can_be_int_or_str: Union[int, str] = (
    "Hello"  # This variable can be either an int or a str.
)
can_be_int_or_str = 42  # This variable can also be an int.
can_be_int_or_str = "World"  # This variable can also be a str.
# can_be_int_or_str = [
#     1,
#     2,
#     3,
# ]  # If we try to assign a list to this variable, a static type checker would raise an error, as it is not an int or a str.

optional_value: Optional[int] = None  # This variable can be an int or None.
optional_value = 10  # This variable can also be an int.
# optional_value = "Hello"  # If we try to assign a str to this variable, a static type checker would raise an error, as it is not an int or None.

any_value: Any = "Hello"  # This variable can be of any type.
any_value = 42  # This variable can also be an int.
any_value = [1, 2, 3]  # This variable can also be a list.

# -------------------------------------------------------------------------------------------------------------------------------------------

# The match-case statement in Python, introduced in Python 3.10, is a powerful control flow structure that allows for pattern matching. It provides a more concise and readable way to handle multiple conditions compared to traditional if-elif-else statements. The match-case statement can be used to match values against specific patterns, making it easier to write code that is both clear and efficient.

# Example of using match-case statement


def process_value(value):
    match value:
        case 0:
            return "Value is zero"
        case 1:
            return "Value is one"
        case 2 | 3 | 4:
            return "Value is between two and four"
        case _ if value < 0:
            return "Value is negative"
        case _:
            return "Value is something else"


# In this example, the match-case statement is used to check the value of the variable value against different cases. The first case checks if the value is 0, the second case checks if it is 1, and the third case checks if it is either 2, 3, or 4. The fourth case uses a guard (the if statement) to check if the value is negative, and the final case (using _) serves as a catch-all for any other values that do not match the previous cases. This structure allows for clear and concise handling of multiple conditions without the need for nested if-elif-else statements, making the code easier to read and maintain. The match-case statement can also be used with more complex patterns, such as matching against data structures like lists or dictionaries, further enhancing its versatility in handling various scenarios.

# Note: The '_' in the match-case statement is a wildcard pattern that matches any value. It is often used as a catch-all case to handle situations where none of the previous cases match. In the example above, the case _ serves as a default case that will be executed if the value does not match any of the specified cases (0, 1, 2, 3, 4, or negative values). This allows us to ensure that all possible values are accounted for in our code, providing a fallback option for unexpected inputs.

# -------------------------------------------------------------------------------------------------------------------------------------------

# While using context managers in Python, we can open or use multiple resources within a single with statement by separating them with commas. This allows us to manage multiple resources efficiently and ensures that all of them are properly closed or released when the block of code is exited, even if an error occurs.

print("Using multiple context managers in a single with statement:")
with (
    open(
        "../resources/main.txt",
        "r",
    ) as main_file,
    open("../resources/logs.txt", "r") as logs_file,
):
    main_file_content = main_file.read()
    logs_file_content = logs_file.read()
    print(f"Content of main.txt: {main_file_content}")
    print(f"Content of logs.txt: {logs_file_content}")
    print()  # Just to add a newline for better readability of the output.

# In this example, we are opening two files, main.txt and logs.txt, using a single with statement. By separating the context managers with commas, we can manage both files simultaneously. When the block of code is exited, both files will be automatically closed, ensuring that we do not have to worry about manually closing them or handling exceptions that may arise during file operations. This approach helps to keep our code clean and efficient when working with multiple resources.

# We can also use multiple context managers with other types of resources, such as database connections, network connections, or any other objects that support the context management protocol. This allows us to manage various resources in a consistent and efficient manner, ensuring that they are properly released when no longer needed.

# Example of using multiple context managers with a database connection and a file


class DatabaseConnection:
    """
    A simple custom context manager to simulate a database connection.
    """

    def __enter__(self):
        print("Opening database connection")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection")

    def query(self, sql):
        print(f"Executing query: {sql}")


print("Using multiple context managers with a database connection and a file:")
with DatabaseConnection() as db, open("../resources/main.txt", "r") as main_file:
    db.query("SELECT * FROM users")
    main_file_content = main_file.read()
    print(f"Content of main.txt: {main_file_content}")
print()  # Just to add a newline for better readability of the output.

# In this example, we are using a custom context manager for a database connection along with a file context manager. The DatabaseConnection class implements the __enter__ and __exit__ methods to manage the opening and closing of the database connection. By using both context managers in a single with statement, we can ensure that both the database connection and the file are properly managed, with resources being released when they are no longer needed. This approach helps to keep our code organized and efficient when working with multiple resources.

# -------------------------------------------------------------------------------------------------------------------------------------------

# The if __name__ == "__main__": block is a common Python idiom that is used to determine whether a Python file is being run as the main program or if it is being imported as a module in another script. When a Python file is run directly, the special variable __name__ is set to "__main__". However, when the same file is imported as a module, __name__ is set to the name of the module. This allows us to write code that will only execute when the file is run directly, and not when it is imported. This is particularly useful for testing or for code that should only run in a specific context.

# def main():
#     print("This code will only run when the file is executed directly.")

# if __name__ == "__main__":
#     main()

# In this example, we define a main function that contains code we want to execute only when the file is run directly. The if __name__ == "__main__": block checks if the file is being run as the main program, and if so, it calls the main function. If this file were to be imported as a module in another script, the code inside the main function would not execute, allowing us to control the behavior of our code based on how it is being used.

# ----------------------------------------------------------------------------------------------------------------------------------------------

# The global keyword in Python is used to declare that a variable inside a function is global, meaning that it refers to a variable defined outside the function. This allows us to modify the value of a global variable from within a function. Without using the global keyword, any assignment to a variable inside a function would create a new local variable, and the global variable would remain unchanged. Using the global keyword can be useful when we want to maintain state across function calls or when we need to modify a variable that is shared across multiple functions. However, it is generally recommended to use global variables sparingly, as they can make code harder to understand and maintain.

counter = 0  # This is a global variable


def increment_counter():
    global counter  # Declare that we want to use the global variable 'counter'
    counter += 1  # Increment the global counter
    print(f"Counter value inside function: {counter}")


increment_counter()  # This will increment the counter to 1
increment_counter()  # This will increment the counter to 2
print(
    f"Counter value outside function: {counter}"
)  # This will print the current value of the counter, which is 2
print()  # Just to add a newline for better readability of the output.

# In this example, we have a global variable counter that is initialized to 0. The increment_counter function uses the global keyword to indicate that it wants to modify the global counter variable. Each time the function is called, it increments the counter by 1 and prints its value. When we call increment_counter twice, the counter is incremented to 2, and we can see the updated value both inside and outside the function. This demonstrates how the global keyword allows us to modify a global variable from within a function.

# Note: If we are declaring a variable as global inside a function, we must ensure that the variable is declared as global first, before assigning a value to it. If we try to assign a value to a variable before declaring it as global, we will get an error because Python will treat it as a local variable and will not recognize the global variable. Therefore, it is important to declare the variable as global before using it in the function.

# ----------------------------------------------------------------------------------------------------------------------------------------------

# The enumerate function in Python is a built-in function that allows us to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of the current item. It returns an enumerate object, which is an iterator that produces pairs of index and value for each item in the sequence. This can be particularly useful when we need to access both the index and the value of items in a loop without having to manually manage a separate counter variable.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
print()  # Just to add a newline for better readability of the output.

fruits = ("apple", "banana", "cherry")
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
print()  # Just to add a newline for better readability of the output.

fruits = "apple"
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Character: {fruit}")
print()  # Just to add a newline for better readability of the output.

# In these examples, we use the enumerate function to iterate over a list of fruits, a tuple of fruits, and a string of characters. The enumerate function provides both the index and the value for each item in the sequence, allowing us to easily access and print both pieces of information in our loop. This makes our code more concise and easier to read compared to manually managing an index variable.

# ----------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehensions in Python are a concise way to create lists. They allow us to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. List comprehensions can make our code more readable and efficient by reducing the need for explicit loops and temporary variables. They consist of brackets containing an expression followed by a for clause, and optionally, one or more if clauses. The expression is evaluated for each item in the iterable, and the resulting values are collected into a new list.

# Example of a simple list comprehension to create a list of squares

squares = [x**2 for x in range(10)]
print(f"Squares from 0 to 9: {squares}")
print()  # Just to add a newline for better readability of the output.

# Example of a list comprehension with a condition to filter square of even numbers

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares of even numbers from 0 to 9: {even_squares}")
print()  # Just to add a newline for better readability of the output.

# Example of a list comprehension to create a list of tuples containing numbers and their squares

number_square_tuples = [(x, x**2) for x in range(10)]
print(f"Tuples of numbers and their squares from 0 to 9: {number_square_tuples}")
print()  # Just to add a newline for better readability of the output.

# In these examples, we use list comprehensions to create new lists based on a range of numbers. The first example generates a list of squares for numbers from 0 to 9. The second example filters the numbers to include only even numbers before calculating their squares. The third example creates a list of tuples, where each tuple contains a number and its corresponding square. List comprehensions provide a powerful and elegant way to generate lists in Python, making our code more concise and easier to read.

# ----------------------------------------------------------------------------------------------------------------------------------------------
