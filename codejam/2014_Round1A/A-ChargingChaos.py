#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2014 Round A [2014-04-26]
# Problem: A. Charging Chaos
# URL: https://code.google.com/codejam/contest/2984486/dashboard
# Author: Masatoshi Ohta
# Strategy:
#   2 つのビット列の xor を取ると、異なる部分が分かることを利用する。
#   初期配置のリスト init[] の 1 つ目 init[0] のビット列と、
#   最終系のリスト desired[i] との xor を取ると、
#   候補となるスイッチのパターンを構成できる。
#   つまり候補は desired[] の数 N だけ存在するが、
#   この時点ではそのパターンが正しいとは分からない。
#   そのパターンを残りの init[1..N-1] にも適用 (xor) していき、
#   それぞれがいずれかの desired[] と一致するようであれば、
#   そのパターン（スイッチの組み合わせ）は組み合わせとして正しいことになる。
#   あとは正しいスイッチのパターンのうち、1 のビット数が少ないものを選ぶ。
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def read_strs(): return sys.stdin.readline().split()
INF = float('inf')

def count_bits(val):
    count = 0
    while val > 0:
        if val & 1 == 1:
            count += 1
        val >>= 1
    return count

def solve():
    N, L = read_ints()
    inits = [int(x, 2) for x in read_strs()]
    desired = [int(x, 2) for x in read_strs()]
    patterns = map(lambda x: x ^ inits[0], desired)

    min_change = INF
    for p in patterns:
        for i in range(1, N):
            if not (p ^ inits[i] in desired):
                # pattern p is not acceptable by inits[i]
                break
        else:
            # pattern p seems acceptable
            c = count_bits(p)
            if c < min_change:
                min_change = c

    if min_change == INF:
        return 'NOT POSSIBLE'
    else:
        return min_change

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, str(solve())))
