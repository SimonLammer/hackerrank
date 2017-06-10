#!/bin/python
# https://www.hackerrank.com/challenges/between-two-sets

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

def prime_factorization(num):
    factors = []
    factor = 2
    while num > 1:
        cnt = 0
        while num % factor == 0:
            cnt += 1
            num /= factor
        if cnt > 0:
            factors.append([factor, cnt])
        factor += 1
    return factors

a_factors = map(prime_factorization, a)
b_factors = map(prime_factorization, b)

a_lcm_factors = []
for factors in a_factors:
    i = 0
    for factor in factors:
        while i < len(a_lcm_factors) and a_lcm_factors[i][0] < factor[0]:
            i += 1
        if i < len(a_lcm_factors):
            if a_lcm_factors[i][0] == factor[0]:
                if a_lcm_factors[i][1] < factor[1]:
                    a_lcm_factors[i][1] = factor[1]
            else:
                a_lcm_factors.insert(i, factor[:])
        else:
            a_lcm_factors.append(factor[:])

b_gcf_factors = b_factors[0][:]
for factors in b_factors[1:]:
    i = 0
    for factor in factors:
        while i < len(b_gcf_factors) and factor[0] > b_gcf_factors[i][0]:
            del b_gcf_factors[i]
        if i >= len(b_gcf_factors):
            break;
        if factor[0] == b_gcf_factors[i][0]:
            if factor[1] < b_gcf_factors[i][1]:
                b_gcf_factors[i][1] = factor[1]
            i += 1
    while i < len(b_gcf_factors):
        del b_gcf_factors[i]

# x % a_lcm == 0 and x % b_gcf == 0
result = 1
i = 0
for gcf_factor in b_gcf_factors:
    if i >= len(a_lcm_factors) or gcf_factor[0] < a_lcm_factors[i][0]:
        result *= gcf_factor[1] + 1
        #print 'A ' + str(gcf_factor[1] + 1)
    elif gcf_factor[0] == a_lcm_factors[i][0]:
        if gcf_factor[1] < a_lcm_factors[i][1]:
            result = 0
            break
        elif gcf_factor[1] > a_lcm_factors[i][1]:
            result *= gcf_factor[1] - a_lcm_factors[i][1] + 1
            #print 'B ' + str(gcf_factor[1] - a_lcm_factors[i][1] + 1)
        i += 1
    else: # gcf_factor[0] > a_lcm_factors[i][0]
        result = 0
        break
if i < len(a_lcm_factors):
    result = 0
print result