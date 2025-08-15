class Student:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id

    def __str__(self): #to make it readable
        return f"{self.fname} {self.lname}'s Id is {self.id}"

nero = Student('Roth', 'Chau', 3018187)

print(nero) #this prints out: <__main__.Student object at 0x102fbee40>
#print(str(nero)) #same like above

print(nero.fname)

class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.output = x + y
    
    def __add__(self, other):
        return Add(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x} + {self.y} = {self.output}"
    
a = Add(3,4)

print(a)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        #return f"{self.x} and {self.y}"
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
p1 = Position(3,4)
p2 = Position(4,5)
p3 = Position(4,5)

print(p1)
print(p2)
print(p1 == p2)
print(p3 == p2)
