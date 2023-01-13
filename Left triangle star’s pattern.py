n=int(input("Enter the number of rows: "))

for i in range(1,n):
    for j in range(n,0,-1):
        if(j>i):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print("")
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if(j>i):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    print("")
