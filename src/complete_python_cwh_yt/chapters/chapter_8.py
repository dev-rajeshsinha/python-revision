# -------------------------------------------------------------------------------------------------------------------------------------------

# Functions in Python are reusable blocks of code that perform a specific task. They allow us to break our code into smaller, more manageable pieces, and can be called multiple times throughout our program for reusability. Functions can take parameters (inputs) and can return values (outputs).

# To define a function in Python, we use the 'def' keyword followed by the function name and parentheses. If the function takes parameters, we include them within the parentheses. The block of code that makes up the function is indented under the function definition. We can call a function by using its name followed by parentheses, and if it takes parameters, we provide the arguments within the parentheses.


def greet(name):  # The 'greet' function takes one parameter, 'name'.
    """This function takes a name as an argument and prints a greeting message."""
    print(f"Hello, {name}! Welcome to Python programming.")


# We can call the greet function with different names to see the greeting message. The different names we pass to the function are called arguments, and they will be used in place of the parameter 'name' within the function during the function execution.

greet("Alice")  # Output: Hello, Alice! Welcome to Python programming.
greet("Bob")  # Output: Hello, Bob! Welcome to Python programming.
print()  # Just to add a newline for better readability.

# We can also ask the user for input and pass that input to the function.

user_name = input("Please enter your name: ")
greet(user_name)  # Output will depend on the user's input.
print()  # Just to add a newline for better readability.

# Functions can also return values. To return a value from a function, we use the 'return' statement followed by the value we want to return. This allows us to capture the output of the function and use it elsewhere in our code. Along with returning values, we can define functions that can take multiple parameters and perform more complex operations.


def add_numbers(a, b):  # The 'add_numbers' function takes two parameters, 'a' and 'b'.
    """This function takes two numbers as arguments and returns their sum."""
    return a + b


result = add_numbers(
    5, 3
)  # The 'add_numbers' function is called with arguments 5 and 3, and the result is stored in the variable 'result'.
print(f"The sum of 5 and 3 is: {result}")  # Output: The sum of 5 and 3 is: 8
print()  # Just to add a newline for better readability.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum_result = add_numbers(
    first_number, second_number
)  # The 'add_numbers' function is called with user input, and the result is stored in 'sum_result'.
print(
    f"The sum of {first_number} and {second_number} is: {sum_result}"
)  # Output will depend on the user's input.
print()  # Just to add a newline for better readability.

# We can also define functions that take no parameters and simply perform a task or print a message.


def say_hello():
    """This function takes no parameters and prints a greeting message."""
    print("Hello! This is a function with no parameters.")


say_hello()  # Output: Hello! This is a function with no parameters.
print()  # Just to add a newline for better readability.

# -------------------------------------------------------------------------------------------------------------------------------------------

# In Python, we can also define functions that take a variable number of arguments using the *args syntax. This allows us to pass an arbitrary number of arguments to the function, which will be treated as a tuple within the function. This is useful when we don't know in advance how many arguments will be passed to the function.


def sum_all(*args):
    """This function takes a variable number of arguments and returns their sum."""
    total = 0
    for num in args:
        total += num
    return total


result = sum_all(
    1, 2, 3
)  # The 'sum_all' function is called with three arguments, and the result is stored in 'result'.
print(f"The sum of 1, 2, and 3 is: {result}")  # Output: The sum of 1, 2, and 3 is: 6
print()  # Just to add a newline for better readability.

result = sum_all(
    1, 2, 3, 4, 5
)  # The 'sum_all' function is called with multiple arguments, and the result is stored in 'result'.
print(
    f"The sum of 1, 2, 3, 4, and 5 is: {result}"
)  # Output: The sum of 1, 2, 3, 4, and 5 is: 15
print()  # Just to add a newline for better readability.

# We can also use the *args syntax to pass a list of numbers to the function by unpacking the list using the * operator.

numbers = [1, 2, 3, 4, 5]
result = sum_all(
    *numbers
)  # The 'sum_all' function is called with the unpacked list of numbers, and the result is stored in 'result'.
print(
    f"The sum of the numbers in the list is: {result}"
)  # Output: The sum of the numbers in the list is: 15
print()  # Just to add a newline for better readability.

# We can also define functions that take keyword arguments using the **kwargs syntax. This allows us to pass an arbitrary number of keyword arguments to the function, which will be treated as a dictionary within the function. This is useful when we want to pass named arguments to the function.


