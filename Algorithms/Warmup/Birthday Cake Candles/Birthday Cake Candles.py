#!/bin/python
# https://www.hackerrank.com/challenges/birthday-cake-candles

import sys


n = int(raw_input().strip())
heights = map(int,raw_input().strip().split(' '))

res = 0
highest = max(heights)
for i in heights:
    if i == highest:
        res += 1

print res