#!/usr/bin/env python
# Contest: Google Code Jam - 2008 Round 1A
# Problem: A. Minimum Scalar Product
# URL: https://code.google.com/codejam/contest/dashboard?c=32016
# Author: Masatoshi Ohta
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def solve():
    # Read a problem
    n = read_int()
    v1 = read_ints()
    v2 = read_ints()
    v1.sort()
    v2.sort()
    v2.reverse()

    sum = 0
    for i in range(n):
        sum += v1[i] * v2[i]

    return sum

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
