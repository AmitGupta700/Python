#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    i=1
    while(i<=10):
        num=n
        num=num*i
        print("%d x %d = %d" %(n,i,num))
        i+=1
