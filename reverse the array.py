a=[1,2,3,4,5]
temp=0
n=len(a)
for i in range (0,n//2):
    temp=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=temp
    i+=1

print(a)