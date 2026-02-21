# ----------------------------------------------------------------------------------------------------------------------------------------

# In Python, the primarily used data types include:
# 1. int (Integer)
# 2. float (Floating-point)
# 3. str (String)
# 4. bool (Boolean)
# 5. list (List)
# 6. tuple (Tuple)
# 7. dict (Dictionary)
# 8. set (Set)
# 9. NoneType (None)

# ----------------------------------------------------------------------------------------------------------------------------------------

# A variable in Python is a named location in memory (RAM) that is used to store data. It can hold different types of data, such as numbers, strings, lists, etc. Variables are created when we assign a value to them using the assignment operator (=). A variable is also known as an identifier in some programming languages.

int_var = 10  # This is an integer variable
float_var = 3.14  # This is a floating-point variable
string_var = "Hello, World!"  # This is a string variable
bool_var = True  # This is a boolean variable
list_var = [1, 2, 3, 4, 5]  # This is a list variable
tuple_var = (1, 2, 3, 4, 5)  # This is a tuple variable
dict_var = {"name": "John", "age": 30}  # This is a dictionary variable
set_var = {1, 2, 3, 4, 5}  # This is a set variable
none_var = None  # This is a variable that holds the value None (null)

# While creating a variable, we can choose any name for it, but it must follow certain rules:
# 1. The variable name must start with a letter (a-z, A-Z) or an underscore (_).
# 2. The variable name can only contain letters, numbers, and underscores.
# 3. The variable name cannot be a reserved keyword in Python (e.g., if, else, for, while, etc.).
# 4. Variable names are case-sensitive (e.g., myVar and myvar are different variables).

# ----------------------------------------------------------------------------------------------------------------------------------------

# There are a number of operators are available in Python, which can be categorized into the following types:
# 1. Arithmetic Operators: +, -, *, /, %, //, **
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=
# 5. Bitwise Operators: &, |, ^, ~, <<, >>
# 6. Membership Operators: in, not in
# 7. Identity Operators: is, is not

# Examples of using arithmetic operators in Python:
print(f"10 + 5 = {10 + 5}")  # Output: 15 (Addition)
print(f"10 - 5 = {10 - 5}")  # Output: 5 (Subtraction)
print(f"10 * 5 = {10 * 5}")  # Output: 50 (Multiplication)
print(f"10 / 5 = {10 / 5}")  # Output: 2.0 (Division)
print(f"10 % 3 = {10 % 3}")  # Output: 1 (Modulus)
print(f"10 // 3 = {10 // 3}")  # Output: 3 (Floor Division)
print(f"10 ** 2 = {10 ** 2}")  # Output: 100 (Exponentiation)
print()  # Just to add a newline for better readability of the output

# Examples of using comparison operators in Python:
print(f"10 == 5: {10 == 5}")  # Output: False (Equal to)
print(f"10 != 5: {10 != 5}")  # Output: True (Not equal to)
print(f"10 > 5: {10 > 5}")  # Output: True (Greater than)
print(f"10 < 5: {10 < 5}")  # Output: False (Less than)
print(f"10 >= 5: {10 >= 5}")  # Output: True (Greater than or equal to)
print(f"10 <= 5: {10 <= 5}")  # Output: False (Less than or equal to)
print()  # Just to add a newline for better readability of the output

# Examples of using logical operators in Python:
print(f"True and False: {True and False}")  # Output: False (Logical AND)
print(f"True or False: {True or False}")  # Output: True (Logical OR)
print(f"not True: {not True}")  # Output: False (Logical NOT)
print(f"0 or 5: {0 or 5}")  # Output: 5 (Logical OR with integers)
print(f"0 and 5: {0 and 5}")  # Output: 0 (Logical AND with integers)
print()  # Just to add a newline for better readability of the output

# Examples of using assignment operators in Python:
x = 10  # Assignment operator
print(f"x = {x}")  # Output: 10
x += 5  # Equivalent to x = x + 5
print(f"x += 5: {x}")  # Output: 15
x -= 3  # Equivalent to x = x - 3
print(f"x -= 3: {x}")  # Output: 12
x *= 2  # Equivalent to x = x * 2
print(f"x *= 2: {x}")  # Output: 24
x /= 4  # Equivalent to x = x / 4
print(f"x /= 4: {x}")  # Output: 6.0
x %= 5  # Equivalent to x = x % 5
print(f"x %= 5: {x}")  # Output: 1.0
x //= 2  # Equivalent to x = x // 2
print(f"x //= 2: {x}")  # Output: 0.0
x **= 3  # Equivalent to x = x ** 3
print(f"x **= 3: {x}")  # Output: 0.0
print()  # Just to add a newline for better readability of the output

