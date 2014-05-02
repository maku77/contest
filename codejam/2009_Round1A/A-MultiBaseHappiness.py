#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2009 Round 1A
# Problem: A. Multi-base happiness
# URL: https://code.google.com/codejam/contest/32013/dashboard#s=p1
# Author: Masatoshi Ohta
# Strategy:
#   ある数値 n が、基数 base において Happy number であるかどうかは、
#   is_happy(n, base) をメモ化して求められるようにしておく。
#   メモ化の範囲は n <= 1000 だけしておいて、それ以上の n に対して
#   求めたい場合は n <= 1000 になるまで sum_squares() を繰り返し実行。
#   各桁の二乗は高々 9*9=81 にしかならないので、sum_squares() の結果は、
#   すぐに 1000 以下になる。
#   より重要な高速化ポイントは、与えられた全ての base で happy number となる
#   最小の値を求めるときに、どの数から確認していくかということ。
#   （各基数の組み合わせでの確認を、毎回 2 から行っていると非常に遅い）
#   ここでは、考えうるすべての基数のコンビネーションで最小 happy number を
#   先に求めてしまうアプローチをとっている。
#   より少ない数の基数のコンビネーションでの最小 happy number を先に求めておけば、
#   それよりひとつ数の多い基数の組み合わせは、過去に求めたコンビネーションに
#   基数をひとつだけ足したものなので、確認を始める数の最小値は、過去の解から
#   求めることができる。
import itertools
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def debug(*arr): sys.stderr.write(' '.join(str(x) for x in arr)+'\n')

class HappyCache:
    BASES = range(2, 11)
    CACHE_MAX = 1000
    SQUARE_TABLE = [x ** 2 for x in range(0, 10)]

    def __init__(self):
        self.create_cache()

    def create_cache(self):
        self.memo = {}  # key:(num, base), val:True or False
        for base in self.BASES:
            self.memo[(1, base)] = True
            for n in range(2, self.CACHE_MAX+1):
                self.calc_happy(n, base)

    def calc_happy(self, n, base):
        if (n, base) in self.memo:
            return self.memo[(n, base)]
        self.memo[(n, base)] = False
        next_num = self.sum_squares(n, base)
        self.memo[(n, base)] = self.calc_happy(next_num, base)
        return self.memo[(n, base)]

    @classmethod
    def sum_squares(cls, n, base):
        result = 0
        while n != 0:
            n, r = divmod(n, base)
            result += cls.SQUARE_TABLE[r]
        return result

    def is_happy(self, n, base):
        while n > 1000:
            n = self.sum_squares(n, base)
        return self.memo[(n, base)]

def solve(start_num, happy, bases):
    n = start_num
    while not all(happy.is_happy(n, b) for b in bases):
        n += 1
    return n

if __name__ == '__main__':
    happy = HappyCache()

    # Calculate all combinations of the bases
    answers = {}  # key:(base1, base2, ...), val:smallest_happy
    BASES = range(2, 11)
    for i in range(1, len(BASES)+1):
        for bases in itertools.combinations(BASES, i):
            start_num = 2
            for sub in itertools.combinations(bases, len(bases)-1):
                if sub in answers and start_num < answers[sub]:
                    start_num = answers[sub]
            ans = solve(start_num, happy, bases)
            answers[bases] = ans
            debug(bases, ans)

    # Show answers
    T = read_int()
    for i in range(T):
        bases = tuple(read_ints())
        print('Case #{}: {}'.format(i+1, answers[bases]))

