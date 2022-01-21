#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())

if N%2 != 0:
    print("Weird")
elif N%2 == 0 & 2 <= N <= 5:
    print("Not Weird")
elif N%2 ==0 & 6 <= N <= 20:
    print("Weird")
elif N%2 ==0 & 20<N:
    print("Not Weird")


