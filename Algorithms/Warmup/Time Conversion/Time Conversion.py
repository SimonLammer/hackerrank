#!/bin/python
# https://www.hackerrank.com/challenges/time-conversion

import sys


time = raw_input().strip()
if time[:2] == '12':
    time = '00' + time[2:]

if time[-2:] == 'AM':
    print time[:-2]
else: # ends with 'PM'
    print str(int(time[:2]) + 12) + time[2:-2]