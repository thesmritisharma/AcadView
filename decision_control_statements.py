#Question 1
print("Q.1-\n")
yr = int(input("Enter a year: "))
if yr % 400 == 0:
    print(yr, "is a leap year.")
elif yr % 100 == 0:
    print(yr, "is not a leap year")
elif yr % 4 == 0:
    print(yr, "is a leap year.")
else:
    print(yr, "is not a leap year.")

#Question 2
print("Q.2-\n")
l = int(input('Enter length: '))
b = int(input('Enter breadth: '))
if l == b:
    print("Square")
else:
    print("Rectangle")


#Question 3
print("Q.3-\n")
a = int(input('Enter age 1: '))
b = int(input('Enter age 2: '))
c = int(input('Enter age 3: '))
if a > b:
    if a > c:
        large = a
        if b > c:
            small = c
        else:
            small = b
    else:
        large = c
        if a > b:
            small = b
        else:
            small = a
elif b > c:
    large = b
    if a > c:
        small = c
    else:
        small = a
else:
    large = c
print("Youngest:", small)
print("Oldest:", large)


#Question 4
print("Q.4-\n")
age = int(input('Enter your age: '))
sex = input('Sex(M/F): ')
mstat = input('Marital Status(Y/N): ')
if sex == 'F':
    print("Urban Areas")
elif sex == 'M':
    if age >= 20 & age <= 40:
        print("Anywhere")
elif sex == 'M':
    if age >= 40 & age <= 60:
        print("Urban Areas")
if age < 20 | age > 60:
    print('Error')


#Question 5
print("Q.5-\n")
qty = int(input('Quantity of item: '))
cost = qty * 100
dis = int(10 / 100 * cost)
if cost > 1000:
    print("Discount of 10%. Final Cost is:", cost - dis)
else:
    print("No discount. Final Cost is:", cost)