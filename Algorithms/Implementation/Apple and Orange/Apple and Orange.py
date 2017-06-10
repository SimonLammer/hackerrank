#!/bin/python
# https://www.hackerrank.com/challenges/apple-and-orange

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))

#print (apples, oranges)

cnt = 0
for apple in apples:
    if s <= (a + apple) and (a + apple) <= t:
        cnt += 1
print cnt

cnt = 0
for orange in oranges:
    if s <= (b + orange) and (b + orange) <= t:
        cnt += 1
print cnt