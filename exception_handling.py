'''
#Question 1
while True:
     try:
         a = 3
         if a < 4:
             a = a / (a - 3)
             print(a)
         break
     except ZeroDivisionError:
         print("ZeroDivisionError")


#Question 2
while True:
        try:
            l = [1, 2, 3]
            print(l[3])
            break
        except IndexError:
            print("Index Error")
            break


#Question 3
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"

Output --> An exception


#Question 4
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

Output --> -5.0
a/b result in 0


#Question 5
IMPORT ERROR----->
try:
    from _foo import *
except ImportError:
    print('Import Error')

VALUE ERROR------>

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

INDEX ERROR------>
while True:
        try:
            l = [1, 2, 3]
            print(l[3])
            break
        except IndexError:
            print("Index Error")
            break


#QUestion 6
class Error(Exception):

 class AgeTooSmallError():
     pass
 while True:
     try:
         age = input('Enter your age: ')
         if age < 18:
             raise AgeTooSmallError()
     except AgeTooSmallError:
         print('Inappropriate Age...')
'''


