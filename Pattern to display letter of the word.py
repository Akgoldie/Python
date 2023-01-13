str=input("Enter the string or word: ")
n=len(str)
for i in range(0,n):
    for j in range(0,i+1):
        print(str[j],end=" ")
    print("")


#Alternative Solution:
"""
x=" "
for i in str:
    x+=i
    print(x)
"""