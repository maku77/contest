#!/usr/bin/env python3
def solve(n, m, i, j):
    mask1 = (1 << j) - 1
    mask2 = (1 << i) - 1
    mask = ~(mask1 ^ mask2)
    return (n & mask) | (m << i)

if __name__ == '__main__':
    N = 0b10000000000
    M = 0b10011
    i = 2
    j = 6
    print(bin(solve(N, M, i, j)))
