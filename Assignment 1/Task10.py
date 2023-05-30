
# Task 10
# list = [ 1, 4, 56, 2, 4 , 12, 6, 89 ,11, 0]
# Write a program to empty list using while loop and pop() function.

list = [1, 4, 56, 2, 4, 12, 6, 89, 11, 0]
i=0
y=(len(list))
while i<y:
    list.pop()
    i+=1
print("The list after poping all elements : ",list)
