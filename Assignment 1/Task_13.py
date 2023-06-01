
#Task 13
#Write a python code to find the factorial of number using recursion.

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input('Enter your number: '))
print(f"Factorial : {factorial(num)}")
