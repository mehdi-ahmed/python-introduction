# While
i = 0
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done!')

# For

for item in 'Python':
    print(item)

for item in ['Mosh', 'Mehdi', 'John']:
    print(item)

for item in range(10):
    print(item)

for item in range(99, 199):
    print(item)

# step = 2
for item in range(99, 199, 2):
    print(item)

# Nested loops - generate coordinates
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
