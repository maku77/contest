#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2009 Qualification Round
# Problem: C. Welcome to Code Jam
# URL: https://code.google.com/codejam/contest/90101/dashboard#s=p2
# Author: Masatoshi Ohta
# Strategy:
#   Dynamic Programming で解く。
#   'welcome ...' のフレーズを phrase[] に格納し、
#   与えられた任意のテキストを text[] に格納するとする。
#   dp[i][j] を、phrase[i-1] までのフレーズが、text[j-1] の時点で
#   一致するパターン数だと定義する。
#   dp[0][0] は、0 文字のフレーズが一致するパターン数なので 1 を格納。
#   あとは、一文字ずつ見ていき、phrase[i] が text[j] と一致するのであれば、
#   text[j] までに phrase[i] まで一致するパターン数は、
#   text[j-1] 以前に phrase[i-1] まで一致するパターン数を足し込んだものに等しい。
#   最終的な解は、phrase 全体が一致するパターン数を足し込んだもの。
#   それは dp[-1][0..-1] を足し込んだもの。
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def arr2d(y,x,init=0): return [[init] * x for _ in range(y)]

def solve():
    text = read_line()
    phrase = 'welcome to code jam'
    len_text = len(text)
    len_phrase = len(phrase)

    # dp[i][j] -- num of patterns where phrase[i-1] matches text[j-1]
    dp = arr2d(len_phrase + 1, len_text + 1)
    dp[0][0] = 1

    for i in range(len_phrase):
        ch = phrase[i]
        for j in range(i, len_text):
            if text[j] == ch:
                # i-1 sequence also matches?
                for k in range(i, j+1):
                    dp[i+1][j+1] += dp[i][k]

    return sum(dp[-1])

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {:04}'.format(i+1, solve() % 10000))
