#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    '''k=2*n-2
    for i in range (0,n):
        for j in range (0,k):
            print(end="")
        k=k-2
        for j in range (0,i+1):
            print("#", end="")
        print("")
    # Write your code here'''
    # python3 code to print pyramid pattern using while loop
    i=1
    while(i<=n):
        print(" " * (n - i) +"#" * i)
        i+=1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
