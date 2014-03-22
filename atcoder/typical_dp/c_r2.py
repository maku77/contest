#!/usr/local/bin/python3.3
# Contest: AtCoder - Typical DP Contest [2014-08-31]
# Problem: C - Tournament
# Author: Masatoshi Ohta
import sys
def read_int(): return int(sys.stdin.readline())
def array2d(x,y,init=0): return [[init] * x for _ in range(y)]

def read_problem():
    K = read_int()
    R = []
    for i in range(2 ** K):
        R.append(read_int())
    return (K, R)

# Calculate the probability of win
def probability(rate1, rate2):
    return 1 / (1 + 10 ** ((rate2 - rate1) / 400))

def solve(K, R):
    # Create dp[K+1][2**K].
    # dp[i][j] means the probability that (j+1)-th player survives after the i-th match.
    # So the final answer will be in dp[K][].
    dp = array2d(2**K, K+1)

    # Initialize the dp array (all players survive 100% when no match has begun)
    dp[0] = [1.0] * 2**K

    for i in range(1, K+1):
        group_size = 2 ** (i - 1)
        for j in range(0, 2**K - group_size, group_size * 2):
            op_start = j + group_size
            op_end = op_start + group_size
            for k in range(j, j + group_size):
                for op in range(op_start, op_end):
                    dp[i][k] += dp[i-1][k] * dp[i-1][op] * probability(R[k], R[op])
                    dp[i][op] += dp[i-1][k] * dp[i-1][op] * probability(R[op], R[k])

    # Print the answer
    for x in dp[K]:
        print('{:.9f}'.format(x))

if __name__ == '__main__':
    solve(*read_problem())
