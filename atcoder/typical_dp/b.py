#!/usr/bin/python2.7
# Contest: AtCoder - Typical DP Contest [2014-08-31]
# Problem: B - Game
# Author: Masatoshi Ohta
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def solve():
    # Read a problem
    A, B = read_ints()
    a = read_ints()
    b = read_ints()

    # Solve a problem
    dp = [[0] * (B+1) for _ in range(A+1)]  # dp[A+1][B+1]

    dp[A][B] = 0
    for i in reversed(range(A)):
        dp[i][B] = a[i] - dp[i+1][B]
    for j in reversed(range(B)):
        dp[A][j] = b[j] - dp[A][j+1]
        for i in reversed(range(A)):
            dp[i][j] = max(a[i] - dp[i+1][j], b[j] - dp[i][j+1])

    return (dp[0][0] + sum(a) + sum(b)) / 2

print(solve())
