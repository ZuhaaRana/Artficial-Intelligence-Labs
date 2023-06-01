
# Task 12
# Write a python code to find if the number is an Armstrong number or not!
# Note: abcd = an + bn + cn +dn +…., n is the total number of digits.

n = int(input('Enter your number: '))
pwr = len(str(n))
sum = 0
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** pwr
   temp //= 10

if n == sum:
   print(f"{n} is an Armstrong number")
else:
   print(f"{n} is not an Armstrong number")
