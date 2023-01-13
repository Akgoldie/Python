#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    f = s.split(':')

    if (f[2][2] == "P"):
        if (int(f[0]) < 12):
            f1 = int(f[0]) + 12
            f[0] = str(f1)
            f[2] = f[2][:2]
            return (":".join(f))
        elif (int(f[0]) >= 12):
            f[2] = f[2][:2]
            return (":".join(f))

    elif (f[2][2] == "A"):
        if (int(f[0]) >= 12):
            f[0] = "00"
            f[2] = f[2][:2]
            return (":".join(f))
        else:
            f[2] = f[2][:2]
            return (":".join(f))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    #timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