# Examples of using bitwise operators in Python:
print(f"5 & 3 = {5 & 3}")  # Output: 1 (Bitwise AND)
print(f"5 | 3 = {5 | 3}")  # Output: 7 (Bitwise OR)
print(f"5 ^ 3 = {5 ^ 3}")  # Output: 6 (Bitwise XOR)
print(f"~5 = {~5}")  # Output: -6 (Bitwise NOT)
print(f"5 << 1 = {5 << 1}")  # Output: 10 (Bitwise Left Shift)
print(f"5 >> 1 = {5 >> 1}")  # Output: 2 (Bitwise Right Shift)
print()  # Just to add a newline for better readability of the output

# Examples of using membership operators in Python:
my_list = [1, 2, 3, 4, 5]
print(f"3 in my_list: {3 in my_list}")  # Output: True (Membership operator 'in')
print(
    f"6 not in my_list: {6 not in my_list}"
)  # Output: True (Membership operator 'not in')
print()  # Just to add a newline for better readability of the output

# Examples of using identity operators in Python:
a = [1, 2, 3]
b = a  # b is assigned the same list as a
c = [1, 2, 3]  # c is a new list with the same content as a
print(f"a is b: {a is b}")  # Output: True (Identity operator 'is')
print(f"a is c: {a is c}")  # Output: False (Identity operator 'is')
print(f"a == c: {a == c}")  # Output: True (Equality operator '==')
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# type() function is used to determine the type of a variable or value in Python. It returns the type of the object passed as an argument.

print(f"type(10): {type(10)}")  # Output: <class 'int'> (Integer type)
print(f"type(3.14): {type(3.14)}")  # Output: <class 'float'> (Floating-point type)
print(
    f"type('Hello, World!'): {type('Hello, World!')}"
)  # Output: <class 'str'> (String type)
print(f"type(True): {type(True)}")  # Output: <class 'bool'> (Boolean type)
print(
    f"type([1, 2, 3, 4, 5]): {type([1, 2, 3, 4, 5])}"
)  # Output: <class 'list'> (List type)
print(
    f"type((1, 2, 3, 4, 5)): {type((1, 2, 3, 4, 5))}"
)  # Output: <class 'tuple'> (Tuple type)
print(
    f"type({{'name': 'John', 'age': 30}}): {type({'name': 'John', 'age': 30})}"
)  # Output: <class 'dict'> (Dictionary type)
print(
    f"type({{1, 2, 3, 4, 5}}): {type({1, 2, 3, 4, 5})}"
)  # Output: <class 'set'> (Set type)
print(f"type(None): {type(None)}")  # Output: <class 'NoneType'> (NoneType)
print()  # Just to add a newline for better readability of the output

# We can also cast a variable from one type to another using the built-in functions like int(), float(), str(), bool(), list(), tuple(), dict(), set(), etc.

print(f"String to Integer - int('10'): {int('10')}")  # Output: 10 (String to Integer)
print(
    f"String to Float - float('3.14'): {float('3.14')}"
)  # Output: 3.14 (String to Float)
print(f"Integer to String - str(10): {str(10)}")  # Output: '10' (Integer to String)
print(f"Integer to Boolean - bool(0): {bool(0)}")  # Output: False (Integer to Boolean)
print(
    f"Tuple to List - list((1, 2, 3)): {list((1, 2, 3))}"
)  # Output: [1, 2, 3] (Tuple to List)
print(
    f"List to Tuple - tuple([1, 2, 3]): {tuple([1, 2, 3])}"
)  # Output: (1, 2, 3) (List to Tuple)
print(
    f"List of tuples to Dictionary - dict([('name', 'John'), ('age', 30)]): {dict([('name', 'John'), ('age', 30)])}"
)  # Output: {'name': 'John', 'age': 30} (List of tuples to Dictionary)
print(
    f"List to Set - set([1, 2, 3, 4, 5, 5]): {set([1, 2, 3, 4, 5, 5])}"
)  # Output: {1, 2, 3, 4, 5} (List to Set)
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The input() function is used to take input from the user in Python. It reads a line of text from the user and returns it as a string. We can also provide a prompt message to the user by passing a string argument to the input() function.

name = input("Enter your name: ")  # Taking input from the user
print(f"Hello, {name}!")  # Output: Hello, <name>!
print(
    f"Your name is of type: {type(name)}"
)  # Output: Your name is of type: <class 'str'>

age = input("Enter your age: ")  # Taking input from the user
print(f"You are {age} years old.")  # Output: You are <age> years old.
print(f"Your age is of type: {type(age)}")  # Output: Your age is of type: <class 'str'>
