#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # count_list=[]
    for i in range(0, 100):
        count = 0
        for j in range(0, n, +1):
            if ((arr[j]) == i):
                count += 1
        # count_list.append(count)
        print(count, end=" ")

    """for i in range (0,len(count_list)):
        print(count_list[i],end=" ")
              """


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # result = countingSort(arr)
    countingSort(arr)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
