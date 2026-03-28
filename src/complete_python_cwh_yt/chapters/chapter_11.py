# -------------------------------------------------------------------------------------------------------------------------------------------

# Inheritance is a fundamental concept in OOP that allows a new class (child class) to inherit properties and behaviors from an existing class (parent class). This promotes code reusability and establishes a natural hierarchical relationship between classes. The child class can also override methods of the parent class to provide specific implementations.


class Animal:
    """This class represents a generic animal."""

    def __init__(self, name):
        """Initialize the name of the animal."""
        self.name = name

    def speak(self) -> str:
        """Method to be overridden by subclasses to define the sound the animal makes."""
        return "Some animal sound"


class Dog(Animal):
    """This class represents a dog, which is a specific type of animal."""

    def speak(self) -> str:
        """Override the speak method to return the sound a dog makes."""
        return "Woof!"


class Cat(Animal):
    """This class represents a cat, which is a specific type of animal."""

    def speak(self) -> str:
        """Override the speak method to return the sound a cat makes."""
        return "Meow!"


# We can create instances of the Dog and Cat classes and call their speak methods:

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

print(f"Is dog an instance of Animal? {isinstance(dog, Animal)}")  # Output: True
print(f"Is dog an instance of Dog? {isinstance(dog, Dog)}")  # Output: True
print(f"Is cat an instance of Animal? {isinstance(cat, Animal)}")  # Output: True
print(f"Is cat an instance of Cat? {isinstance(cat, Cat)}")  # Output: True
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a parent class `Animal` with a method `speak` that is meant to be overridden by subclasses. The `Dog` and `Cat` classes inherit from the `Animal` class and provide their own implementations of the `speak` method. This demonstrates inheritance in OOP, allowing us to create specific types of animals while still sharing common attributes and behaviors defined in the parent class.

# We can also use the `super()` function to call methods from the parent class within the child class. This is useful when we want to extend the functionality of a method rather than completely overriding it.


class Bird(Animal):
    """This class represents a bird, which is a specific type of animal."""

    def __init__(self, name, can_fly):
        """Initialize the name and flying ability of the bird."""
        super().__init__(name)  # Call the __init__ method of the parent class
        self.can_fly = can_fly  # Attribute to indicate if the bird can fly

    def speak(self) -> str:
        """Override the speak method to return the sound a bird makes."""
        return "Chirp!"

    def fly(self) -> str:
        """Method to indicate if the bird can fly."""
        if self.can_fly:
            return f"{self.name} can fly."
        else:
            return f"{self.name} cannot fly."


# We can create an instance of the Bird class and call its methods:

bird = Bird("Tweety", True)
print(bird.speak())  # Output: Chirp!
print(bird.fly())  # Output: Tweety can fly.

print(f"Is bird an instance of Animal? {isinstance(bird, Animal)}")  # Output: True
print(f"Is bird an instance of Bird? {isinstance(bird, Bird)}")  # Output: True
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Bird` class that inherits from the `Animal` class. We use the `super()` function to call the `__init__` method of the parent class to initialize the `name` attribute, and we also add a new attribute `can_fly` specific to the `Bird` class, which is not available in the `Animal` class or other child classes of `Animal`. The `speak` method is overridden to return a bird-specific sound, and we also define a new method `fly` to indicate whether the bird can fly or not. This demonstrates how we can extend the functionality of a parent class while still maintaining the core attributes and behaviors through inheritance.

# Note that, the Dog and Cat classes did not have their own `__init__` method, so they inherited the `__init__` method from the Animal class directly. The Bird class, however, has its own `__init__` method that calls the parent class's `__init__` method using super() to initialize the `name` attribute, and also initializes its own `can_fly` attribute. This shows how we can use inheritance to create more specific classes while still reusing code from the parent class. Generally, if we are not introducing any new attributes in the child class, we can simply inherit the `__init__` method from the parent class without needing to define it in the child class. However, if we need to add new attributes or perform additional initialization, we can define our own `__init__` method in the child class and call the parent class's `__init__` method using super() to ensure that the inherited attributes are properly initialized.

# Note that, the `isinstance()` function is used to check if an object is an instance of a specific class or a subclass thereof. In the examples above, we used `isinstance()` to verify that the `dog`, `cat`, and `bird` objects are instances of the `Animal` class, which confirms that they have inherited from the `Animal` class. This is a useful way to check the type of an object and ensure that it belongs to a certain class hierarchy in OOP.

# A class can also inherit from multiple parent classes, which is known as multiple inheritance. This allows a child class to inherit attributes and methods from more than one parent class.


class Flyer:
    """This class represents the ability to fly."""

    def fly(self) -> str:
        """Method to indicate flying ability."""
        return "I can fly!"


class Swimmer:
    """This class represents the ability to swim."""

    def swim(self) -> str:
        """Method to indicate swimming ability."""
        return "I can swim!"


class Duck(Animal, Flyer, Swimmer):
    """This class represents a duck, which can fly and swim."""

    def speak(self) -> str:
        """Override the speak method to return the sound a duck makes."""
        return "Quack!"


# We can create an instance of the Duck class and call its methods:

duck = Duck("Daffy")
print(duck.speak())  # Output: Quack!
print(duck.fly())  # Output: I can fly!
print(duck.swim())  # Output: I can swim!

print(f"Is duck an instance of Animal? {isinstance(duck, Animal)}")  # Output: True
print(f"Is duck an instance of Flyer? {isinstance(duck, Flyer)}")  # Output: True
print(f"Is duck an instance of Swimmer? {isinstance(duck, Swimmer)}")  # Output: True
print(f"Is duck an instance of Duck? {isinstance(duck, Duck)}")  # Output: True
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Duck` class that inherits from three parent classes: `Animal`, `Flyer`, and `Swimmer`. The `Duck` class can access the methods from all three parent classes, allowing it to speak, fly, and swim. This demonstrates multiple inheritance in OOP, where a child class can inherit from multiple parent classes to combine their functionalities.