def print_info(**kwargs):
    """This function takes a variable number of keyword arguments and prints them."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(
    name="Alice", age=30, city="New York"
)  # Output: name: Alice, age: 30, city: New York
print()  # Just to add a newline for better readability.

info = {"name": "Bob", "age": 25, "city": "Los Angeles"}
print_info(
    **info
)  # The 'print_info' function is called with the unpacked dictionary of information, and the output will be: name: Bob, age: 25, city: Los Angeles
print()  # Just to add a newline for better readability.

# We can also combine *args and **kwargs in the same function to allow for both variable positional arguments and variable keyword arguments.


def display_info(*args, **kwargs):
    """This function takes both variable positional arguments and variable keyword arguments and displays them."""
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(
    "Hello", "World", name="Alice", age=30
)  # Output: Positional arguments: Hello, World; Keyword arguments: name: Alice, age: 30
print()  # Just to add a newline for better readability.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Unpacking arguments in Python allows us to pass a collection of items (like a list, tuple, or dictionary) to a function as individual arguments. This is done using the * operator for unpacking iterables and the ** operator for unpacking dictionaries.


def multiply(a, b, c):
    """This function takes three numbers as arguments and returns their product."""
    return a * b * c


numbers = [2, 3, 4]
result = multiply(
    *numbers
)  # The 'multiply' function is called with the unpacked list of numbers, and the result is stored in 'result'.
print(
    f"The product of 2, 3, and 4 is: {result}"
)  # Output: The product of 2, 3, and 4 is: 24
print()  # Just to add a newline for better readability.

info = {"a": 2, "b": 3, "c": 4}
result = multiply(
    **info
)  # The 'multiply' function is called with the unpacked dictionary of information, and the result will be: The product of 2, 3, and 4 is: 24
print(
    f"The product of 2, 3, and 4 is: {result}"
)  # Output: The product of 2, 3, and 4 is: 24
print()  # Just to add a newline for better readability.

# -------------------------------------------------------------------------------------------------------------------------------------------

# In Python, we can also define functions that have default parameter values. This means that if the caller does not provide a value for that parameter, the function will use the default value instead. This is useful for providing flexibility in function calls while still ensuring that the function has all the necessary information to execute properly.


def greet_updated(name="Guest"):
    """This function takes a name as an argument and prints a greeting message. If no name is provided, it defaults to 'Guest'."""
    print(f"Hello, {name}! Welcome to Python programming.")


greet_updated()  # Output: Hello, Guest! Welcome to Python programming.
greet_updated("Alice")  # Output: Hello, Alice! Welcome to Python programming.
print()  # Just to add a newline for better readability.


def add_numbers_updated(a, b=0):
    """This function takes two numbers as arguments and returns their sum. The second number defaults to 0 if not provided."""
    return a + b


result = add_numbers_updated(
    5
)  # The 'add_numbers_updated' function is called with only one argument, and the result is stored in 'result'.
print(
    f"The sum of 5 and the default value is: {result}"
)  # Output: The sum of 5 and the default value is: 5
result = add_numbers_updated(
    5, 3
)  # The 'add_numbers_updated' function is called with two arguments, and the result is stored in 'result'.
print(f"The sum of 5 and 3 is: {result}")  # Output: The sum of 5 and 3 is: 8
print()  # Just to add a newline for better readability.

# We can also use default parameter values in combination with *args and **kwargs to provide even more flexibility in our function definitions.


def display_info_updated(name="Guest", *args, **kwargs):
    """This function takes a name as a default parameter, variable positional arguments, and variable keyword arguments, and displays the information."""
    print(f"Name: {name}")
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info_updated(
    "Alice", "Hello", "World", age=30, city="New York"
)  # Output: Name: Alice; Positional arguments: Hello, World; Keyword arguments: age: 30, city: New York
print()  # Just to add a newline for better readability.

display_info_updated(
    age=25, city="Los Angeles"
)  # Output: Name: Guest; Positional arguments: (none); Keyword arguments: age: 25, city: Los Angeles
print()  # Just to add a newline for better readability.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Along with defining our own functions, Python also provides a wide range of built-in functions that we can use in our programs. These built-in functions perform common tasks and are readily available for us to use without needing to import any additional modules. Some examples of built-in functions include 'print()', 'len()', 'type()', 'input()', and many more.

# - The 'print()' function is used to output information to the console. It can take multiple arguments and will print them all on the same line by default, separated by a space.
# - The 'len()' function is used to get the length of a string, list, tuple, or other iterable. It returns the number of items in the iterable.
# - The 'type()' function is used to determine the type of a variable or value. It returns the type as a string.
# - The 'input()' function is used to get user input from the console. It takes an optional prompt string as an argument and returns the input as a string.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Recursion in Python is a programming technique where a function calls itself in order to solve a problem. A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller subproblems and calls the function on those subproblems. It is important to ensure that the base case is reached eventually to prevent infinite recursion, which can lead to a stack overflow error. A recursive function can accept parameters and return values just like any other function as well.


def factorial(n):
    """This function takes a non-negative integer n and returns its factorial using recursion."""
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:  # Recursive case: factorial of n is n multiplied by factorial of (n-1)
        return n * factorial(n - 1)


result = factorial(
    5
)  # The 'factorial' function is called with the argument 5, and the result is stored in 'result'.
print(f"The factorial of 5 is: {result}")  # Output: The factorial of 5 is: 120
print()  # Just to add a newline for better readability.

result = factorial(
    0
)  # The 'factorial' function is called with the argument 0, and the result is stored in 'result'.
print(f"The factorial of 0 is: {result}")  # Output: The factorial of 0 is: 1
print()  # Just to add a newline for better readability.

# -------------------------------------------------------------------------------------------------------------------------------------------
