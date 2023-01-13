def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase
    l = []
    for i in range(n):
        s = "-".join(design[i:n])
        #print(s)
        l.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
        #print(s[::-1])
        #print(s[1:])
        #print((s[::-1] + s[1:]))
        #l.append((s[::-1] + s[1:]))
    #print(l[:0:-1])
    #print(l)

    print('\n'.join(l[:0:-1] + l))


n=int(input())
print_rangoli(n)