# If there are methods with the same name in multiple parent classes, the method resolution order (MRO) determines which method is called when the child class calls that method. The MRO follows a specific order based on the hierarchy of the classes and the order in which they are defined.


class A:
    def method(self) -> str:
        return "Method from class A"


class B:
    def method(self) -> str:
        return "Method from class B"


class C(A, B):
    pass


c = C()
print(c.method())  # Output: Method from class A
print(
    f"Method Resolution Order (MRO) for class C: {C.mro()}"
)  # Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(
    f"Method Resolution Order (MRO) for class C using __mro__: {C.__mro__}"
)  # Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print()  # Just to add a newline for better readability of the output

# In this example, we have two parent classes `A` and `B`, both of which have a method named `method`. The child class `C` inherits from both `A` and `B`. When we call the `method` on an instance of class `C`, it follows the method resolution order (MRO) and calls the method from class `A` first considering the method is not overridden in class `C`, since `A` is listed before `B` in the inheritance list of class `C`. If the method is not found in class `A`, it will look for the method in class `B`. Also, if the class `C` has its own implementation for the method, it will override the methods from both `A` and `B`, and once called, it will not look further into the parent classes. This demonstrates how Python resolves method calls in the case of multiple inheritance. If the class `C` was defined as `class C(B, A)`, then the method from class `B` would be called instead. The MRO can be checked using the `mro()` method or the `__mro__` attribute of the class.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Apart from Multiple Inheritance, there are also other types of inheritance in OOP, such as:
# 1. Single Inheritance: A child class inherits from a single parent class.
# 2. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class, creating a multi-level hierarchy.
# 3. Hierarchical Inheritance: Multiple child classes inherit from a single parent class, creating a hierarchy of classes.

# Example of Single Inheritance:


class Vehicle:
    """This class represents a generic vehicle."""

    def __init__(self, make, model):
        """Initialize the make and model of the vehicle."""
        self.make = make
        self.model = model

    def start_engine(self) -> str:
        """Method to start the engine."""
        return "Engine started!"


class Car(Vehicle):
    """This class represents a car, which is a specific type of vehicle."""

    def honk(self) -> str:
        """Method to honk the horn."""
        return "Honk! Honk!"


# We can create an instance of the Car class and call its methods:

