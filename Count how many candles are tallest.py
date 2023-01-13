#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    sr = sorted(candles)
    l = len(sr)
    big = sr[l - 1]
    # print(big)
    count = 0
    for i in range(0, l):
        if sr[i] == big:
            count += 1
    # print(count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    # birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
