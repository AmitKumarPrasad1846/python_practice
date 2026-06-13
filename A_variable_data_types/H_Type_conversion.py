# -------------------------------
# Type Conversion vs Casting
# -------------------------------

# Type Conversion (Automatic)
# Python automatically converts compatible types
a, b = 1, 2.0
sum = a + b
print(sum)   # Output: 3.0

# Error Example: Incompatible types (int + str)
a, b = 1, "2"
# sum = a + b   # ❌ TypeError

# Casting (Manual Conversion)
# We can explicitly convert types using functions
a, b = 1, "2"
sum = a + int(b)   # Convert string "2" to integer
print(sum)         # Output: 3


# type conversion
a = 2
b = 4.25
print(a + b)

# type casting
a, b = 1, "2"
c = int(b)
print(a + c)
print(type(c))

