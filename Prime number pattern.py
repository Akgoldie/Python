n=int(input("Enter the number row: "))
num=1
for i in range(0,n):
    for j in range(0,i+1):
        print(num*num, end=" ")
        num+=1
    print("\r")
