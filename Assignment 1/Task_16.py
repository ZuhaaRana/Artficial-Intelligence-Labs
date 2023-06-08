
# Task 16
# Write a python code to create a dictionary. And do the following tasks.
# i. Create Dictionary = {“brand”:”Samsung”,”OS- type”:”Oreo”,”color”:”black”,”camera”:”42 megapixels”,”year”:2012}
# ii. Then add a list in the current dictionary with key = “sizes” and values of random numbers.
# iii. Then delete the “year” key from the dictionary.
# iv. Lastly show the dictionary in following order. Use loop to show the dictionary:
# a. Brand
# b. Color
# c. Camera
# d. OS-type
# e. Sizes

from random import randint
dict = {"brand" : "Samsung", "OS-type" : "Oreo", "color" : "black", "camera" : "42 megapixels", "year" : 2012}
print("Original dictionary: {}".format(dict))

print("\nAdding sizes..")
dict['sizes'] = [randint(0, 100) for _ in range(5)]

print("\nUpdated dictionary: {}".format(dict))

print("\nDeleting year..")

del dict["year"]

c = 97
for k,v in dict.items():
    print(f"{chr(c)}. {k} : {v}")
    c += 1
