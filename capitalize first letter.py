def solve(s):

    sp=s.split(" ")
    #print(len(sp))
    #print(sp)
    for i in range(0, len(sp)):
        f = sp[i]
        #print(f)
        fi=f.capitalize()
        #print(fi)
        sp[i]=str(fi)
    spl=' '.join(sp)
    return spl



s = input()
j=solve(s)
print(j)