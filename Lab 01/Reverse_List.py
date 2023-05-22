#REVERSE A LIST

# Write a function that reverses a string. The input string is given
# as an array of characters. You can use Python list to create the
# array of characters. Do not allocate extra space for another array
#you must do this reversal by modifying the input array in-place #with O(1) extra memory.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

print("List : ")
new_list = ["h", "e", "l", "l", "o"]
print(new_list)
print("Reverse of the list is : ")
print(new_list[::-1])
print("Another method to reverse is : ")
new_list.reverse()
print(new_list)

#Reverse String by function

new_list = ["h", "e", "l", "l", "o", "o"]
print("Given List : ")
print(new_list)

#for i in range(0, int(len(str) / 2)):
    #str[i] = str[len-1]

print(len(new_list))
i = 0
j = len(new_list) - 1
print(j)

while (i < j):

    temp = new_list[i]
    new_list[i] =new_list[j]
    new_list[j] = temp
    i = i+1
    j = j+1

print("Reversed List : ")
print(new_list)
