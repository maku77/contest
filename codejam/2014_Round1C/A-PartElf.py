#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2014 Round 1C
# Problem: A. Part Elf
# URL: https://code.google.com/codejam/contest/3004486/dashboard
# Author: Masatoshi Ohta
# Strategy:
#   与えられた分数を約分して、2 の累乗の形になっていなかったら impossible。
#   （n & (n-1) != 0 で判別可能）
#   祖先から考えると、その子供は 0, 1/2, 2/2 が考えられる。
#   さらに、その子供は 0, 1/4, 2/4, 3/4, 4/4 が考えられる。
#   さらに、その子供は 0, 1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 8/8 が考えられる。
#   自分自身が 1/2 以上であれば、その親のどちらかは 1 でよい。
#   逆に自分自身が 1/2 より小さければ、どちらかの親を最大にしていけばよい。
#   それはつまり、親のどちらかが自分自身の 2 倍であると考えればよい。
import sys
import fractions
def read_int(): return int(sys.stdin.readline())

def reduce_fraction(a, b):
  div = fractions.gcd(a, b)
  return (a//div, b//div)

def solve():
    p, q = [int(x) for x in sys.stdin.readline().strip().split('/')]
    p, q = reduce_fraction(p, q)
    if q & (q - 1) != 0:
        return 'impossible'

    count = 1
    while p * 2 < q:
        count += 1
        p *= 2

    return count

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
