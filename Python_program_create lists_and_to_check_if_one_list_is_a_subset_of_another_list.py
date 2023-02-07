def is_subset(list1, list2):
    for element in list1:
        #print(element)
        if element not in list2:
            return False
    return True

list1 = []
list2 = []
def list_1():
    n1=int(input("Enter the no of element in list 1: "))
    for i in range(n1):
        elements = int(input("Enter the value of list 1: "))
        list1.append(elements)
    print("list1: ",list1)

def list_2():
    n2=int(input("Enter the no of element in list 2: "))
    for i in range(n2):
        elements = int(input("Enter the value of list 2: "))
        list2.append(elements)
    print("list2: ",list2)

list_1()
list_2()
if is_subset(list1, list2):
    print("list1 is a subset of list2.")
else:
    print("list1 is not a subset of list2.")