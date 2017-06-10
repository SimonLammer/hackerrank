#!/bin/python
# https://www.hackerrank.com/challenges/grading

import sys

def solve(grades):
    return map(roundGrade, grades)

def roundGrade(grade):
    if grade < 38:
        return grade
    else:
        d = grade % 5
        if d >= 3:
            return grade + 5 - d
        else:
            return grade

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
