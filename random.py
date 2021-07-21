from Lib import random

for i in range(3):
    print(random.random())
# 0.527635977267916
# 0.9087153399507294
# 0.7393979069452381

for i in range(3):
    print(random.randint(10, 20))
# 14
# 15
# 15

# Pick a random item from a List
members = ['Bob', 'Mehdi', 'Ed', 'Tom']
leader = random.choice(members)
print(leader)
