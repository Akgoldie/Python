'''

##end with one number
n=int(input("Enter the number row: "))
for i in range(0,n):
    n-=1
    sum=0
    for j in range(n+1,0,-1):
        print(sum, end="")
        sum+=1
    print("\r")'''



#end with two number
n=int(input("Enter the number row: "))
for i in range(n,0,-1):
    for j in range(i+1):
        print(j, end=" ")
    print("\r")
