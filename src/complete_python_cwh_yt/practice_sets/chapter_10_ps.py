# -------------------------------------------------------------------------------------------------------------------------------------------

# 1. There is a Python class with a class attribute called `some_attribute`. If we use an instance of the class to change the value of `some_attribute`, will it change the value for all instances of the class? Explain your answer.

# No, changing the value of `some_attribute` using an instance of the class will not change the value for all instances of the class. This is because when we assign a new value to `some_attribute` using an instance, it creates an instance attribute that shadows the class attribute. The class attribute remains unchanged for other instances that have not overridden it. Therefore, only the instance that was used to change the value will see the new value, while other instances will still see the original class attribute value.


class MyClass:
    some_attribute = "Original Value"


# Create an instance of MyClass

instance1 = MyClass()
print(instance1.some_attribute)  # Output: Original Value

# Change the value of some_attribute using instance1

instance1.some_attribute = "New Value"
print(instance1.some_attribute)  # Output: New Value

# Create another instance of MyClass

instance2 = MyClass()
print(instance2.some_attribute)  # Output: Original Value

# The output shows that instance1 has the new value "New Value" for some_attribute, while instance2 still has the original value "Original Value". This demonstrates that changing the value of some_attribute using instance1 does not affect instance2 or the class attribute itself.

# -------------------------------------------------------------------------------------------------------------------------------------------
