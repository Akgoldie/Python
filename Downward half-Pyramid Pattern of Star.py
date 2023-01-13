n=int(input("Enter the number of rows: "))
for i in range (n,0,-1):    #for i in range(rows + 1, 0, -1):
    for j in range(i,0,-1): #for j in range(0, i - 1):
        print("*", end=" ")
    print("")


#Alternative Solution:
'''
n=int(input("Enter the number of rows: "))
for i in range (n+1,0,-1):
        print("* "*i)
'''