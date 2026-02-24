# ----------------------------------------------------------------------------------------------------------------------------------------

# We can create a string in Python by enclosing characters in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Triple quotes are used when we want to create a multi-line string.

single_quote_string = "This is a string created using single quotes."
double_quote_string = "This is a string created using double quotes."
triple_quote_string = """This is a string created using triple quotes.
It can span multiple lines."""

print(single_quote_string)  # Output: This is a string created using single quotes.
print(double_quote_string)  # Output: This is a string created using double quotes.
print(triple_quote_string)  # Output: This is a string created using triple quotes.
print()  # Just to add a newline for better readability of the output

# A string in Python is an immutable sequence of characters. This means that once a string is created, it cannot be modified. If we try to change a character in a string, it will create a new string object instead of modifying the existing one.

string_obj = "This is a string object in Python."
print(
    f"ID of created string object: {id(string_obj)}"
)  # Output: ID of string_obj: <some unique identifier>

string_obj = "This is an updated string object in Python."
print(
    f"ID of updated string object: {id(string_obj)}"
)  # Output: ID of updated string_obj: <some unique identifier>
print()  # Just to add a newline for better readability of the output

# We can access individual characters in a string using their index, which starts from 0. We can also use negative indices to access characters from the end of the string, where -1 is the last character. But we cannot modify the characters in a string directly since strings are immutable.

string_obj = "Hello, World!"
print(f"Original string: {string_obj}")  # Output: Original string: Hello, World!
print(f"string_obj[0]: {string_obj[0]}")  # Output: string_obj[0]: H
print(f"string_obj[7]: {string_obj[7]}")  # Output: string_obj[7]: W

# The following line will raise an error because we cannot modify a string directly.
# string_obj[0] = 'h'  # This will raise a TypeError: 'str' object does not support item assignment

# ----------------------------------------------------------------------------------------------------------------------------------------

# Slicing a string allows us to extract a portion of the string by specifying a range of indices. The syntax for slicing is: string[start:stop:step]. The 'start' index is inclusive, while the 'stop' index is exclusive. The 'step' parameter is optional and specifies the step size for slicing, which implies the interval between each character to be included in the slice, for example: string[0:10:2] will include every second character from index 0 to 9.

string_obj = "Hello, World!"
print(f"Original string: {string_obj}")  # Output: Original string: Hello, World!
print(f"Sliced string (0:5): {string_obj[0:5]}")  # Output: Sliced string (0:5): Hello
print(
    f"Sliced string (7:12): {string_obj[7:12]}"
)  # Output: Sliced string (7:12): World
print(
    f"Sliced string (0:len(string_obj):2): {string_obj[0:len(string_obj):2]}"
)  # Output: Sliced string (0:len(string_obj):2): Hlo ol!

# We can also use negative indices to slice a string. Negative indices count from the end of the string, with -1 being the last character.

print(
    f"Sliced string (-6:-1): {string_obj[-6:-1]}"
)  # Output: Sliced string (-6:-1): World
print(f"Sliced string (-1:-6): {string_obj[-1:-6]}")  # Output: Sliced string (-1:-6):
print()  # Just to add a newline for better readability of the output

# We can also reverse a string using slicing by specifying a negative step.
print(f"Original string: {string_obj}")  # Output: Original string: Hello, World!
print(f"Reversed string: {string_obj[::-1]}")  # Output: Reversed string: !dlroW ,olleH
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The strip() method is used to remove any leading and trailing whitespace characters from a string. It does not modify the original string but returns a new string with the whitespace removed.

string_with_whitespace = "   Hello, World!   "
print(
    f"Original string: '{string_with_whitespace}'"
)  # Output: Original string: '   Hello, World!   '
stripped_string = string_with_whitespace.strip()
print(
    f"Stripped string: '{stripped_string}'"
)  # Output: Stripped string: 'Hello, World!'
print()  # Just to add a newline for better readability of the output

# The lstrip() method is used to remove any leading whitespace characters from a string, while the rstrip() method is used to remove any trailing whitespace characters.

