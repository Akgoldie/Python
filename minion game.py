def minion_game(string):

    # your code goes here
    s =len(string)

    # vow=['A','E' 'I','O','U']
    k = 0
    st = 0
    # lenght= len(s)
    for i in range(s):
        if string[i] in 'AEIOU':
            k +=(s-i)
        else:
            st +=(s-i)
    if (k > st):
        print("Kevin ", k)
    elif (st > k):
        print("Stuart ", st)
    else:
        print("Draw")
x=0
if x==0:
    s = input()
    minion_game(s)