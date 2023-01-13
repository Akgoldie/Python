#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    l = len(arr)
    s_arr = sorted(arr)
    # print(l)
    # print(s_arr)
    # print(s_arr[l-1])
    sum_1 = sum(s_arr[0:(l - 1)])
    sum_2 = sum(s_arr[1:l])
    print(sum_1, sum_2)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
