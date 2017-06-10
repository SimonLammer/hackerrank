#!/bin/python

import sys

n = 6
arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

def hourglassSum(arr, centerRow, centerColumn):
    #print arr[centerRow - 1][centerColumn-1:centerColumn+2]
    #print '    ' + str(arr[centerRow][centerColumn])
    #print arr[centerRow + 1][centerColumn-1:centerColumn+2]
    res = arr[centerRow][centerColumn] # center
    for i in [-1, 1]:
        res += sum(arr[centerRow + i][centerColumn - 1:centerColumn + 2]) # top and bottom
    return res

maxHourglassSum = -9 * 7
for col in xrange(1, n - 1):
    for row in xrange(1, n - 1):
        s = hourglassSum(arr, row, col)
        #print str(s) + '\n'
        if (maxHourglassSum < s):
            maxHourglassSum = s

print maxHourglassSum