print(
    f"Original string: '{string_with_whitespace}'"
)  # Output: Original string: '   Hello, World!   '
print(
    f"Left stripped string: '{string_with_whitespace.lstrip()}'"
)  # Output: Left stripped string: 'Hello, World!   '
print(
    f"Right stripped string: '{string_with_whitespace.rstrip()}'"
)  # Output: Right stripped string: '   Hello, World!'
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The split() method is used to split a string into a list of substrings based on a specified delimiter. By default, the delimiter is any whitespace character (space, tab, newline, etc.). The split() method returns a list of substrings.

string_to_split = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{string_to_split}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
split_string = string_to_split.split()
print(
    f"Split string (default delimiter): {split_string}"
)  # Output: Split string (default delimiter): ['Hello,', 'World!', 'Welcome', 'to', 'Python', 'programming.']

# We can also specify a custom delimiter to split the string. For example, if we want to split the string based on commas, we can do so by passing ',' as an argument to the split() method.

string_to_split = "Hello,World!,Welcome,To,Python,Programming"
split_string_comma = string_to_split.split(",")
print(
    f"Split string (comma delimiter): {split_string_comma}"
)  # Output: Split string (comma delimiter): ['Hello', 'World!', 'Welcome', 'To', 'Python', 'Programming']

# We can also specify a maximum number of splits by passing an additional argument to the split() method. For example, if we want to split the string into a maximum of 3 parts, we can do so by passing 3 as the second argument.

string_to_split = "Hello, World! Welcome to Python programming."
split_string_max = string_to_split.split(" ", 3)
print(
    f"Split string (space delimiter, max splits=3): {split_string_max}"
)  # Output: Split string (space delimiter, max splits=3): ['Hello,', 'World!', 'Welcome', 'to Python programming.']

# We can also use the rsplit() method to split a string from the right side. This method works similarly to split(), but it starts splitting from the end of the string.

string_to_split = "Hello, World! Welcome to Python programming."
split_string_rmax = string_to_split.rsplit(" ", 3)
print(
    f"Split string (space delimiter, max splits=3 from the right): {split_string_rmax}"
)  # Output: Split string (space delimiter, max splits=3 from the right): ['Hello, World! Welcome', 'to', 'Python', 'programming.']

# We can also use the splitlines() method to split a string into a list of lines based on the newline character. This method is useful when we want to process multi-line strings.

multi_line_string = """Hello, World!
Welcome to Python programming."""
split_lines = multi_line_string.splitlines()
print(
    f"Original multi-line string: '{multi_line_string}'"
)  # Output: Original multi-line string: 'Hello, World!
# Welcome to Python programming.'
print(
    f"Split lines: {split_lines}"
)  # Output: Split lines: ['Hello, World!', 'Welcome to Python programming.']
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The join() method is used to concatenate a list of strings into a single string, with a specified separator between each string. The syntax for the join() method is: separator.join(iterable), where 'separator' is the string that will be inserted between each element of the iterable (which can be a list, tuple, or any other iterable containing strings).

string_list = ["Hello", "World", "Welcome", "to", "Python", "programming"]
separator = " "
joined_string = separator.join(string_list)
print(
    f"Original list of strings: {string_list}"
)  # Output: Original list of strings: ['Hello', 'World', 'Welcome', 'to', 'Python', 'programming']
print(
    f"Joined string with space separator: '{joined_string}'"
)  # Output: Joined string with space separator: 'Hello World Welcome to Python programming'

# We can also use a different separator, such as a comma, to join the strings.

separator_comma = ", "
joined_string_comma = separator_comma.join(string_list)
print(
    f"Joined string with comma separator: '{joined_string_comma}'"
)  # Output: Joined string with comma separator: 'Hello, World, Welcome, to, Python, programming'

# We can also use an empty string as a separator to concatenate the strings without any space between them.

separator_empty = ""
joined_string_empty = separator_empty.join(string_list)
print(
    f"Joined string with empty separator: '{joined_string_empty}'"
)  # Output: Joined string with empty separator: 'HelloWorldWelcometoPythonprogramming'

