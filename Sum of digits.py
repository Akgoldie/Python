def getSum(n):
    sum = 0
    for digit in str(n):
        print(int(digit))
        sum += int(digit)
    return sum


n = 12345
print(getSum(n))