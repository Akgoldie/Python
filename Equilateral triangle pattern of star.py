n=int(input("Enter the number of rows: "))
k=n
for i in range(1,n+1):
    for j in range(k,0,-1):

        print(" ",end=" ")
    k -= 1
    for j in range(0,i):
        print("* ",end=" ")
    print("")