# We can also use the join() method to join a list of strings with a newline character as the separator, which is useful for creating multi-line strings.

separator_newline = "\n"
joined_string_newline = separator_newline.join(string_list)
print(
    f"Joined string with newline separator:\n{joined_string_newline}"
)  # Output: Joined string with newline separator:
# Hello
# World
# Welcome
# to
# Python
# programming
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The replace() method is used to replace occurrences of a specified substring with another substring in a string. The syntax for the replace() method is: string.replace(old, new, count), where 'old' is the substring to be replaced, 'new' is the substring to replace with, and 'count' is an optional parameter that specifies the maximum number of occurrences to replace. If 'count' is not provided, all occurrences of the 'old' substring will be replaced. We need to note that the replace() method does not modify the original string but returns a new string with the replacements made as string objects are immutable.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
replaced_string = original_string.replace("Python", "Java")
print(
    f"String after replacement: '{replaced_string}'"
)  # Output: String after replacement: 'Hello, World! Welcome to Java programming.'

# We can also specify the 'count' parameter to limit the number of replacements. For example, if we want to replace only the first occurrence of "o" with "0", we can do so by passing 1 as the third argument.

limited_replacement = original_string.replace("o", "0", 1)
print(
    f"String after limited replacement: '{limited_replacement}'"
)  # Output: String after limited replacement: 'Hell0, World! Welcome to Python programming.'

# We can also use the replace() method to remove a substring by replacing it with an empty string. For example, if we want to remove all occurrences of "o" from the original string, we can do so by replacing "o" with "".

removed_substring = original_string.replace("o", "")
print(
    f"String after removing 'o': '{removed_substring}'"
)  # Output: String after removing 'o': 'Hell, Wrld! Welcme t Pythn prgramming.'

# We can also use the replace() method to replace multiple occurrences of a substring by chaining multiple replace() calls. For example, if we want to replace "o" with "0" and "l" with "1", we can do so by chaining the replace() calls.

chained_replacement = original_string.replace("o", "0").replace("l", "1")
print(
    f"String after chained replacement: '{chained_replacement}'"
)  # Output: String after chained replacement: 'He110, W0r1d! We1c0me t0 Pyth0n prgramming.'
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The count() method is used to count the number of occurrences of a specified substring in a string. The syntax for the count() method is: string.count(substring, start, end), where 'substring' is the string to be counted, 'start' is an optional parameter that specifies the starting index for the search, and 'end' is an optional parameter that specifies the ending index for the search. If 'start' and 'end' are not provided, the count() method will count all occurrences of the substring in the entire string.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
count_o = original_string.count("o")
print(
    f"Number of occurrences of 'o': {count_o}"
)  # Output: Number of occurrences of 'o': 4

# We can also specify the 'start' and 'end' parameters to count occurrences within a specific range of the string. For example, if we want to count the occurrences of "o" between index 0 and 20, we can do so by passing 0 and 20 as the second and third arguments.

count_o_range = original_string.count("o", 0, 20)
print(
    f"Number of occurrences of 'o' between index 0 and 20: {count_o_range}"
)  # Output: Number of occurrences of 'o' between index 0 and 20: 3

# If the substring we are counting does not exist in the string, the count() method will return 0.

count_z = original_string.count("z")
print(
    f"Number of occurrences of 'z': {count_z}"
)  # Output: Number of occurrences of 'z': 0

# We can also use the count() method to count occurrences of a substring that is more than one character long. For example, if we want to count the occurrences of "Python" in the original string, we can do so by passing "Python" as the argument.

count_python = original_string.count("Python")
print(
    f"Number of occurrences of 'Python': {count_python}"
)  # Output: Number of occurrences of 'Python': 1
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The startswith() and endswith() methods are used to check if a string starts with or ends with a specified substring, respectively. The syntax for these methods is: string.startswith(substring, start, end) and string.endswith(substring, start, end), where 'substring' is the string to be checked, 'start' is an optional parameter that specifies the starting index for the search, and 'end' is an optional parameter that specifies the ending index for the search. If 'start' and 'end' are not provided, the methods will check the entire string.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
starts_with_hello = original_string.startswith("Hello")
print(
    f"Does the string start with 'Hello'? {starts_with_hello}"
)  # Output: Does the string start with 'Hello'? True
ends_with_programming = original_string.endswith("programming.")
print(
    f"Does the string end with 'programming.'? {ends_with_programming}"
)  # Output: Does the string end with 'programming.'? True

