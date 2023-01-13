#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = []
    d2 = []
    for i in range(0, n):
        for j in range(0, n):
            d1.append(arr[i][i])
            d2.append(arr[i][n - 1 - i])
            break

    # print(d1,d2)
    sd1 = sum(d1)
    sd2 = sum(d2)
    # print(sd1,sd2)
    if (sd1 > sd2):
        det = sd1 - sd2
        # print(det)
    elif (sd2 > sd1):
        det = sd2 - sd1
        # print(det)
    else:
        det = sd1 - sd2
        # print(det)

    return det


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
