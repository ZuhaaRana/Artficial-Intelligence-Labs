
# Task 15
# Write a python code to create a tuple. And do the following tasks.
# i. Create Tuple = (“john”,”mark”,12,”14”,”orange”,4.5)
# ii. Then update the Tuple and add a new value 6.5.
# iii. After updating the value, create a function that shows the count
# of how many integers, strings and float variables does it have.

==Tuple = ("john", "mark", 12, "14", "orange", 4.5)
print(f"Original tuple: {Tuple}")
print("Adding..")
Tuple += (6.5,)
print(f"Updated tuple: {Tuple}")

def count(t):
    strs = 0
    floats = 0
    ints = 0
    for i in t:
        if type(i) == int:
            ints += 1
        elif type(i) == str:
            strs += 1
        elif type(i) == float:
            floats += 1

    return strs, floats, ints

strN, floatN, intN = count(Tuple)
print("Number of string variables: {}".format(strN))

print("Number of float variables: {}".format(floatN))

print("Number of integer variables: {}".format(intN))
