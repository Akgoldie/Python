#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count_p = 0
    count_n = 0
    count_z = 0
    for i in range(0, len(arr)):
        if (arr[i] > 0):
            count_p += 1
        elif (arr[i] < 0):
            count_n += 1
        else:
            count_z += 1
    print(count_p / len(arr))
    print(count_n / len(arr))
    print(count_z / len(arr))

    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
