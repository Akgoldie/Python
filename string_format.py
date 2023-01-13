number=int(input())
'''for i in range (1,n+1):
        #print(i,"\t", oct(i),"\t")
        print(i,"\t",oct(i),"\t",hex(i),"\t",bin(i))
for i in range(1,number+1):
        binlen = len(str(bin(number)))
        octf = oct(i).split('o')
        hexf = hex(i).split('x')
        binf = bin(i).split('b')
        print(i , octf[1] , hexf[1].upper() , binf[1] )'''

l1 = len(bin(number)[2:])
#print(bin(number))
#print(l1)

for i in range(1, number + 1):
        print(str(i).rjust(l1, ' '), end=" ")
        print(oct(i)[2:].rjust(l1, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
        print(bin(i)[2:].rjust(l1, ' '), end=" ")
        #print(i, "\t", oct(i), "\t", hex(i), "\t", bin(i))
        print("")