# We can also specify the 'start' and 'end' parameters to check for the substring within a specific range of the string. For example, if we want to check if the substring "World" starts at index 7, we can do so by passing 7 as the second argument.

starts_with_world = original_string.startswith("World", 7)
print(
    f"Does the substring 'World' start at index 7? {starts_with_world}"
)  # Output: Does the substring 'World' start at index 7? True
ends_with_welcome = original_string.endswith("Welcome", 0, 25)
print(
    f"Does the substring 'Welcome' end between index 0 and 25? {ends_with_welcome}"
)  # Output: Does the substring 'Welcome' end between index 0 and 25? True

# If the substring we are checking for does not exist in the string, both methods will return False.

starts_with_python = original_string.startswith("Python")
print(
    f"Does the string start with 'Python'? {starts_with_python}"
)  # Output: Does the string start with 'Python'? False
ends_with_java = original_string.endswith("Java")
print(
    f"Does the string end with 'Java'? {ends_with_java}"
)  # Output: Does the string end with 'Java'? False

# We can also use the startswith() and endswith() methods to check for substrings that are more than one character long. For example, if we want to check if the string starts with "Hello, World", we can do so by passing "Hello, World" as the argument.

starts_with_hello_world = original_string.startswith("Hello, World")
print(
    f"Does the string start with 'Hello, World'? {starts_with_hello_world}"
)  # Output: Does the string start with 'Hello, World'? True
ends_with_welcome_to_python = original_string.endswith("Welcome to Python programming.")
print(
    f"Does the string end with 'Welcome to Python programming.'? {ends_with_welcome_to_python}"
)  # Output: Does the string end with 'Welcome to Python programming.' True
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The capitalize() method is used to convert the first character of a string to uppercase and the rest of the characters to lowercase. The syntax for the capitalize() method is: string.capitalize(). This method does not modify the original string but returns a new string with the first character capitalized.

original_string = "hello, world! welcome to python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'hello, world! welcome to python programming.'
capitalized_string = original_string.capitalize()
print(
    f"Capitalized string: '{capitalized_string}'"
)  # Output: Capitalized string: 'Hello, world! welcome to python programming.'

# We can also use the capitalize() method on a string that already has some uppercase characters. For example, if we have a string "hELLO, wORLD!", the capitalize() method will convert it to "Hello, world!".

mixed_case_string = "hELLO, wORLD!"
capitalized_mixed_case = mixed_case_string.capitalize()
print(
    f"Original mixed case string: '{mixed_case_string}'"
)  # Output: Original mixed case string: 'hELLO, wORLD!'
print(
    f"Capitalized mixed case string: '{capitalized_mixed_case}'"
)  # Output: Capitalized mixed case string: 'Hello, world!'

# We can also use the capitalize() method on a string that is already capitalized. In this case, the method will return the same string without any changes.

already_capitalized_string = "Hello, World!"
capitalized_already = already_capitalized_string.capitalize()
print(
    f"Original already capitalized string: '{already_capitalized_string}'"
)  # Output: Original already capitalized string: 'Hello, World!'
print(
    f"Capitalized already capitalized string: '{capitalized_already}'"
)  # Output: Capitalized already capitalized string: 'Hello, World!'

# We can also use the capitalize() method on an empty string. In this case, the method will return an empty string.

empty_string = ""
capitalized_empty = empty_string.capitalize()
print(f"Original empty string: '{empty_string}'")  # Output: Original empty string: ''
print(
    f"Capitalized empty string: '{capitalized_empty}'"
)  # Output: Capitalized empty string: ''
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The title() method is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. The syntax for the title() method is: string.title(). This method does not modify the original string but returns a new string with each word capitalized.

