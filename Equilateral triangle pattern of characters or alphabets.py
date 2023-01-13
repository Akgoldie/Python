"""
n=int(input("Enter the number of rows: "))
n=5
ascii_number=65
for i in range(1,n+1):
    for j in range(n,0,-1):
        if(j>i):
            print(" ",end=' ')
        else:
            print(chr(ascii_number),end=' ')
            ascii_number+=1
            print(chr(ascii_number), end=' ')
            ascii_number += 1
    print("")
"""

n=int(input("Enter the number of rows: "))
k=n
ascii_number=65
for i in range(1,n+1):
    for j in range(k,0,-1):

        print(" ",end="")
    k -= 1
    for j in range(0,i):
        print(chr(ascii_number),end=" ")
        ascii_number+=1
    print("")


