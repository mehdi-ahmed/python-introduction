values = [5, 6, 586, 10, 85, -55, 66, 1]
max: int = values[0]

for item in values:
    if item > max:
        max = item

print(max)
