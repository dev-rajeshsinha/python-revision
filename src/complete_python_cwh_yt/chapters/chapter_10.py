# -------------------------------------------------------------------------------------------------------------------------------------------

# Object Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes to structure code. It allows for better organization, reusability, and modularity. In OOP, we can create classes that define the properties (attributes) and behaviors (methods) of objects. We can then create instances of these classes, which are individual objects that can have their own unique data.

# Here are some key concepts of OOP in Python:
# 1. Class: A blueprint for creating objects. It defines the attributes and methods that the objects created from the class will have.
# 2. Object: An instance of a class. It is a specific realization of the class with its own unique data.
# 3. Inheritance: A mechanism that allows a new class (child class) to inherit properties and behaviors from an existing class (parent class).
# 4. Encapsulation: The bundling of data (attributes) and methods that operate on the data into a single unit (class). It also restricts direct access to some of the object's components, which can help prevent accidental modification of data.
# 5. Polymorphism: The ability of different classes to be treated as instances of the same class through inheritance. It allows for methods to be used in different ways based on the object that is calling them.

# -------------------------------------------------------------------------------------------------------------------------------------------

# To define a class in Python, we use the `class` keyword followed by the class name and a colon. Inside the class, we can define attributes and methods. The `__init__` method is a special method that is called when an object is created from the class. It is used to initialize the attributes of the object.


