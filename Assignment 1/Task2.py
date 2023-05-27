# Task 2
# Write a python code to do the following task
# i. Take 2 integers from user input
# ii. Make the following functions of Add, Subtract, Multiply and Divide Remainder, Square, and Cube of a given number.
# iii. Display the output of each function.
# Note: Square and Cube functions can take 1 value.


def add(first_int, second_int):
    sum = first_int + second_int
    return sum

def subtract(first_int, second_int):
    subtract = first_int - second_int
    return subtract

def multiply(first_int, second_int):
    product = first_int * second_int
    return product
    
def divide(first_int, second_int):
    remainder = first_int/second_int
    return remainder

def square(value):
    sq = value*value
    return sq

def cube(value):
    cu = value*value*value
    return cu

first_int = int(input("Enter first integer : "))
second_int = int(input("Enter second integer : "))

print("Sum is : ", add(first_int, second_int))
print("Subtraction is : ", subtract(first_int, second_int))
print("Product is : ", multiply(first_int, second_int))
print("Remainder (after division) is : ", divide(first_int, second_int))

value = int(input("Enter a value to find square and cube : "))
print("Square of ",value, " is ", square(value))
print("Cube of ",value, " is ", cube(value))








