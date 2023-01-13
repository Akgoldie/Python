n=int(input("Enter the number row: "))
for i in range(0,n):
    n-=1
    for j in range(n+1,0,-1):
        print(i+1, end="")
    print("\r")