car = Car("Toyota", "Corolla")
print(f"Is car an instance of Vehicle? {isinstance(car, Vehicle)}")  # Output: True
print(f"Is car an instance of Car? {isinstance(car, Car)}")  # Output: True
print(car.start_engine())  # Output: Engine started!
print(car.honk())  # Output: Honk! Honk!
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Vehicle` class that represents a generic vehicle with attributes for make and model, and a method to start the engine. The `Car` class inherits from the `Vehicle` class and adds its own method to honk the horn. This demonstrates single inheritance in OOP, where the `Car` class is a specific type of `Vehicle` that inherits its properties and behaviors while also adding its own unique functionality.

# Example of Multilevel Inheritance:


class Person:
    """This class represents a generic person."""

    def __init__(self, name):
        """Initialize the name of the person."""
        self.name = name

    def introduce(self) -> str:
        """Method to introduce the person."""
        return f"Hello, my name is {self.name}."


class Employee(Person):
    """This class represents an employee, which is a specific type of person."""

    def __init__(self, name, employee_id):
        """Initialize the name and employee ID of the employee."""
        super().__init__(name)  # Call the __init__ method of the parent class
        self.employee_id = employee_id  # Attribute to store employee ID

    def work(self) -> str:
        """Method to indicate that the employee is working."""
        return f"{self.name} is working."


class Manager(Employee):
    """This class represents a manager, which is a specific type of employee."""

    def manage(self) -> str:
        """Method to indicate that the manager is managing."""
        return f"{self.name} is managing the team."


# We can create an instance of the Manager class and call its methods:

manager = Manager("Alice", "M123")
print(
    f"Is manager an instance of Person? {isinstance(manager, Person)}"
)  # Output: True
print(
    f"Is manager an instance of Employee? {isinstance(manager, Employee)}"
)  # Output: True
print(
    f"Is manager an instance of Manager? {isinstance(manager, Manager)}"
)  # Output: True
print(manager.introduce())  # Output: Hello, my name is Alice.
print(manager.work())  # Output: Alice is working.
print(manager.manage())  # Output: Alice is managing the team.
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Person` class that represents a generic person with a name and a method to introduce themselves. The `Employee` class inherits from the `Person` class and adds an employee ID attribute and a method to indicate that the employee is working. The `Manager` class inherits from the `Employee` class and adds a method to indicate that the manager is managing the team. This demonstrates multilevel inheritance in OOP, where the `Manager` class is a specific type of `Employee`, which in turn is a specific type of `Person`, creating a multi-level hierarchy of classes.

# Example of Hierarchical Inheritance:


class Shape:
    """This class represents a generic shape."""

    def area(self) -> str:
        """Method to calculate the area of the shape."""
        return "Area of the shape"


class Circle(Shape):
    """This class represents a circle, which is a specific type of shape."""

    def area(self) -> str:
        """Override the area method to calculate the area of a circle."""
        return "Area of the circle"


class Square(Shape):
    """This class represents a square, which is a specific type of shape."""

    def area(self) -> str:
        """Override the area method to calculate the area of a square."""
        return "Area of the square"


# We can create instances of the Circle and Square classes and call their area methods:

circle = Circle()
square = Square()

print(f"Is circle an instance of Shape? {isinstance(circle, Shape)}")  # Output: True
print(f"Is circle an instance of Circle? {isinstance(circle, Circle)}")  # Output: True
print(f"Is square an instance of Shape? {isinstance(square, Shape)}")  # Output: True
print(f"Is square an instance of Square? {isinstance(square, Square)}")  # Output: True
print(circle.area())  # Output: Area of the circle
print(square.area())  # Output: Area of the square
print()  # Just to add a newline for better readability of the output

# In this example, we have defined a `Shape` class that represents a generic shape with a method to calculate its area. The `Circle` and `Square` classes both inherit from the `Shape` class and override the `area` method to provide specific implementations for calculating the area of a circle and a square, respectively. This demonstrates hierarchical inheritance in OOP, where multiple child classes (`Circle` and `Square`) inherit from a single parent class (`Shape`), creating a hierarchy of classes that share common attributes and behaviors while also providing their own specific implementations.

# -------------------------------------------------------------------------------------------------------------------------------------------

# A very fundamental concept in Inheritance is the concept of Interface. An interface is a blueprint for a class that defines a set of methods that the class must implement. In Python, we can create interfaces using abstract base classes (ABCs) from the `abc` module. An abstract base class is a class that cannot be instantiated and is meant to be subclassed. It can contain abstract methods, which are methods that are declared but not implemented in the abstract base class. Subclasses of the abstract base class must implement all abstract methods to be instantiable. This allows us to define a common interface for a group of related classes, ensuring that they all implement the same set of methods, which promotes consistency and code reusability. In other programming languages, interfaces and abstract classes are often distinct concepts, but in Python, we can use abstract base classes to achieve similar functionality as interfaces.

from abc import ABC, abstractmethod

# An abstract base class must inherit from the `ABC` class provided by the `abc` module, and any method that is meant to be abstract must be decorated with the `@abstractmethod` decorator. This indicates that the method is abstract and must be implemented by any subclass that inherits from the abstract base class. The abstract base class itself cannot be instantiated, and any attempt to create an instance of it will result in a `TypeError`. This enforces the requirement that subclasses must provide concrete implementations for all abstract methods defined in the abstract base class.


