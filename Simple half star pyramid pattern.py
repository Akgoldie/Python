n=int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print("")



#Alternative Solution:
'''
n=int(input("Enter the number of rows: "))
for i in range (1,n+1):
        print("* "*i)
'''