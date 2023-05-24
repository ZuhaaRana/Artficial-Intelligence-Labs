
#Merge 

#Merge two dictionaries using update () method

dictionary_1 = {'A': 'aaa', 'B': 'bbb', 'C':'ccc'}
dictionary_2 = {'D': 'ddd', 'E': 'eee','F':'fff'}

print("Dictionary 1 : ")
print(dictionary_1)

print("Dictionary 2 : ")
print(dictionary_2)

dictionary_1.update(dictionary_2)
dictionary_3 = dictionary_1

print("Merged Dictionary : ")
print(dictionary_3)