class Person:
    """This class represents a person with a name and age."""

    def __init__(self, name, age):
        """Initialize the attributes of the person."""
        self.name = name  # Attribute to store the name of the person
        self.age = age  # Attribute to store the age of the person

    def greet(self):
        """Method to return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# We can create an instance of the `Person` class and call its method:

person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# We can also create another instance of the `Person` class:

person2 = Person("Bob", 25)
print(person2.greet())  # Output: Hello, my name is Bob and I am 25 years old.

print(
    f"Is person1 an instance of Person? {isinstance(person1, Person)}"
)  # Output: True
print(
    f"Is person2 an instance of Person? {isinstance(person2, Person)}"
)  # Output: True
print()  # Just to add a newline for better readability of the output

# As visible, we have created two different objects (person1 and person2) from the same class (Person), and each object has its own unique data (name and age). This is one of the key features of OOP, allowing us to create multiple instances of a class with different attributes. We have also defined a method (greet) that can be called on each instance to return a personalized greeting message. This method can be reused across all instances of the class, demonstrating the reusability aspect of OOP.

# A class can also have class variables (class attributes), which are shared among all instances of the class. These variables are defined within the class but outside of any instance methods. They can be accessed using the class name or through an instance.


class Car:
    """This class represents a car with a make, model, and year."""

    # Class variable to keep track of the total number of cars created
    total_cars = 0

    def __init__(self, make, model, year):
        """Initialize the attributes of the car."""
        self.make = make  # Attribute to store the make of the car
        self.model = model  # Attribute to store the model of the car
        self.year = year  # Attribute to store the year of the car
        Car.total_cars += (
            1  # Increment the total number of cars when a new car is created
        )

    def car_info(self):
        """Method to return information about the car."""
        return f"{self.year} {self.make} {self.model}"


# We can create instances of the `Car` class and access the class variable:

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.car_info())  # Output: 2020 Toyota Camry
print(car2.car_info())  # Output: 2019 Honda Civic
print(f"Total cars created: {Car.total_cars}")  # Output: Total cars created: 2

print(f"Is car1 an instance of Car? {isinstance(car1, Car)}")  # Output: True
print(f"Is car2 an instance of Car? {isinstance(car2, Car)}")  # Output: True
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Car` class with a class variable `total_cars` that keeps track of the total number of cars created. Each time a new car is instantiated, the `__init__` method increments this variable. We can access the class variable using the class name `Car.total_cars` to see how many cars have been created. This demonstrates how class variables work in OOP and how they are shared among all instances of the class.

# Along with instance methods, we can also define class methods and static methods in a class. Class methods are defined using the `@classmethod` decorator and take the class itself as the first argument (usually named `cls`). Static methods are defined using the `@staticmethod` decorator and do not take any special first argument.


class MathOperations:
    """This class provides basic math operations."""

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Static method to subtract two numbers."""
        return a - b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers."""
        return a * b

    @classmethod
    def divide(cls, a, b):
        """Class method to divide two numbers."""
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


# We can call the static methods and class methods without creating an instance of the class:

print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.subtract(5, 3))  # Output: 2
print(MathOperations.multiply(5, 3))  # Output: 15
print(MathOperations.divide(5, 3))  # Output: 1.6666666666666667
print(MathOperations.divide(5, 0))  # Output: Cannot divide by zero
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `MathOperations` class with static methods for addition and subtraction, and class methods for multiplication and division. We can call these methods directly on the class without needing to create an instance, demonstrating the use of static and class methods in OOP. Static methods are used for operations that do not require access to any instance or class-specific data, while class methods can access class-level data if needed.

# If we update a class variable, it will affect all instances of the class that share that variable. However, if we update an instance variable, it will only affect that specific instance.


class Student:
    """This class represents a student with a name and grade."""

    school_name = "ABC High School"  # Class variable shared by all instances

    def __init__(self, name, grade):
        """Initialize the attributes of the student."""
        self.name = name  # Instance variable to store the name of the student
        self.grade = grade  # Instance variable to store the grade of the student


# We can create instances of the `Student` class and see how class variables and instance variables work:

student1 = Student("Charlie", "A")
student2 = Student("Diana", "B")

print(
    f"{student1.name} is in {student1.school_name} and has a grade of {student1.grade}."
)
# Output: Charlie is in ABC High School and has a grade of A.
print(
    f"{student2.name} is in {student2.school_name} and has a grade of {student2.grade}."
)
# Output: Diana is in ABC High School and has a grade of B.

# Now, let's update the class variable `school_name` and see how it affects both instances:

Student.school_name = "XYZ High School"

print(
    f"{student1.name} is in {student1.school_name} and has a grade of {student1.grade}."
)
# Output: Charlie is in XYZ High School and has a grade of A.
print(
    f"{student2.name} is in {student2.school_name} and has a grade of {student2.grade}."
)
# Output: Diana is in XYZ High School and has a grade of B.

# Now, let's update the instance variable `grade` for `student1` and see how it affects only that instance:

student1.grade = "A+"

print(
    f"{student1.name} is in {student1.school_name} and has a grade of {student1.grade}."
)
# Output: Charlie is in XYZ High School and has a grade of A+.
print(
    f"{student2.name} is in {student2.school_name} and has a grade of {student2.grade}."
)
# Output: Diana is in XYZ High School and has a grade of B.
print()  # Just to add a newline for better readability of the output

# In this example, we have a `Student` class with a class variable `school_name` that is shared among all instances of the class. When we update the `school_name`, it affects both `student1` and `student2` because they share the same class variable. However, when we update the `grade` for `student1`, it only affects that specific instance, and `student2` remains unchanged. This illustrates the difference between class variables and instance variables in OOP.

# -------------------------------------------------------------------------------------------------------------------------------------------

# @property is a built-in decorator in Python that allows us to define methods in a class that can be accessed like attributes. It is used to create getter, setter, and deleter methods for class attributes, providing a way to control access to the attributes while still allowing them to be accessed as if they were regular attributes.


class Circle:
    """This class represents a circle with a radius."""

    def __init__(self, radius):
        """Initialize the radius of the circle."""
        self._radius = radius  # Use a private variable to store the radius

    @property
    def radius(self):
        """Getter method for the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter method for the radius."""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        """Property to calculate the area of the circle."""
        import math

        return math.pi * (self._radius**2)


# We can create an instance of the `Circle` class and access the properties:

circle = Circle(5)
print(f"Radius of the circle: {circle.radius}")  # Output: Radius of the circle: 5
print(
    f"Area of the circle: {circle.area}"
)  # Output: Area of the circle: 78.53981633974483

# Now, let's update the radius using the setter method and see how it affects the area:

circle.radius = 10
print(
    f"Updated radius of the circle: {circle.radius}"
)  # Output: Updated radius of the circle: 10
print(
    f"Updated area of the circle: {circle.area}"
)  # Output: Updated area of the circle: 314.1592653589793
print()  # Just to add a newline for better readability of the output

# circle.area = 100  # This will raise an error because area is a read-only property

# In this example, we have defined a `Circle` class with a private variable `_radius` to store the radius of the circle. We have used the `@property` decorator to create a getter method for the radius, allowing us to access it as an attribute. We have also created a setter method for the radius that checks if the value is non-negative before updating it. Additionally, we have defined a property for calculating the area of the circle based on its radius. This demonstrates how we can use properties in OOP to control access to attributes while still providing a convenient way to access and modify them. If we try to set the area directly, it will raise an error because it is a read-only property, which is a common use case for properties in OOP.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can also create private attributes and methods in a class by prefixing their names with double underscores (`__`). This is known as name mangling, and it helps to prevent accidental access to these attributes and methods from outside the class. However, it is important to note that this does not make the attributes and methods truly private, as they can still be accessed using a specific naming convention.


class BankAccount:
    """This class represents a bank account with a balance."""

    def __init__(self, initial_balance):
        """Initialize the balance of the bank account."""
        self.__balance = initial_balance  # Private attribute to store the balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError(
                "Withdrawal amount must be positive and less than or equal to the balance"
            )

    def get_balance(self):
        """Method to return the current balance of the account."""
        return self.__balance


# We can create an instance of the `BankAccount` class and perform some operations:

account = BankAccount(1000)
print(f"Initial balance: {account.get_balance()}")  # Output: Initial balance: 1000
account.deposit(500)
print(
    f"Balance after deposit: {account.get_balance()}"
)  # Output: Balance after deposit: 1500
account.withdraw(200)
print(
    f"Balance after withdrawal: {account.get_balance()}"
)  # Output: Balance after withdrawal: 1300

# Now, let's try to access the private attribute directly (this will raise an error):

# print(account.__balance)  # This will raise an AttributeError

# However, we can still access the private attribute using name mangling:

print(account._BankAccount__balance)  # type: ignore # Output: 1300
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `BankAccount` class with a private attribute `__balance` to store the balance of the account. We have provided methods for depositing and withdrawing money, as well as a method to get the current balance. The private attribute cannot be accessed directly from outside the class, but it can still be accessed using name mangling (e.g., `account._BankAccount__balance`). This illustrates how we can use private attributes and methods in OOP to encapsulate data and control access to it, while still allowing for some level of access if needed.

# Sometimes, a single underscore prefix (e.g., `_attribute`) is used to indicate that an attribute or method is intended for internal use within the class or module, but it is not strictly enforced as private. This is a convention in Python to signal that the attribute or method should not be accessed directly from outside the class, but it can still be accessed if necessary.


class Employee:
    """This class represents an employee with a name and salary."""

    def __init__(self, name, salary):
        """Initialize the attributes of the employee."""
        self._name = name  # Single underscore to indicate internal use
        self._salary = salary  # Single underscore to indicate internal use

    def get_employee_info(self):
        """Method to return information about the employee."""
        return f"Employee Name: {self._name}, Salary: {self._salary}"


# We can create an instance of the `Employee` class and access the information:

employee = Employee("Eve", 50000)
print(employee.get_employee_info())  # Output: Employee Name: Eve, Salary: 50000

# Now, let's try to access the attributes directly (this is not recommended, but it is possible):

print(employee._name)  # Output: Eve
print(employee._salary)  # Output: 50000
print()  # Just to add a newline for better readability of the output

# -------------------------------------------------------------------------------------------------------------------------------------------

# Overloading in Python means giving the same operator or function name different behavior based on the type or number of inputs. Python does not support traditional method overloading like some other languages (multiple methods with the same name but different parameter lists). However, we can still achieve overloading behavior in two common ways:
# 1. Operator overloading using special methods such as `__add__`, `__sub__`, etc.
# 2. Flexible method definitions using default arguments, `*args`, or type checks.


class Vector:
    """This class demonstrates operator overloading with vectors."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + to add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector to Vector")

    def __str__(self):
        """Readable string representation of the vector."""
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v1)  # Output: Vector(2, 3)
print(v2)  # Output: Vector(4, 5)
print(v3)  # Output: Vector(6, 8)
print()  # Just to add a newline for better readability of the output


class Calculator:
    """This class demonstrates method overloading-like behavior in Python."""

    def add(self, a, b=0, c=0):
        """Add two or three numbers using default arguments."""
        return a + b + c


calculator = Calculator()

print(calculator.add(5, 10))  # Output: 15
print(calculator.add(5, 10, 20))  # Output: 35
print()  # Just to add a newline for better readability of the output


class FlexibleCalculator:
    """This class demonstrates overloading-like behavior using *args."""

    def add(self, *numbers):
        """Add any number of numeric arguments."""
        if not numbers:
            return 0
        return sum(numbers)


flexible_calculator = FlexibleCalculator()

print(flexible_calculator.add())  # Output: 0
print(flexible_calculator.add(7))  # Output: 7
print(flexible_calculator.add(7, 8, 9, 10))  # Output: 34
print()  # Just to add a newline for better readability of the output

# In this example, `Vector` shows operator overloading by redefining how `+` works for custom objects. The `Calculator` class shows one way to mimic method overloading using default parameters, and `FlexibleCalculator` shows another way using `*args`.

# -------------------------------------------------------------------------------------------------------------------------------------------
