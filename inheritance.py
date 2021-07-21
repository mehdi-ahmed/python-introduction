class Mammals:
    def walk(self):
        print("walk")


class Cat(Mammals):
    pass


class Dog(Mammals):
    pass


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()
