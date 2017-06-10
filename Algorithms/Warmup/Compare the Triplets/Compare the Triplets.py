#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    a = 0
    b = 0
    for x in [(a0, b0), (a1, b1), (a2, b2)]:
        if x[0] > x[1]:
            a += 1
        elif x[0] < x[1]:
            b += 1
    return [a, b]

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))