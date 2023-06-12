
# Task 18
# Create a function dsort() to sort a list in descending order, taking
#a list as argument and returning it. Use the following list and print 
#it.
# list = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]

def dsort(l):
    l.sort(reverse = True)
    return l

list = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]

print(f"Original array: {list}")
print(f"Sorted array: {dsort(list[::])}")
