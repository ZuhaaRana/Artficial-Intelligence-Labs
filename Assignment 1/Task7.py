
#Task 7
#Get number from the user and write a program to reverse the number.

num = int(input("Enter a number : "))
reverse = 0
while(num!=0):
    remainder = num % 10
    reverse = (reverse * 10 )+ remainder
    num //= 10

print("Reverse of the given number is : ", reverse)
