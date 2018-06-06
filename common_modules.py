#Question 1
'''
Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

Index	Field	            Values
0	    4-digit year	    2008
1	    Month	            1 to 12
2	    Day	                1 to 31
3	    Hour	            0 to 23
4	    Minute	            0 to 59
5	    Second	            0 to 61 (60 or 61 are leap-seconds)
6	    Day of Week	        0 to 6 (0 is Monday)
7	    Day of year	        1 to 366 (Julian day)
8	    Daylight savings	-1, 0, 1, -1 means library determines DST


#Question 2
import time
ti = time.gmtime()
print(time.asctime(ti))
print(time.ctime())


#Question 3
import time
import datetime
from datetime import date
d = date.today()
print(d)
print(d.month)


#Question 4
import time
import datetime
from datetime import date
d = date.today()
print(d)
print(d.day)


#Question 5
import time
import datetime
from datetime import date
d = date.today()
print(d)
print(d.day)


#Qusetion 6
import time
print(time.localtime())


#Question 7
import math
print('Factorial:', math.factorial(5))


#Question 8
import math
print('GCD:', math.gcd(4,8))
'''