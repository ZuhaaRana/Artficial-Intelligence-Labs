#VALID PALINDROME

# Given a string s, determine if it is a palindrome, considering only
#alphanumeric characters and ignoring cases. Refer to this link to
#learn about Python string functions which might come handy in this
#task.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.



import re
def Palindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

new_string = "A man a plan a canal Panama"
print(new_string)
lower_string = new_string.lower()
updated_string = re.sub(r"\s+", "", lower_string, flags=re.UNICODE)

print(updated_string)
to_check = Palindrome(updated_string)

if (to_check):
    print("true")
    print("Explanation: ", updated_string, " is a Palindrome.")
else:
    print("false")
    print("Explanation: ", updated_string, " is not Palindrome.")
