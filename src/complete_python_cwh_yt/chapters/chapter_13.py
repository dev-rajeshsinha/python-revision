# ----------------------------------------------------------------------------------------------------------------------------------------------

# Virtual Environments in Python is a tool to create isolated Python environments. It allows us to manage dependencies for different projects separately, ensuring that each project has its own set of libraries and packages without interfering with others. This is particularly useful when working on multiple projects that require different versions of the same library or when we want to avoid conflicts between global and project-specific dependencies.

# To create a virtual environment in Python, we can use the built-in `venv` module. Here are the steps to create and activate a virtual environment:

# 1. Open a terminal or command prompt.
# 2. Navigate to the directory where we want to create our project.
# 3. Run the following command to create a virtual environment named `venv`:
#    ```
#    python -m venv venv
#    ```
# 4. Activate the virtual environment:
#    - On Windows:
#      ```
#      venv\Scripts\activate
#      ```
#    - On macOS and Linux:
#      ```
#      source venv/bin/activate
#      ```
# 5. Once the virtual environment is activated, we can install packages using `pip` without affecting the global Python installation. For example:
#    ```
#    pip install requests
#    ```
# 6. To deactivate the virtual environment, simply run:
#    ```
#    deactivate
#    ```
# 7. To remove the virtual environment, we can delete the `venv` directory.
#
# Note: At step 3, we can choose any name for our virtual environment instead of `venv`. It's a common convention to use `venv`, but we can name it according to our project or preference. For example, if our project is named `my_project`, we could create the virtual environment with:
#    ```
#    python -m venv my_project_env
#    ```
# This would create a virtual environment named `my_project_env` instead of `venv`. The name of the virtual environment is flexible and can be chosen based on the project's needs or personal preference.
#
# Note: It's important to remember that when we activate a virtual environment, the command prompt will typically change to indicate that we are now working within that environment. This helps us keep track of which environment we are currently using. Additionally, when we install packages while the virtual environment is activated, those packages will only be available within that environment and will not affect other projects or the global Python installation. This isolation is one of the key benefits of using virtual environments in Python. It is often recommended to include a `requirements.txt` file in our project, which lists all the dependencies needed for the project. This allows other developers to easily set up the same environment by running:
#    ```
#    pip install -r requirements.txt
#    ```
#
# To create a `requirements.txt` file, we can use the following command while the virtual environment is activated:
#    ```
#    pip freeze > requirements.txt
#    ```
# This command will generate a `requirements.txt` file that contains a list of all the packages and their versions that are currently installed in the virtual environment. This file can then be shared with others or used to recreate the same environment on another machine by running the `pip install -r requirements.txt` command. This is a common practice in Python projects to ensure that all developers are working with the same dependencies and to make it easier to manage and share project requirements.

# ----------------------------------------------------------------------------------------------------------------------------------------------

# Lambda functions in Python are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not intended to be reused elsewhere in the code.
#
# The syntax for a lambda function is as follows:
# lambda arguments: expression

# Below is an example of a lambda function that takes two arguments and returns their sum:

add = lambda x, y: x + y

# In this example, `add` is a lambda function that takes two arguments `x` and `y`, and returns their sum. We can use this function like any other function:

result = add(5, 3)
print(result)  # Output: 8
print(type(add))  # Output: <class 'function'>
print()  # Just to add a newline for better readability

# Lambda functions can also be used with higher-order functions like `map`, `filter`, and `reduce` to perform operations on collections of data.

# Below is an example of using a lambda function with `map` to square each number in a list:

numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]
print()  # Just to add a newline for better readability

# Below is another example of a lambda function that calculate sum of the even numbers in a list:

even_sum = sum(filter(lambda x: x % 2 == 0, numbers))
print(even_sum)  # Output: 12
print()  # Just to add a newline for better readability

# Below is an example of a lambda function that uses `reduce` to calculate the product of all numbers in a list:

from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 720
print()  # Just to add a newline for better readability

# In the above example, we import the `reduce` function from the `functools` module and use a lambda function to multiply all the numbers in the list together. The `reduce` function applies the lambda function cumulatively to the items of the list, resulting in a single value that is the product of all the numbers.

# We can also create lambda functions that take no arguments.

# Below is an example of a lambda function that takes no arguments and returns a string:

greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!
print()  # Just to add a newline for better readability

# It is also possible to create lambda functions that take variable-length arguments using `*args` and `**kwargs`.

# Below is an example of a lambda function that takes variable-length arguments and returns their sum:

sum_all = lambda *args: sum(args)
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print()  # Just to add a newline for better readability

# Below is an example of a lambda function that takes variable-length keyword arguments and returns a cumulative product of the values:

product_all = lambda *args: reduce(lambda x, y: x * y, args)
print(product_all(1, 2, 3, 4, 5))  # Output: 120
print()  # Just to add a newline for better readability

# Lambda functions can be even more complex, allowing for multiple operations within a single expression using conditional statements. However, it's important to keep in mind that lambda functions are meant for simple operations. If a function becomes too complex, it is generally better to define a regular function using the `def` keyword for better readability and maintainability.

# ----------------------------------------------------------------------------------------------------------------------------------------------
