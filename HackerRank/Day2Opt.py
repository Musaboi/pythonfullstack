#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
def solve(meal_cost,tip_percent, tax_percent):
    print(int(meal_cost+tip_percent/100*meal_cost+tax_percent/100*meal_cost))

solve(meal_cost,tip_percent,tax_percent)


