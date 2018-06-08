'''
#Question 1
class Animal:
    def animal_attribute(self):
        print('Animals')

class Tiger(Animal):
    def tiger_method(self):
        print('Tigers')


obj = Tiger()
obj.animal_attribute()


#Question 2
A B
A B


#Question 3
class Cop:
    def __init__(self, name, age, work, exp, des):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.des = des

    def add(self, name, age, work, exp, des):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.des = des

    def display(self):
        print(self.name, self.age, self.work, self.exp, self.des, sep = '\n')

    def update(self, name, age, work, exp, des):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.des = des


class Mission(Cop):
    def add_mission_details(self):
        print('Available for mission')


obj = Mission('AAA', 28, 'YYY', 2, 'Jr.\n')
obj.display()
obj.add('ABC', 32, 'XYZ', 9, 'Sr.\n')
obj.display()
obj.update('PQR', 25, 'XYZ', 4, 'Jr.\n')
obj.display()
obj.add_mission_details()


#Question 4
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def Area(self):
        area = self.length * self.breadth
        print('Class Square')

class Rectangle(Shape):
    def Area(self):
        self.area = self.length * self.breadth
        print('Class Rectangle')
        return self.area

class Square(Shape):
    def Area(self):
        self.area = self.length * self.breadth
        print('Class Square')
        return self.area

rect = Rectangle(2, 4)
sqr = Square(2, 2)

for obj in (rect, sqr):
    print(obj.Area())
'''