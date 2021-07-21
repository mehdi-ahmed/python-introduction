from Lib import random


class Dice:
    def roll(self):
        return f'({random.randint(1, 6)}, {random.randint(1, 6)})'

    def roll_mosh_solution(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


random_roll = Dice()
print(random_roll.roll())
print(random_roll.roll_mosh_solution())
