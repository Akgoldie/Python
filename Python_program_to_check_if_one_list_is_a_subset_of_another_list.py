def is_subset(list1, list2):
    for element in list1:
        #print(element)
        if element not in list2:
            return False
    return True

list1 = [1, 2, 3, 4, 5]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if is_subset(list1, list2):
    print("list1 is a subset of list2.")
else:
    print("list1 is not a subset of list2.")