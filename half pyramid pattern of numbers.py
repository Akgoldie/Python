n=int(input("Enter the number row: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print("\r")