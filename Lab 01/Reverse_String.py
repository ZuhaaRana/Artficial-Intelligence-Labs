#REVERSE A STRING

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

#Reverse a string by function

def reverse_string(new_string):  
    reversed_string = ""
    for i in new_string:  
        reversed_string = i + reversed_string 
    return reversed_string  
     
new_string =  input("Enter a string to reverse : ") 

print("The original string is: ", new_string)  
print("The reversed string is", reverse_string(new_string))

#Reverse a string using slicing

new_list = ["h", "e", "l", "l", "o"]
print("Given List : ")
print(new_list)
print("Reverse of the list is : ")
print(new_list[::-1])

#Python builtin function to reverse a string

new_list = ["h", "e", "l", "l", "o"]
print("Given List : ")
print(new_list)
print("Reversed string : ")
new_list.reverse()
print(new_list)

