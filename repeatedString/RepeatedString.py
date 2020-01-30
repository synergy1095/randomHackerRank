#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s = '', n = -1):
    if n < 0 or not s:
        return None
    # print(s + ' ' + str(n))
    sLength = len(s)
    aCount = 0
    numACount = n // sLength
    for i in range(sLength):
        if s[i] == 'a':
            aCount += 1

    remainder = n % sLength
    remainderACount = 0
    if remainder != 0:
        for j in range(remainder):
            if s[j] == 'a':
                remainderACount += 1

    # print(str(aCount) + ' ' + str(numACount) + ' ' + str(remainder))
    totalACount = aCount * numACount + remainderACount
    
    return totalACount 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # n = int(input())
    s = 'a'
    n = 1000000000000
    # s = 'ceebbcb'
    # n = 817723
    result = repeatedString(s, n)
    print (result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
