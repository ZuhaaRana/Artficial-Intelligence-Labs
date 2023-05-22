#SQRT(x)

# Sqrt(x) without any built-in methods (10 Marks)
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned. 

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842…, and since the decimal part is truncated, 2 is returned.

def to_find_Sqrt(new_int):
    if (new_int == 0 or new_int == 1):
        return new_int

    i = 1
    N = 1

    while (N <= new_int):
        i = i+1
        N = i * i
    return i - 1

new_int = int(input("Enter a positive integer : "))

print(to_find_Sqrt(new_int))
