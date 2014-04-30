#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def arr2d(y,x,init=0): return [[init] * x for _ in range(y)]
INF = float('inf')

def solve():
    # Read a problem
    a = read_int()
    b = read_int()
    c, d, e = read_ints()

    # Result should be returned as tuple or list
    return (1, 2, 3)

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: '.format(i+1) + ' '.join(map(str, solve())))
