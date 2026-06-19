# pass Statement

# pass is a null statement that does nothing.
# It is used as a placeholder for future code.

for el in range(10):
    pass

# --- Additional Revision Notes ---

# 1. Why use pass?
# Python requires indentation for blocks (if, for, while, functions, classes)
# pass allows you to write syntactically correct code that doesn't do anything
# Useful when you're planning code structure but haven't implemented it yet

# 2. pass in different contexts:

# a) In if statements:
age = 18
if age >= 18:
    pass        # Will add logic later
else:
    pass        # Will add logic later

# b) In loops:
for i in range(5):
    pass        # Placeholder for loop body

while True:
    pass        # Placeholder (avoid infinite loop in practice)

# c) In functions:
def my_function():
    pass        # Function defined but not implemented yet

def calculate_average():
    pass        # Will implement later

# d) In classes:
class Student:
    pass        # Class defined but no attributes yet

class MyClass:
    def method1(self):
        pass
    def method2(self):
        pass

# 3. pass vs comment:
# Comment (#): Ignored by Python, doesn't affect code
# pass: Python statement that does nothing but is syntactically valid

# This is valid:
for i in range(5):
    # TODO: Add code here
    pass        # Still needs pass to avoid IndentationError

# This would cause IndentationError:
# for i in range(5):
#     # Nothing here (IndentationError)

# 4. Practical use cases:

# a) Skeleton for future implementation:
def process_data(data):
    pass        # Will implement data processing later

def validate_input(user_input):
    pass        # Will implement validation later

# b) In exception handling:
try:
    risky_operation()
except Exception:
    pass        # Ignore exception (use cautiously)

# c) In conditional stubs:
if condition:
    pass        # First condition not implemented yet
elif other_condition:
    perform_action()
else:
    pass

# 5. pass vs continue vs break:

# pass: Does nothing, continues execution normally
# continue: Skip current iteration and go to next
# break: Exit the loop entirely

for i in range(5):
    if i == 2:
        pass        # Does nothing, continues normally
    if i == 3:
        continue    # Skips printing 3
    if i == 4:
        break       # Exits loop
    print(i)
# Output: 0, 1, 2 (pass did nothing, continue skipped 3, break stopped at 4)

# 6. pass vs return:

# pass: Does nothing, continues execution
# return: Exits the function (only valid in functions)

def example1():
    pass
    print("This prints")  # This will execute

def example2():
    return
    print("This won't print")  # This never executes

# 7. pass for minimal class definitions:
# Useful when creating multiple classes with future implementation
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# 8. pass in abstract methods:
class Shape:
    def area(self):
        pass    # Base method, will be overridden by subclasses

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def area(self):
        return self.side ** 2

# 9. Common mistakes:
# - Using pass when you meant to implement something (debugging!)
# - Forgetting pass in empty loops causing IndentationError
# - Using pass in places where logic is required

# 10. Quick reference:
# pass = "Do nothing, just keep Python happy"
# Use pass when:
# - Writing skeleton code
# - Creating placeholder functions/classes
# - Avoiding IndentationError in empty blocks
# - Testing code structure before implementation