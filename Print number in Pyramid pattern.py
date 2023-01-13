n=int(input("Enter the row: "))
sum=1
for i in range(1,n+1):
    for j in range (1,i):
        print(sum,end=" ")
        sum+=1
    print("")