original_string = "hello, world! welcome to python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'hello, world! welcome to python programming.'
title_string = original_string.title()
print(
    f"Title case string: '{title_string}'"
)  # Output: Title case string: 'Hello, World! Welcome To Python Programming.'

# We can also use the title() method on a string that already has some uppercase characters. For example, if we have a string "hELLO, wORLD!", the title() method will convert it to "Hello, World!".

mixed_case_string = "hELLO, wORLD!"
title_mixed_case = mixed_case_string.title()
print(
    f"Original mixed case string: '{mixed_case_string}'"
)  # Output: Original mixed case string: 'hELLO, wORLD!'
print(
    f"Title case mixed case string: '{title_mixed_case}'"
)  # Output: Title case mixed case string: 'Hello, World!'

# We can also use the title() method on a string that is already in title case. In this case, the method will return the same string without any changes.

already_title_string = "Hello, World!"
title_already = already_title_string.title()
print(
    f"Original already title case string: '{already_title_string}'"
)  # Output: Original already title case string: 'Hello, World!'
print(
    f"Title case already title case string: '{title_already}'"
)  # Output: Title case already title case string: 'Hello, World!'

# We can also use the title() method on an empty string. In this case, the method will return an empty string.

empty_string = ""
title_empty = empty_string.title()
print(f"Original empty string: '{empty_string}'")  # Output: Original empty string: ''
print(
    f"Title case empty string: '{title_empty}'"
)  # Output: Title case empty string: ''
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The upper() and lower() methods are used to convert all characters in a string to uppercase or lowercase, respectively. The syntax for these methods is: string.upper() and string.lower(). These methods do not modify the original string but return a new string with the characters converted to the specified case.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
upper_string = original_string.upper()
print(
    f"Uppercase string: '{upper_string}'"
)  # Output: Uppercase string: 'HELLO, WORLD! WELCOME TO PYTHON PROGRAMMING.'
lower_string = original_string.lower()
print(
    f"Lowercase string: '{lower_string}'"
)  # Output: Lowercase string: 'hello, world! welcome to python programming.'

# We can also use the upper() and lower() methods on a string that is already in uppercase or lowercase. In this case, the methods will return the same string without any changes.

already_upper_string = "HELLO, WORLD!"
upper_already = already_upper_string.upper()
print(
    f"Original already uppercase string: '{already_upper_string}'"
)  # Output: Original already uppercase string: 'HELLO, WORLD!'
print(
    f"Uppercase already uppercase string: '{upper_already}'"
)  # Output: Uppercase already uppercase string: 'HELLO, WORLD!'

already_lower_string = "hello, world!"
lower_already = already_lower_string.lower()
print(
    f"Original already lowercase string: '{already_lower_string}'"
)  # Output: Original already lowercase string: 'hello, world!'
print(
    f"Lowercase already lowercase string: '{lower_already}'"
)  # Output: Lowercase already lowercase string: 'hello, world!'

# We can also use the upper() and lower() methods on an empty string. In this case, the methods will return an empty string.

empty_string = ""
upper_empty = empty_string.upper()
lower_empty = empty_string.lower()
print(f"Original empty string: '{empty_string}'")  # Output: Original empty string: ''
print(f"Uppercase empty string: '{upper_empty}'")  # Output: Uppercase empty string: ''
print(f"Lowercase empty string: '{lower_empty}'")  # Output: Lowercase empty string: ''
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The find() method is used to find the index of the first occurrence of a specified substring in a string. The syntax for the find() method is: string.find(substring, start, end), where 'substring' is the string to be searched for, 'start' is an optional parameter that specifies the starting index for the search, and 'end' is an optional parameter that specifies the ending index for the search. If 'start' and 'end' are not provided, the find() method will search for the substring in the entire string. If the substring is found, the method returns the index of its first occurrence; otherwise, it returns -1.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
index_world = original_string.find("World")
print(f"Index of 'World': {index_world}")  # Output: Index of 'World': 7

# We can also specify the 'start' and 'end' parameters to search for the substring within a specific range of the string. For example, if we want to find the index of "o" between index 0 and 20, we can do so by passing 0 and 20 as the second and third arguments.

