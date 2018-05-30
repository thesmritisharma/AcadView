#Question 1
vowels = ['a', 'e', 'i', 'o', 'u']
print("Q.1-", "\n     Vowels list:" , vowels)

#Question 2
vowels.extend(['google', 'apple', 'facebook', 'microsoft', 'tesla'])
print("\nQ.2-", "\n     Extended list:" , vowels)

#Question 3
print("\nQ.3-", "\n     Total occurences of 'google':", vowels.count('google'))

#Question 4
numbers = [123,35,23,86,92]
print("\nQ.4-", "\n     List of numbers:", numbers)
numbers.sort()
print("\n     List of numbers in ascending order:", numbers)

#Question 5
A = [2, 8, 12, 23, 34]
print("\nQ.5-", "\n     Sorted array A:", A)
B = [1, 9, 15, 33, 45]
print("\n     Sorted array B:", B)
C = A + B
C.sort()
print("\n     Sorted array C:", C)

#Question 6

#Stack
stack = ['apple', 'orange', 'banana']
print("\nQ.6-","\n     STACK:")
print("    ", stack)
print("PUSH-")
stack.append('mango')
print("    ", stack)
stack.append('grapes')
print("    ", stack)
print("POP-")
stack.pop()
print("    ", stack)
stack.pop()
print("    ", stack)

#Queue
queue = ['apple', 'orange', 'banana']
print("\n    ", "QUEUE:")
print("    ", queue)
print("INSERTION-")
queue.append('mango')
print("    ", queue)
queue.append('grapes')
print("    ", queue)
print("DELETION-")
queue.pop(0)
print("    ", queue)
queue.pop(0)
print("    ", queue)

