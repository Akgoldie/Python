n=int(input("Enter the number: "))
sum=0
for i in range (1,n+1):#1___2
    print("i : ",i)
    for j in range (1,i+1):#1...2___
        print("j : ", j)
        sum+=j
        print("sum : ", sum)

print("Sum of the given series: ",sum)