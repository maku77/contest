#!/usr/bin/python2.7
# Contest: AtCoder - Typical DP Contest [2014-08-31]
# Problem: A - Contest
# Author: Masatoshi Ohta
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def solve():
    # Read a problem
    N = read_int()
    P = read_ints()

    # Solve a problem
    dp = [False] * (sum(P) + 1)
    dp[0] = True
    for p in P:
        for i in reversed(range(len(dp))):
            if dp[i]:
                dp[i + p] = True

    return dp.count(True)

print(solve())
