#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    maxVal = 0
    print(queries)
    ar = [0] * (n+1)

    for i in queries:
        ar[i[0]] += i[2]
        if (i[1]+1) <= n:
            ar[i[1]+1] -= i[2]

    temp = 0
    for i in range(1,n+1):
        temp += ar[i]
        if maxVal < temp:
            maxVal = temp
    print(temp)
    print(maxVal)
    return maxVal

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nm = input().split()

    # n = int(nm[0])

    # m = int(nm[1])

    # queries = []

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))
    n = 10
    queries = [[1,5,3],[4,8,7],[6,9,1]]
    print(queries[0])
    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')

    # fptr.close()
