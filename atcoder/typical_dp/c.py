#!/usr/local/bin/python3.3
# Contest: AtCoder - Typical DP Contest [2014-08-31]
# Problem: C - Tournament
# Author: Masatoshi Ohta
import sys
def read_int(): return int(sys.stdin.readline())

def read_problem():
    K = read_int()
    R = []
    for i in range(2 ** K):
        R.append(read_int())
    return (K, R)

# Calculate the probability of win
def probability(rate1, rate2):
    return 1 / (1 + 10 ** ((rate2 - rate1) / 400))

def opponent_indices(match, player_index):
    factor = 2 ** match
    div = int(player_index / factor)
    if div % 2 == 0: start_index = (div + 1) * factor
    else: start_index = (div - 1) * factor

    indices = []
    for i in range(factor):
        indices.append(start_index + i)
    return indices

def solve(K, R):
    # Create dp[K][2**K].
    # dp[i][j] means the probability that (j+1)th player survives after the (i+1)th match.
    # So the final answer will be in dp[K-1][].
    dp = [[0] * (2**K) for _ in range(K)]

    # Initialize the dp array (probability of win after the first match)
    for i in range(0, 2**K, 2):
        dp[0][i] = probability(R[i], R[i+1])
        dp[0][i+1] = probability(R[i+1], R[i])

    for i in range(1, K):
        for j in range(2**K):
            for op in opponent_indices(i, j):
                dp[i][j] += dp[i-1][j] * dp[i-1][op] * probability(R[j], R[op])

    # Print the answer
    for x in dp[K-1]:
        print('{:.9f}'.format(x))

if __name__ == '__main__':
    solve(*read_problem())
