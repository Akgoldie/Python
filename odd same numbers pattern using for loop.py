n=int(input("Enter the number row: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i*2)-1, end=" ")
    print("\r")