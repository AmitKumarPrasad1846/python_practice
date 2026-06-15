# List Methods

list = [2, 1, 3]

# 1. append() - Adds one element at the end
list.append(4)          # Result: [2, 1, 3, 4]

# 2. sort() - Sorts in ascending order
list.sort()             # Result: [1, 2, 3]

# 3. sort(reverse=True) - Sorts in descending order
list.sort(reverse=True) # Result: [3, 2, 1]

# 4. reverse() - Reverses the list
list.reverse()          # Result: [3, 1, 2]

# 5. insert() - Inserts element at specific index
# list.insert(idx, el)    # Syntax: list.insert(index, element)

# --- Additional Revision Notes ---

# Example list for demonstration
numbers = [2, 1, 3]

# 6. remove() - Removes first occurrence of a value
numbers = [2, 1, 3, 1]
numbers.remove(1)       # Result: [2, 3, 1] (removes only first 1)

# 7. pop() - Removes element at index (or last if no index)
numbers = [2, 1, 3]
numbers.pop()           # Result: [2, 1]  (removes last element)
numbers.pop(0)          # Result: [1]    (removes element at index 0)

# 8. index() - Returns index of first occurrence
numbers = [2, 1, 3, 1]
idx = numbers.index(1)  # Returns: 1 (index of first 1)
idx = numbers.index(3)  # Returns: 2

# 9. count() - Counts occurrences of an element
numbers = [2, 1, 3, 1, 1]
count = numbers.count(1)  # Returns: 3

# 10. copy() - Creates a shallow copy
original = [1, 2, 3]
duplicate = original.copy()  # New independent list

# 11. extend() - Adds all elements of another list
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)     # Result: [1, 2, 3, 4]

# 12. clear() - Removes all elements
numbers = [1, 2, 3]
numbers.clear()         # Result: []

# Important Notes:
# - append() adds ONE element (even if it's a list)
# - extend() adds multiple elements from another list
# - insert() shifts elements to the right
# - sort() and reverse() modify the original list (in-place)
# - sort() only works if all elements are of comparable types

# Example differences:
list1 = [1, 2]
list1.append([3, 4])    # Result: [1, 2, [3, 4]]  (nested list)
list2 = [1, 2]
list2.extend([3, 4])    # Result: [1, 2, 3, 4]    (flattened)

# insert() examples:
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")  # Result: ["apple", "orange", "banana", "cherry"]
fruits.insert(0, "mango")   # Result: ["mango", "apple", "orange", "banana", "cherry"]
fruits.insert(100, "grape") # Inserts at end if index too large

# Common mistakes:
# - append() vs extend() confusion
# - Forgetting that sort() returns None (modifies in place)
# - Using sort() on mixed types (int and str) - will cause TypeError