

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
