#19 sum of series
import math
n=int(input("Enter the limit: "))
x=float(input("Enter the number: "))
sum=0
for i in range (1,n+1):
    nume=x**i
    dem=math.factorial(i*2)
    units=nume/dem
    if i==1:
        sum=1
    elif i%2==0:
        sum=sum-units
    else:
        sum=sum+units
print("Sum of the series: ",sum)
