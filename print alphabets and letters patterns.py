n=int(input("Enter the number of rows: "))
ascii_number=65
for i in range(0,n):
    for j in range(0,i+1):
        char=chr(ascii_number)
        print(char,end=" ")
        ascii_number+=1
    print("")