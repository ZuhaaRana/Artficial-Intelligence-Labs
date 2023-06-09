
# Task 14
# Write a python code to make a list. Populate it with random number
#using random number generator and then find the min and max value from
#the list. Size of list should be given by user. Note: do not use max 
#and min built-in function.

from random import randint
def minmax1 (x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum: maximum = i
    return (minimum,maximum)


size = int(input('Enter size of the list: '))
list = [randint(0,100) for i in range(size)]

min, max = minmax1(list)

print(f"List: {list}\nMax: {max}\nMin: {min}")
