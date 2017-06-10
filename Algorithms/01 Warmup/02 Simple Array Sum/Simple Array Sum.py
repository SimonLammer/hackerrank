#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sum = 0;
for num in arr:
   sum += num

print sum