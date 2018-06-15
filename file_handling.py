'''
#Question 1
file = open("C:\Users\smrit\Desktop\example.txt")
list = file.readlines()
n = input('Enter a number: ')
for line in list[-n:]:
    print(line)


#Qusetion 2
with open('C:\Users\smrit\Desktop\example.txt') as file:
    data = file.readlines()
    count = 0
    for line in data:
        list = line.split()
        count = count + (len(list))
print('Frequency of words =', count)


#Question 3
with open('C:\Users\smrit\Desktop\example.txt') as file:
    with open("example1.txt", "w") as file1:
        for line in file:
            file1.write(line)


#Question 4
with open('C:\Users\smrit\Desktop\example.txt') as file1, open('C:\Users\smrit\PycharmProjects\Acadview\example1.txt') as file2:
    for line1, line2 in zip(file1, file2):
        print(line1+line2)


#Question 5
import random
file = open("Random.txt", "r+" )
list = []
for i in range(10):
    list.append(str(random.randint(1, 100)))
file.write(str(list))

print(list)
'''