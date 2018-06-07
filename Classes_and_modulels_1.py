'''
#Question 1
class Circle:
    def __init__(self, r):
        self.r = r
    def getArea(self):
        area = 3.14 * self.r * self.r
        return area
    def getCircumference(self):
        cir = 2 * 3.14 * self.r
        return cir
obj = Circle(5)
print(obj.getArea())
print(obj.getCircumference())


#Question 2
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(self.name, self.roll, sep = '\n')
obj = Student('Smriti', 1215273)
obj.display()


#Question 3
class Temperature:
    def convertFahrenheit(self, c):
        self.f = c * (9 / 5) + 32
        return self.f
    def convertCelsius(self, f):
        self.c = (f - 32) * (5 / 9)
        return self.c
obj = Temperature()
print(obj.convertFahrenheit(32))
print(obj.convertCelsius(32))


#Question 4
class MovieDetails:
    def __init__(self, name, a_name, year, rating):
        self.name = name
        self.a_name = a_name
        self.year = year
        self.rating = rating
    def display(self):
        print(self.name, self.a_name, self.year, self.rating, sep = '\n')
    def update(self, name, a_name, year, rating):
        self.name = name
        self.a_name = a_name
        self.year = year
        self.rating = rating
obj = MovieDetails('Raazi', 'Alia', 2018, 4)
obj.display()
obj.update('Carry on Jatta 2', 'ABC', 2018, 5)
obj.display()


#Question 5
class Expenditure:
    def __init__(self, expenditure, savings):
        self.expenditure = expenditure
        self.savings = savings

    def display(self):
        print(self.expenditure, self.savings, sep='\n')

    def totalsalary(self):
        total = self.expenditure + self.savings
        return total

    def displaysalary(self):
        print(Expenditure.totalsalary(self))


obj = Expenditure(10000, 18000)
obj.display()
obj.totalsalary()
obj.displaysalary()
'''