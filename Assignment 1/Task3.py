# Task 3
# Write a python code to do the following task
# i. Take 3 float values from user input
# ii. Make a function that adds 5 to first value 10 to second value and 15 to third value
# iii. Return these 3 values and show it in the main function.


def add(first_float, second_float, third_float):
    first = first_float+5
    second = second_float+10
    third = third_float + 15
    return first,second,third
    #return second
first_float = float(input("Enter first float value : "))
second_float = float(input("Enter second float value : "))
third_float = float(input("Enter third float value : "))

print("Values after increment : ", add(first_float, second_float, third_float))