index_o_range = original_string.find("o", 0, 20)
print(
    f"Index of 'o' between index 0 and 20: {index_o_range}"
)  # Output: Index of 'o' between index 0 and 20: 4

# If the substring we are searching for does not exist in the string, the find() method will return -1.

index_z = original_string.find("z")
print(f"Index of 'z': {index_z}")  # Output: Index of 'z': -1

# We can also use the find() method to search for a substring that is more than one character long. For example, if we want to find the index of "Python" in the original string, we can do so by passing "Python" as the argument.

index_python = original_string.find("Python")
print(f"Index of 'Python': {index_python}")  # Output: Index of 'Python': 31

# We can also use the find() method to search for a substring that appears multiple times in the string. In this case, the method will return the index of the first occurrence of the substring. For example, if we want to find the index of "o" in the original string, it will return the index of the first "o" that appears in the string. If we want to find the index of the next occurrence of "o", we can use the index returned by the first find() call as the starting index for the next search.

index_o_first = original_string.find("o")
print(f"Index of first 'o': {index_o_first}")  # Output: Index of first 'o': 4
index_o_second = original_string.find("o", index_o_first + 1)
print(f"Index of second 'o': {index_o_second}")  # Output: Index of second 'o': 8
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The rfind() method is used to find the index of the last occurrence of a specified substring in a string. The syntax for the rfind() method is: string.rfind(substring, start, end), where 'substring' is the string to be searched for, 'start' is an optional parameter that specifies the starting index for the search, and 'end' is an optional parameter that specifies the ending index for the search. If 'start' and 'end' are not provided, the rfind() method will search for the substring in the entire string. If the substring is found, the method returns the index of its last occurrence; otherwise, it returns -1.

original_string = "Hello, World! Welcome to Python programming."
print(
    f"Original string: '{original_string}'"
)  # Output: Original string: 'Hello, World! Welcome to Python programming.'
index_o_last = original_string.rfind("o")
print(f"Index of last 'o': {index_o_last}")  # Output: Index of last 'o': 38

# We can also specify the 'start' and 'end' parameters to search for the substring within a specific range of the string. For example, if we want to find the index of "o" between index 0 and 20, we can do so by passing 0 and 20 as the second and third arguments.

index_o_last_range = original_string.rfind("o", 0, 20)
print(
    f"Index of last 'o' between index 0 and 20: {index_o_last_range}"
)  # Output: Index of last 'o' between index 0 and 20: 8

# If the substring we are searching for does not exist in the string, the rfind() method will return -1.

index_z_last = original_string.rfind("z")
print(f"Index of last 'z': {index_z_last}")  # Output: Index of last 'z': -1

# We can also use the rfind() method to search for a substring that is more than one character long. For example, if we want to find the index of "Python" in the original string, we can do so by passing "Python" as the argument.

index_python_last = original_string.rfind("Python")
print(
    f"Index of last 'Python': {index_python_last}"
)  # Output: Index of last 'Python': 31

# We can also use the rfind() method to search for a substring that appears multiple times in the string. In this case, the method will return the index of the last occurrence of the substring. For example, if we want to find the index of "o" in the original string, it will return the index of the last "o" that appears in the string. If we want to find the index of the previous occurrence of "o", we can use the index returned by the first rfind() call as the ending index for the next search.

index_o_last = original_string.rfind("o")
print(f"Index of last 'o': {index_o_last}")  # Output: Index of last 'o': 38
index_o_previous = original_string.rfind("o", 0, index_o_last)
print(f"Index of previous 'o': {index_o_previous}")  # Output: Index of previous 'o': 8
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# Escape characters are special characters that are used to represent certain whitespace characters or to include special characters in a string. In Python, escape characters are represented by a backslash (\) followed by a specific character. Some common escape characters include:
# - \n: Represents a newline character, which creates a new line in the string.
# - \t: Represents a tab character, which creates a horizontal tab in the string.
# - \\: Represents a backslash character, which allows us to include a literal backslash in the string.
# - \': Represents a single quote character, which allows us to include a literal single quote in the string.
# - \": Represents a double quote character, which allows us to include a literal double quote in the string.
# - \r: Represents a carriage return character, which moves the cursor to the beginning of the line.
# - \b: Represents a backspace character, which deletes the previous character in the string.
# - \f: Represents a form feed character, which creates a new page in the string.
# - \v: Represents a vertical tab character, which creates a vertical tab in the string.
# - \0: Represents a null character, which is used to indicate the end of a string in some programming languages.

