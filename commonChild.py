#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 


#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    c3 = 0
    comun = c1 & c2
    list = comun.elements()
    for a in list:
        c3 = c3 + 1
    return c3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()nt
