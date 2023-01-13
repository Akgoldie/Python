n=int(input("Enter the number of rows: "))
for i in range(n+1,1,-1):
    for j in range(n+1,1,-1):
        if(j>i):
            print(" ",end=' ')
        else:
            print("*",end=' ')
            #print("*", end=' ')
    print("")
"""
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

"""