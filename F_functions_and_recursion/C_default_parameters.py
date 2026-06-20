# Default Parameters

# Assigning a default value to parameter, which is used when no argument is passed.

# --- Basic Syntax and Examples ---

# 1. Function with default parameter:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()                 # Output: Hello, Guest!
greet("Amit")           # Output: Hello, Amit!

# 2. Function with multiple default parameters:
def display_info(name="Unknown", age=0, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

display_info()                          # Name: Unknown, Age: 0, City: Unknown
display_info("Amit")                    # Name: Amit, Age: 0, City: Unknown
display_info("Priya", 25)               # Name: Priya, Age: 25, City: Unknown
display_info("Raj", 30, "Delhi")        # Name: Raj, Age: 30, City: Delhi

# 3. Default parameter with non-default parameters:
def power(base, exp=2):
    return base ** exp

print(power(5))         # 25 (5 squared)
print(power(5, 3))      # 125 (5 cubed)

# 4. Default parameter can be any expression:
def multiply(a, b=2+3):     # Default b = 5
    return a * b

print(multiply(4))          # 20
print(multiply(4, 6))       # 24

# --- Important Rules ---

# 5. Default parameters must come AFTER non-default parameters:
def example(a, b=10):       # Valid
    return a + b

# def example(a=10, b):     # INVALID - SyntaxError (default before non-default)
#     return a + b

# 6. Multiple default parameters:
def student_info(name, age=18, city="Delhi"):
    print(f"{name} is {age} years old from {city}")

student_info("Amit")                # Amit is 18 years old from Delhi
student_info("Priya", 20)           # Priya is 20 years old from Delhi
student_info("Raj", 22, "Mumbai")   # Raj is 22 years old from Mumbai

# 7. Using keyword arguments with defaults:
student_info(name="Amit", city="Mumbai")   # Amit is 18 years old from Mumbai
student_info(city="Chennai", name="Sara")  # Sara is 18 years old from Chennai

# --- Common Use Cases ---

# 8. Default parameter for list operations:
def append_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

print(append_to_list(1))    # [1]
print(append_to_list(2))    # [1, 2]  (Note: This is unexpected behavior!)

# 9. Better way (avoid mutable default parameters):
def append_to_list_safe(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(append_to_list_safe(1))    # [1]
print(append_to_list_safe(2))    # [2]  (Good: new list each time)

# 10. Default parameter for dictionary:
def add_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    return my_dict

print(add_to_dict("a", 1))       # {'a': 1}
print(add_to_dict("b", 2))       # {'b': 2}

# 11. Default parameter with common values:
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Amit")               # Hello, Amit!
greet_user("Priya", "Hi")        # Hi, Priya!

# 12. Default parameter for API/configuration:
def connect_to_server(host="localhost", port=8080, timeout=30):
    print(f"Connecting to {host}:{port} (timeout: {timeout}s)")

connect_to_server()                          # localhost:8080 (timeout: 30s)
connect_to_server("192.168.1.1")             # 192.168.1.1:8080 (timeout: 30s)
connect_to_server("192.168.1.1", 9000)       # 192.168.1.1:9000 (timeout: 30s)
connect_to_server(timeout=60)                # localhost:8080 (timeout: 60s)

# 13. Default parameter with built-in functions:
def custom_range(start=0, stop=10, step=1):
    return list(range(start, stop, step))

print(custom_range())           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(custom_range(5, 15))      # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# 14. Default parameter with optional logic:
def format_text(text, uppercase=False, trim=False):
    if trim:
        text = text.strip()
    if uppercase:
        text = text.upper()
    return text

print(format_text("  hello  "))             # "  hello  "
print(format_text("  hello  ", trim=True))  # "hello"
print(format_text("  hello  ", uppercase=True))  # "  HELLO  "
print(format_text("  hello  ", trim=True, uppercase=True))  # "HELLO"

# 15. Default parameters in real-world example:
def create_user(username, password, role="user", active=True, email=None):
    user = {
        "username": username,
        "password": password,
        "role": role,
        "active": active,
        "email": email
    }
    return user

user1 = create_user("amit123", "pass123")
user2 = create_user("priya456", "pass456", role="admin")
user3 = create_user("raj789", "pass789", active=False, email="raj@email.com")

print(user1)  # {'username': 'amit123', 'password': 'pass123', 'role': 'user', 'active': True, 'email': None}
print(user2)  # {'username': 'priya456', 'password': 'pass456', 'role': 'admin', 'active': True, 'email': None}
print(user3)  # {'username': 'raj789', 'password': 'pass789', 'role': 'user', 'active': False, 'email': 'raj@email.com'}

# --- Important Notes ---

# 16. Default parameter evaluation:
# Default parameters are evaluated ONCE when the function is defined
# This is why mutable defaults (list, dict) can cause unexpected behavior

def append_to_list_bad(item, my_list=[]):
    my_list.append(item)
    return my_list

# Both calls share the same list! (Bad practice)
print(append_to_list_bad(1))    # [1]
print(append_to_list_bad(2))    # [1, 2]  (Unexpected!)
print(append_to_list_bad(3))    # [1, 2, 3]

# 17. Best practices:
# - Use None for mutable defaults (list, dict, set)
# - Keep default values simple (immutable types preferred)
# - Order parameters: required, default, *args, **kwargs
# - Use meaningful default values
# - Document default parameter behavior

# 18. Common mistake - Default before non-default:
# def invalid(a=5, b):  # SyntaxError
#     return a + b

# 19. Checking if default parameter was used:
def greet_with_flag(name, greeting=None):
    if greeting is None:
        greeting = "Hello"  # Default greeting
    print(f"{greeting}, {name}!")

# 20. Default parameters with *args and **kwargs:
def complex_func(a, b=10, *args, **kwargs):
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")

complex_func(1)                         # a=1, b=10, args=(), kwargs={}
complex_func(1, 2)                      # a=1, b=2, args=(), kwargs={}
complex_func(1, 2, 3, 4)                # a=1, b=2, args=(3,4), kwargs={}
complex_func(1, 2, extra="data")        # a=1, b=2, args=(), kwargs={'extra': 'data'}

# --- Summary ---
"""
Default Parameters allow:
- Making parameters optional
- Providing fallback values
- Reducing function call clutter
- Creating flexible functions

Rules:
1. Default parameters must be after non-default parameters
2. Defaults are evaluated once at function definition
3. Avoid mutable defaults (list, dict) - use None instead
4. Can be overridden when passing arguments
"""