# We can use escape characters in strings to include special characters or to format the string in a specific way. For example, if we want to include a newline character in a string, we can use the \n escape character.

string_with_newline = "Hello, World!\nWelcome to Python programming."
print(f"String with newline:\n{string_with_newline}")
# Output:
# String with newline:
# Hello, World!
# Welcome to Python programming.

# We can also use the \t escape character to include a tab character in a string.

string_with_tab = "Hello,\tWorld!\tWelcome to Python programming."
print(f"String with tab:\n{string_with_tab}")
# Output:
# String with tab:
# Hello,	World!	Welcome to Python programming.

# We can use the \\ escape character to include a literal backslash in a string.

string_with_backslash = "This is a backslash: \\"
print(f"String with backslash:\n{string_with_backslash}")
# Output:
# String with backslash:
# This is a backslash: \

# We can use the \' escape character to include a literal single quote in a string.

string_with_single_quote = "It's a nice day!"
print(f"String with single quote:\n{string_with_single_quote}")
# Output:
# String with single quote:
# It's a nice day!

# We can use the \" escape character to include a literal double quote in a string.

string_with_double_quote = 'She said, "Hello!"'
print(f"String with double quote:\n{string_with_double_quote}")
# Output:
# String with double quote:
# She said, "Hello!"

# We can also use multiple escape characters in a single string to format it in a specific way. For example, if we want to include both a newline and a tab character in a string, we can do so by using both escape characters.

string_with_newline_and_tab = "Hello,\n\tWorld!\n\tWelcome to Python programming."
print(f"String with newline and tab:\n{string_with_newline_and_tab}")
# Output:
# String with newline and tab:
# Hello,
# 	World!
# 	Welcome to Python programming.

# We can use raw strings to avoid the need for escape characters. A raw string is defined by prefixing the string literal with 'r' or 'R'. In a raw string, backslashes are treated as literal characters and do not have any special meaning.

raw_string = r"This is a raw string with a backslash: \n and a tab: \t"
print(f"Raw string:\n{raw_string}")
# Output:
# Raw string:
# This is a raw string with a backslash: \n and a tab: \t
print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------

# The format() method is used to format strings by replacing placeholders in the string with specified values. The syntax for the format() method is: string.format(value1, value2, ...), where 'string' is the string containing placeholders, and 'value1', 'value2', etc. are the values that will replace the placeholders in the string. Placeholders in the string are represented by curly braces {}. The format() method returns a new string with the placeholders replaced by the specified values.

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(f"Formatted string: '{formatted_string}'")
# Output: Formatted string: 'My name is Alice and I am 30 years old.'

# We can also use positional arguments in the format() method to specify the order of the values that will replace the placeholders. For example, if we want to reverse the order of the name and age in the formatted string, we can do so by using positional arguments.

formatted_string_positional = "My name is {1} and I am {0} years old.".format(age, name)
print(f"Formatted string with positional arguments: '{formatted_string_positional}'")
# Output: Formatted string with positional arguments: 'My name is Alice and I am 30 years old.'

# We can also use keyword arguments in the format() method to specify the values that will replace the placeholders by using their names. For example, if we want to use keyword arguments for the name and age, we can do so by passing them as keyword arguments to the format() method.

formatted_string_keyword = "My name is {name} and I am {age} years old.".format(
    name=name, age=age
)
print(f"Formatted string with keyword arguments: '{formatted_string_keyword}'")
# Output: Formatted string with keyword arguments: 'My name is Alice and I am 30 years old.'

