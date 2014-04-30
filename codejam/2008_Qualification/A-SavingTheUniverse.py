#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2008 Qualification
# Problem: A. Saving the Universe
# URL: https://code.google.com/codejam/contest/32013/dashboard
# Author: Masatoshi Ohta
# Strategy:
#   query を順番に見ていき、できるだけ出てこない Search Engine を使えばよい。
#   例えば、Search Engine の選択肢が 1, 2, 3 のいずれかの場合で、
#   1 2 2 1 3 1 2
#   と query が実行される場合、3 が出てくるまでは Engine 3 を使えばよい。
#   後は、残りの 3 1 2 の query 列が与えられたとして全く同様に処理すればよい。
#   つまり、全ての Search Engine が登場するごとに切り替え数を +1 していく。
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())

def solve():
    # Read a problem
    S = read_int()
    engines = []
    for i in range(S): engines.append(read_line())
    Q = read_int()
    queries = []
    for i in range(Q): queries.append(read_line())

    count = 0
    rest = engines[:]
    for q in queries:
        if q in rest:
            if len(rest) == 1:
                count += 1
                rest = engines[:]
            rest.remove(q)

    return count

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
