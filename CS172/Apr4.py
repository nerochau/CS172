"""class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return 'I have spoken'
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'meow'
    
class Siamese(Cat):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'MEOW'

a = Animal('mos')
print(a.speak())

c = Cat('al')
print(c.speak())

s = Siamese('joe')
print(s.speak())"""

#trying to build a circle
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y) #what does super() mean
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2*math.pi*self.radius

# Test it out
c = Circle(2, 2, 2)
print("Area:", c.area())
print("Perimeter:", c.perimeter())