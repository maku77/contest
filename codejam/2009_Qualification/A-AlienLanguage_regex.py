#!/usr/bin/env python
# Contest: Google Code Jam - 2009 Qualification Round
# Problem: A. Alien Language
# URL: https://code.google.com/codejam/contest/90101/dashboard#s=p0
# Author: Masatoshi Ohta
# Strategy: Using regular expression
import re
import sys
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def read_line(): return sys.stdin.readline().strip()

word_len, num_words, num_tests = read_ints()
words = []
for i in range(num_words):
    words.append(read_line())
for i in range(num_tests):
    pattern = read_line().replace('(', '[').replace(')', ']')
    prog = re.compile(pattern)
    count = len([1 for w in words if prog.match(w)])
    print('Case #{}: {}'.format(i+1, count))