# We can also use the format() method to format numbers in a specific way. For example, if we want to format a floating-point number to two decimal places, we can do so by using the format specifier {:.2f}.

pi = 3.14159
formatted_pi = "The value of pi is approximately {:.2f}.".format(pi)
print(f"Formatted pi: '{formatted_pi}'")
# Output: Formatted pi: 'The value of pi is approximately 3.14.'

# We can also use the format() method to format numbers with a specific width. For example, if we want to format a number to be right-aligned within a width of 10 characters, we can do so by using the format specifier {:>10}.

number = 42
formatted_number = "The number is {:>10}.".format(number)
print(f"Formatted number with width: '{formatted_number}'")
# Output: Formatted number with width: 'The number is         42.'

# We can also use the format() method to format numbers with leading zeros. For example, if we want to format a number to be zero-padded to a width of 5 characters, we can do so by using the format specifier {:0>5}.

number = 42
formatted_number_zero_padded = "The number is {:0>5}.".format(number)
print(f"Formatted number with leading zeros: '{formatted_number_zero_padded}'")
# Output: Formatted number with leading zeros: 'The number is 00042.'

# We can also use the format() method to format numbers with a specific sign. For example, if we want to format a number to always show the sign, we can do so by using the format specifier {:+}.

positive_number = 42
negative_number = -42
formatted_positive = "The positive number is {:+}.".format(positive_number)
formatted_negative = "The negative number is {:+}.".format(negative_number)
print(f"Formatted positive number: '{formatted_positive}'")
print(f"Formatted negative number: '{formatted_negative}'")
# Output:
# Formatted positive number: 'The positive number is +42.'
# Formatted negative number: 'The negative number is -42.'

# We can also use the format() method to format numbers with a specific type. For example, if we want to format a number as a percentage, we can do so by using the format specifier {:.2%}.

percentage = 0.75
formatted_percentage = "The percentage is {:.2%}.".format(percentage)
print(f"Formatted percentage: '{formatted_percentage}'")
# Output: Formatted percentage: 'The percentage is 75.00%.'
print()  # Just to add a newline for better readability of the output

# Even though the format() method is very powerful and flexible, it can be a bit verbose for simple string formatting tasks. In Python 3.6 and later, we can use f-strings (formatted string literals) as a more concise and readable way to format strings. F-strings allow us to embed expressions directly within string literals by prefixing the string with 'f' or 'F' and using curly braces {} to enclose the expressions. But, still the areas where the format() method is more suitable than f-strings include:

# 1. When we need to format a string that is defined in a different part of the code, such as a string that is stored in a variable or a string that is returned by a function. In this case, using the format() method allows us to format the string without having to define it as an f-string at the point of use.

string_stored_in_variable = "My name is {} and I am {} years old."
formatted_string_from_variable = string_stored_in_variable.format(name, age)
print(f"Formatted string from variable: '{formatted_string_from_variable}'")
# Output: Formatted string from variable: 'My name is Alice and I am 30 years old.'

# 2. When we need to format a string that contains curly braces {} as part of the string itself. In this case, using the format() method allows us to include literal curly braces in the string by escaping them with double curly braces {{}}. With f-strings, we would need to use a different approach to include literal curly braces, such as using a backslash to escape them, which can be less readable.

string_with_curly_braces = "This string contains curly braces: {{}}"
formatted_string_with_curly_braces = string_with_curly_braces.format()
print(f"Formatted string with curly braces: '{formatted_string_with_curly_braces}'")
# Output: Formatted string with curly braces: 'This string contains curly braces: {}'

# 3. When we need to format a string that is used in a context where f-strings are not supported, such as in older versions of Python or in certain libraries or frameworks that do not support f-strings. In this case, using the format() method allows us to ensure compatibility with those contexts while still being able to format our strings effectively.

# In general, while f-strings are often more concise and easier to read for simple string formatting tasks, the format() method can still be a valuable tool for more complex formatting scenarios or when compatibility with older Python versions is a concern.

print()  # Just to add a newline for better readability of the output

# ----------------------------------------------------------------------------------------------------------------------------------------
