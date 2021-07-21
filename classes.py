class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('move')


point1 = Point(22, 99)
point1.draw()

point1.x = 10
point1.y = 30
print(point1.y)  # 30

# Constructors

point2 = Point(10, 20)
# point2.x = 77
print(point2.x)  # 10
