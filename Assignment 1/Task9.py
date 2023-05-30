
# Task 9
# list = ["apple", "cherry", "orange", "kiwi", "melon", "mango"]
# i. Remove “cherry” and “melon” from list.
# ii. Add “banana” at second last index.

list = ["apple", "cherry", "orange", "kiwi", "melon", "mango"]
list.remove("cherry")
print("List after removing Cherry : ", list)
list.remove("melon")
print("List after removing Melon : ", list)
list.insert(-1,"banana")
print("List after adding Banana at second last index : ",list)
