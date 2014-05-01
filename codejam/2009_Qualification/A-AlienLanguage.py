#!/usr/bin/env python
# Contest: Google Code Jam - 2009 Qualification Round
# Problem: A. Alien Language
# URL: https://code.google.com/codejam/contest/90101/dashboard#s=p0
# Author: Masatoshi Ohta
import sys

def split_pattern(pattern):
    result = []
    group = ''
    is_group = False
    for ch in pattern:
        if ch == '(':
            group = ''
            is_group = True
        elif ch == ')':
            result.append(group[:])
            is_group = False
        else:
            if is_group: group += ch
            else: result.append(ch)
    return result

def check(word, patterns):
    for i in range(len(word)):
        if not word[i] in patterns[i]:
            return False
    return True

def main():
    # Read a problem
    word_len, num_words, num_tests = Util.read_ints()
    words = []
    for i in range(num_words):
        words.append(Util.read_line())

    # Each test pattern
    for i in range(num_tests):
        pattern = Util.read_line()
        patterns = split_pattern(pattern)
        count = sum(check(w, patterns) for w in words)
        Util.result(count)

##### Template #####
class Util:
    count = 0
    @classmethod
    def result(cls, result):
        cls.count += 1
        print('Case #{}: {}'.format(cls.count, str(result)))
    @staticmethod
    def read_line(): return sys.stdin.readline().strip()
    @staticmethod
    def read_int(): return int(sys.stdin.readline())
    @staticmethod
    def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
    @staticmethod
    def arr2d(y,x,init=0): return [[init] * x for _ in range(y)]

if __name__ == '__main__':
    main()
