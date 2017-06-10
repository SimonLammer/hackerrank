#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

#print a
sum = 0
for col in xrange(n):
    sum += a[col][col] - a[col][n - col - 1]
print abs(sum)