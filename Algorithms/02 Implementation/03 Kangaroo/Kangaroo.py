#!/bin/python
# https://www.hackerrank.com/challenges/kangaroo

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

'''
x1 + t * v1 = x2 + t * v2
t * v1 - t * v2 = x2 - x1
t * (v1 - v2) = x2 - x1
t = (x2 - x1) / (v1 - v2)
'''
if v1 == v2:
    if x1 == x2:
        print 'YES'
    else:
        print 'NO'
else:
    t = (x2 - x1) / float(v1 - v2)
    if t < 0 or t % 1 >= 0.001:
        print 'NO'
    else:
        print 'YES'