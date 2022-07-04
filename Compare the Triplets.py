import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def compareTriplets(a, b):
    if (len(a)==3 and len(b)==3):
        alice = 0
        Bob = 0
        for i in range(3):
            if a[i] > b[i]:
                alice +=1
            if a[i] < b[i]:
                Bob +=1
    return(alice, Bob)

