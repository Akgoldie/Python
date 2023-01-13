n=int(input("Enter the number of rows: "))
for i in range(1):
    for j in range(1,n):
        print("* "*j)
    for k in range(n,0,-1):
        print("* "*k)
