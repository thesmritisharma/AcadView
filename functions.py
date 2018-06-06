#Question 1
def area():
    r = int(input('Enter radius of sphere: '))
    area = 4 * 3.14 * r * r
    print('Area of the sphere is:', area)
    return


area()


#Question 2
def perfect():
    for i in range(1, 1001):
        sum = 0
        for j in range(1, i):
            if i % j == 0 and i != j:
                sum += j
        if sum == i:
            print(i)


perfect()


#Question 3
def mul(i):
    if i == 1:
        return 12
    else:
        return 12 + mul(i - 1)

for i in range(1, 11):
    print('12 *', i, '=', mul(i))


#Question 4
def power(a, b):
    if b == 1:
        return a
    else:
        return a * power(a, b-1)


a = int(input('Enter a: '))
b = int(input('Enter b: '))
print(power(a, b))


#Question 5
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

num = int(input('Enter a no.: '))
dict = {}
dict[num] = fact(num)
print(dict)