def sumOfLists(l1, l2):
    l3 = []
    l3.append(sum(l1))
    l3.append(sum(l2))

    return l3

list1 = [11,22,33,44,21,54,67,54,33,222,4]
list2 = [3,4,5,32,21,33,66,75,87,97,1]

print("List1: {}\nList2: {}".format(list1, list2))

print("List 3: {}".format(sumOfLists(list1, list2)))
