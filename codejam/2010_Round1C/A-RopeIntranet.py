#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2010 Round 1C
# Problem: A. Rope Intranet
# URL: https://code.google.com/codejam/contest/619102/dashboard#s=p0
# Author: Masatoshi Ohta
# Strategy:
#   i 番目の線と j 番目の線が交わる条件は、始点と終点の上下が入れ替わるときなので、
#     A[i] < A[j] and B[i] > B[j]
#   あるいは、
#     A[i] > A[j] and B[i] < B[j]
#   のときとなる。これは以下のようにしても判別可能。
#     (A[i]-A[j]) * (B[i]-B[j]) < 0
#   単純に上記の総当たりでやると、O(N^2) かかってしまうけど、
#   permutation inversion の問題と考えると O(Nlog(N)) で解けるらしい。
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def arr2d(y,x,init=0): return [[init] * x for _ in range(y)]
INF = float('inf')

def solve():
    # Read a problem
    N = read_int()
    wires = []
    for i in range(N):
        wires.append(read_ints())

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            # if (wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]) or (wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]):
            #     count += 1
            d1 = wires[i][0] - wires[j][0]
            d2 = wires[i][1] - wires[j][1]
            if d1 * d2 < 0:
                count += 1

    # Result should be returned as tuple or list
    return count

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
