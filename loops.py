#Question 1
x = []
for i in range(10):
    x.append(int(input("Enter a no.: ")))
print(x)

#Question 2
while True:
    print("An Infinite Loop")

#Question 3
list1 = []
list2 = []
for i in range(5):
    list1.append(int(input("Enter an integer: ")))
    list2.append(list1[i] * list1[i])
print(list1)
print(list2)

#Question 4
mix = [11, 'hello', 3.5, 'orange', 45, 'banana', 36, 76.5]
integer = []
floating = []
string = []
for i in mix:
    if type(i) == int:
        integer.append(i)
    elif type(i) == float:
        floating.append(i)
    elif type(i) == str:
        string.append(i)
print(integer, floating, string, sep = "\n")

#Question 5
prime = []
for i in range(1, 101):
    flag = 0
    if i == 1:
        continue
    if i == 2:
        prime.append(2)
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        prime.append(i)
print('Prime Numbers:', prime)

#Question 6
for i in range(4):
    for j in range(i+1):
        print('*', end = '')
    print('')

#Qusetion 7
dict = {}
name = ['abc', 'xyz', 'pqr']
for i in name:
    dict[i] = int(input('Enter an integer: '))
print(dict)

#Qusetion 8
list = []
for i in range(5):
    list.append(int(input("Enter an item: ")))
print('List:', list)
while not (list == []):
    list.remove(int(input("Enter item to be deleted: ")))
    print('After deletion:', list)
print("List Empty")
