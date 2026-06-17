# Set in Python

# Set is the collection of unordered items.
# Each element in the set must be unique & immutable.

nums = {1, 2, 3, 4}

set2 = {1, 2, 2, 2}
# Repeated elements are stored only once, so it resolves to {1, 2}

null_set = set()    # Empty set syntax (NOT {} which creates empty dict)

# --- Additional Revision Notes ---

# 1. Creating Sets:
set1 = {1, 2, 3, 4}           # Using curly braces
set2 = set([1, 2, 3, 4])      # Using set() constructor with list
set3 = set("hello")           # {'h', 'e', 'l', 'o'} (repeated 'l' removed)
set4 = {1, "hello", 3.14}     # Mixed data types (all immutable)

# 2. Important: Empty set vs Empty dict
empty_set = set()             # Empty SET
empty_dict = {}               # Empty DICTIONARY (NOT set)

# 3. Set properties:
# - UNORDERED: No indexing (cannot do set[0])
# - UNIQUE elements: Duplicates automatically removed
# - IMMUTABLE elements: Can only store immutable types (int, float, string, tuple)
# - MUTABLE set itself: Can add/remove elements

# 4. Adding elements:
nums = {1, 2, 3}
nums.add(4)          # {1, 2, 3, 4}
nums.add(2)          # {1, 2, 3, 4} (no change, 2 already exists)
nums.add("hello")    # {1, 2, 3, 4, 'hello'}

# 5. Removing elements:
nums = {1, 2, 3, 4, 5}
nums.remove(3)       # {1, 2, 4, 5} (raises KeyError if not found)
nums.discard(3)      # {1, 2, 4, 5} (no error if not found)
nums.pop()           # Removes and returns an arbitrary element
nums.clear()         # Removes all elements -> set()

# 6. Set Operations:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (|) - All elements from both sets
union = set_a | set_b              # {1, 2, 3, 4, 5, 6}
union = set_a.union(set_b)         # Same as above

# Intersection (&) - Common elements
intersection = set_a & set_b       # {3, 4}
intersection = set_a.intersection(set_b)  # Same as above

# Difference (-) - Elements in first set but not in second
difference = set_a - set_b         # {1, 2}
difference = set_a.difference(set_b)  # Same as above

# Symmetric Difference (^) - Elements in either set but not both
sym_diff = set_a ^ set_b           # {1, 2, 5, 6}
sym_diff = set_a.symmetric_difference(set_b)  # Same as above

# 7. Set Methods:
nums = {1, 2, 3}

# add() - Add single element
nums.add(4)              # {1, 2, 3, 4}

# update() - Add multiple elements (from another set/list)
nums.update([5, 6, 7])   # {1, 2, 3, 4, 5, 6, 7}

# remove() - Remove element (raises error if not found)
nums.remove(7)           # {1, 2, 3, 4, 5, 6}

# discard() - Remove element (no error if not found)
nums.discard(10)         # No error, set unchanged

# pop() - Remove and return arbitrary element
removed = nums.pop()     # Removes and returns some element

# clear() - Remove all elements
nums.clear()             # set()

# copy() - Create shallow copy
nums_copy = nums.copy()

# 8. Set Comparison:
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# issubset() - Check if all elements of set1 are in set2
set1.issubset(set2)        # True

# issuperset() - Check if set2 contains all elements of set1
set2.issuperset(set1)      # True

# isdisjoint() - Check if sets have no common elements
set1.isdisjoint({4, 5, 6}) # True (no common elements)

# 9. Looping through sets:
nums = {1, 2, 3, 4, 5}
for num in nums:
    print(num)        # Order may vary (unordered)

# 10. Checking membership:
if 3 in nums:
    print("3 is in set")

if 10 not in nums:
    print("10 is not in set")

# 11. Set Comprehension:
squares = {x**2 for x in range(5)}    # {0, 1, 4, 9, 16}
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

# 12. Converting between list and set:
my_list = [1, 2, 2, 3, 3, 3, 4]
unique_set = set(my_list)        # {1, 2, 3, 4} (removes duplicates)
unique_list = list(unique_set)   # [1, 2, 3, 4]

# 13. Frozenset - Immutable version of set:
frozen = frozenset([1, 2, 3])    # Cannot add/remove elements

# Key Points to Remember:
# - Use {} for set with elements, but {} alone is empty DICTIONARY
# - Elements must be IMMUTABLE (no lists as elements)
# - Set itself is MUTABLE (can add/remove)
# - UNORDERED (no indexing, no slicing)
# - NO duplicate elements (automatic deduplication)
# - Very fast for membership testing (in operator)
# - Useful for removing duplicates from lists