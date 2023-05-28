# Task 5
# Take a start value and end value from user and print Even and Odd numbers between them using
# for and while loop.

#(Using for loop)

start = int(input("Enter starting value : "))
end = int(input("Enter ending value : "))
for  i in range(start,end):
    if i%2==0:
        print(i, " is Even.")
    else:
        print(i, " is Odd.")


#(Using while loop)

start = int(input("Enter starting value : "))
end = int(input("Enter ending value : "))
i = start
while i <= end:
    if i%2==0:
        print(i, " is Even.")
        i+=1
    else:
        print(i, " is Odd.")
        i+=1
