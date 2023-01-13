#18 sum of series

n=int(input("Enter the limit: "))
x=float(input("Enter the number: "))
sum=0
def fact(number):
    sum_fact=1
    for i in range(1,number+1):
        sum_fact*=i
    return sum_fact

for i in range (1,n+1):
    nume=x**i
    dem=fact(i+1)
    units=nume/dem
    if i%2==0:
        sum=sum-units
    else:
        sum=sum+units
print("Sum of the series: ",sum)