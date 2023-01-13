n=int(input("Enter the number row: "))
digit=int(input("Enter the that digit: "))
for i in range(0,n):
    n-=1
    for j in range(n+1,0,-1):
        print(digit, end="")
    print("\r")