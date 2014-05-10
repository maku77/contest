#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2014 Round 1B
# Problem: A. The Repeater
# URL: https://code.google.com/codejam/contest/2994486/dashboard
# Author: Masatoshi Ohta
# Strategy:
#   前から順番に登場する文字を、それぞれの文字列でカウントする。
#   同じ文字が登場しない文字列が 1 つでも登場したら達成不可能 ('Fegla Won')。
#   その文字を増減していくつに合わせればよいかは、カウント数のメディアンを
#   を取ればいい。なぜなら、それより減少させる場合、あるいは増加させる場合は、
#   半分以上の文字列に対して操作を加えないといけなくなるから。つまり、
#   中央に位置する数を持つ文字列に合わせていくのが最適になる。
#   （文字列数が偶数の場合は、中央の 2 つどちらに合わせてもよい）
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())

def target_num(vals):
    '''After modification, the num of chars should be this value.'''
    index = len(vals) // 2
    return sorted(vals)[index]

def solve():
    # Read a problem
    N = read_int()
    lines = []
    for i in range(N):
        lines.append(read_line())

    result = 0
    while len(lines[0]) > 0:
        ch = lines[0][0]
        counts = [0] * N
        for i in range(len(lines)):
            while len(lines[i]) > 0 and lines[i][0] == ch:
                counts[i] += 1
                lines[i] = lines[i][1:]
            if counts[i] == 0:
                return 'Fegla Won'
        target = target_num(counts)
        result += sum([int(abs(x - target)) for x in counts])

    if any(len(x) > 0 for x in lines):
        return 'Fegla Won'

    return result

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
