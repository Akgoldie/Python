n=int(input("Enter the number row: "))
for i in range(n,0,-1):
    for j in range(0,i):
        print(i, end='')
    print("\r")


