
# Task 4
# Write a python code to do the following task
# i. Take 2 strings with sequence = “HELLO, WORLD” and “HOW, arE yOu”.
# ii. Do the following tasks Concatenate the 2 strings, Make the 2 strings in upper and lowercase, Slice the strings using python string slicing. The following string should look like this after slicing; “,World” and “EyO”.
# iii. For the second string you have to use only negative number for slicing.
# Note: Read the instructions carefully. And the output of string should be exact especially in slicing.

str_1 = "HELLO, WORLD "
str_2 = "HOW, arE yOu"
print("String 1 : ",str_1)
print("String 2 : ",str_2)
str = str_1 + str_2
print("Concatenation of two strings : ",str)
print("String 1 in Upper case : ", str_1.upper())
print("String 2 in Upper case : ", str_2.upper())
print("Concatenation of two strings in Upper case : ",str.upper())
print("String 1 in lower case : ", str_1.lower())
print("String 2 in lower case : ", str_2.lower())
print("Concatenation of two strings in lower case : ",str.lower())
x = str_1.lower()
y = x.replace(" ","")
print("Slicing of string 1 : ", y[5:12])
z = str_2.replace(" ","")
print("Slicing of String 2 : ",z[-4:-1])