class Abstract_Shape(ABC):
    """This class represents a generic shape and serves as an interface for specific shapes."""

    @abstractmethod
    def area(self) -> float:
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method to calculate the perimeter of the shape."""
        pass


# The abstract methods `area` and `perimeter` are declared in the `Abstract_Shape` class, and any class that inherits from `Abstract_Shape` must provide concrete implementations for these methods to be instantiable. This allows us to define a common interface for all shapes, ensuring that they all have methods to calculate their area and perimeter, while allowing each specific shape to implement these methods in its own way. When we declare abstract methods, we use the `@abstractmethod` decorator from the `abc` module to indicate that these methods must be implemented by subclasses. Also note: in Python, an abstract method can still contain a method body, but as long as it is decorated with `@abstractmethod`, the class remains abstract and cannot be instantiated until all abstract methods are implemented in a concrete subclass.


class Rectangle(Abstract_Shape):
    """This class represents a rectangle, which is a specific type of shape."""

    def __init__(self, width, height):
        """Initialize the width and height of the rectangle."""
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


# We can create an instance of the Rectangle class and call its methods:

rectangle = Rectangle(5, 3)
print(
    f"Is rectangle an instance of Abstract_Shape? {isinstance(rectangle, Abstract_Shape)}"
)  # Output: True
print(
    f"Is rectangle an instance of Rectangle? {isinstance(rectangle, Rectangle)}"
)  # Output: True
print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 15
print(
    f"Perimeter of the rectangle: {rectangle.perimeter()}"
)  # Output: Perimeter of the rectangle: 16
print()  # Just to add a newline for better readability of the output

# In this example, we have defined an abstract base class `Abstract_Shape` that serves as an interface for specific shapes. It contains two abstract methods: `area` and `perimeter`, which must be implemented by any subclass that inherits from `Abstract_Shape`. The `Rectangle` class inherits from `Abstract_Shape` and provides concrete implementations for both the `area` and `perimeter` methods. This demonstrates how we can use abstract base classes to define a common interface for related classes, ensuring that they all implement the same set of methods while allowing for specific implementations in each subclass.

# -------------------------------------------------------------------------------------------------------------------------------------------

# Apart from abstract base classes, Python also provides a way to create interfaces using the `Protocol` class from the `typing` module. A protocol is a way to define a set of methods that a class must implement without requiring the class to inherit from a specific base class. This allows for more flexible and dynamic interfaces, as classes can implement the protocol without needing to be part of a specific class hierarchy. Protocols are particularly useful in situations where we want to define an interface for classes that may not share a common ancestor or when we want to allow for duck typing, where the focus is on whether an object has certain methods rather than its specific type.

from typing import Protocol, runtime_checkable


@runtime_checkable
class Notifier(Protocol):
    """Protocol that defines the interface for sending notifications."""

    channel_name: str

    def send(self, recipient: str, message: str) -> str:
        """Send a message to a recipient and return a status string."""
        ...


class EmailNotifier:
    """Concrete class that sends notifications through email."""

    channel_name = "Email"

    def send(self, recipient: str, message: str) -> str:
        return f"[Email] Sent to {recipient}: {message}"


class SMSNotifier:
    """Concrete class that sends notifications through SMS."""

    channel_name = "SMS"

    def send(self, recipient: str, message: str) -> str:
        return f"[SMS] Sent to {recipient}: {message}"


class SlackNotifier:
    """Another concrete class with the same required structure."""

    channel_name = "Slack"

    def send(self, recipient: str, message: str) -> str:
        return f"[Slack] Sent to {recipient}: {message}"


def notify_user(notifier: Notifier, recipient: str, message: str) -> None:
    """Function accepts any object that matches the Notifier protocol."""

    print(f"Using channel: {notifier.channel_name}")
    print(notifier.send(recipient, message))


def broadcast(notifiers: list[Notifier], recipient: str, message: str) -> None:
    """Broadcast the same message through multiple notifier implementations."""

    for notifier in notifiers:
        notify_user(notifier, recipient, message)
        print("-" * 40)


email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
slack_notifier = SlackNotifier()

broadcast(
    [email_notifier, sms_notifier, slack_notifier],
    "alice@example.com",
    "Your order has been shipped!",
)

# Since Notifier is decorated with @runtime_checkable, we can also use isinstance.
print(f"Is email_notifier a Notifier? {isinstance(email_notifier, Notifier)}")
print(f"Is sms_notifier a Notifier? {isinstance(sms_notifier, Notifier)}")
print(f"Is slack_notifier a Notifier? {isinstance(slack_notifier, Notifier)}")
print()  # Just to add a newline for better readability of the output

# In this example, `Notifier` is a protocol that requires an attribute `channel_name`
# and a method `send(recipient, message)`. None of the concrete classes inherit from
# `Notifier`, yet they all satisfy it because they provide the required structure.
# This is called structural typing. The `notify_user` and `broadcast` functions can
# work with any future class that provides the same interface, making the code flexible
# and easier to extend without changing existing function signatures.
