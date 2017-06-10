#!/bin/python
# https://www.hackerrank.com/challenges/plus-minus

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positives = 0
negatives = 0
zeroes = 0

for num in arr:
    if num > 0:
        positives += 1
    elif num == 0:
        zeroes += 1
    else: # num < 0
        negatives += 1

#print [n, positives, negatives, zeroes]
print round(positives / float(n), 6)
print round(negatives / float(n), 6)
print round(zeroes / float(n), 6)