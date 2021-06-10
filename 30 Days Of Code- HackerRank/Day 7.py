#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    res=arr[::-1]
    res1= ' '.join(map(str,res))
    print(res1)
