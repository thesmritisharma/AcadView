'''
#Question 1
import time
import threading
from threading import Thread

def sleepMe():
    print('Thread is sleeping',threading.currentThread().getName())
    time.sleep(5)
    print("Thread is awake", threading.currentThread().getName())

t=Thread(target=sleepMe,args=())
t.start()


#Question 2
import time
import threading
from threading import Thread

def number():
    for x in range(1, 11):
        print(x)
        time.sleep(2)

t=Thread(target = number, args = ())
t.start()


#Qusetion 3
import time
import threading
from threading import Thread

def func():
    list = [1,2,3,4,5]
    count = 0
    for x in list:
        count += 2
        print(x)
        time.sleep(count)

t=Thread(target = func, args = ())
t.start()


#Question 4
import time
import threading
from threading import Thread

def fact(num):
    time.sleep(2)
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

num = int(input('Enter a no.: '))
dict = {}
dict[num] = fact(num)
print(dict)

t=Thread(target=fact(num), args=())
t.start()
'''
