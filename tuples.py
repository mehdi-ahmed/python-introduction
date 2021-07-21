# tuples are immutable - You cannot modify them. Used typically when we don't want a list to be modified.
numbers = (1, 1, 2, 3)

print(numbers.count(1))  # 2

print(numbers.index(2))  # 2

# Error - Immutability
# numbers[0] = -1  -- TypeError: 'tuple' object does not support item assignment
