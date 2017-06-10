#!/bin/python
# https://www.hackerrank.com/challenges/staircase

import sys


n = int(raw_input().strip())

for i in range(1, n + 1):
    stair = ''
    for j in range(n - i):
        stair += ' '
    for j in range(i):
        stair += '#'
    print stair