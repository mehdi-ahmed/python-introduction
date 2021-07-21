matrix = [
    [1, 5, 9],
    [18, 54, 19],
    [0, 7, 45]
]

print(matrix[0][2])
# result = 9

# Loop over a Matrix (2D Lists)
for row in matrix:
    for item in row:
        print(item)

# Insert an item at the end of the list
a_list = [1, 5, 88, 0, 44]
a_list.append(-999)
print(a_list)
# [1, 5, 88, 44, 0, -999]

# Insert an item at a position
a_list = [1, 5, 88, 0, 44]
a_list.insert(0, -999)
print(a_list)
# [-999, 1, 5, 88, 0, 44]

# Remove an item
a_list = [1, 5, 88, 0, 44]
a_list.remove(88)
print(a_list)
# [-999, 1, 5, 0, 44]

# Remove all
a_list = [1, 5, 88, 0, 44]
a_list.clear()
print(a_list)
# []

# Remove last item
a_list = [1, 5, 88, 0, 44]
a_list.pop()
print(a_list)
# [1, 5, 88, 0]

# Return the index of an item
a_list = [1, 5, 88, 0, 44]
print(a_list.index(88))
# 2

# Check if a value exists
a_list = [1, 5, 88, 0, 44]
print(88 in a_list)
# true
print(-777 in a_list)
# False

# Count a particular item in a list
a_list = [1, 5, 88, 0, 88, 44, 88]
print(a_list.count(88))
# 3

# Sort and reverse a list - Do not call sort() inside a print
a_list = [1, 5, -99, 0, 788, 44, 88]
a_list.sort()
print(a_list)
# [-99, 0, 1, 5, 44, 88, 788]
a_list.reverse()

print(a_list)
# [788, 88, 44, 5, 1, 0, -99]

# Copy a list
a_list = [1, 5, -99, 0, 788, 44, 88]
a_list_copy = a_list.copy()
a_list.append(10)
print(a_list_copy)
# [1, 5, -99, 0, 788, 44, 88]
print(a_list)
# [1, 5, -99, 0, 788, 44, 88, 10]

