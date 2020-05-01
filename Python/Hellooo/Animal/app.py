# 继承
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass


class Cat:
    pass


dog1 = Dog()
dog1.walk()