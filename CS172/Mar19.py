'''class Complex:
    def __init__(self, real: float, imag: float = 0.0):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return '({:.3f}{:+.3f}i)'.format(self.real, self.imag)
    
    def __str__(self):
        return self.__repr__()
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other)
    
    def conjufate(self):
        return Complex(self.real, -self.imag)
    
c1 = Complex(1.3, -1.768)
print(c1)
print(c1 + c2)
#print(c1.__add__(c1))

c2 = Complex(2.5, -1.8)'''

"""Define a class for circles that takes a radius as an argument and defines the
`area` and `circumference` methods with the obvious meanings."""
import math

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 2*(math.pi)*self.radius
    
    def circum(self):
        return 2 * math.pi * self.radius
    
c1 = Circle(5)
print('area:' {c1.area():.2f})
print('circumference:' {c1.circum():.2f})


    
