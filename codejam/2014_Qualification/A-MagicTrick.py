#!/usr/bin/env python
# Contest: Google Code Jam - 2014 Qualification Round [2014-08-31]
# Problem: A. Magic Trick
# URL: https://code.google.com/codejam/contest/2974486/dashboard
# Author: Masatoshi Ohta
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def get_candidate():
    ans = read_int()
    for i in range(4):
        if i+1 == ans:
            rowset = set(read_ints())
        else:
            read_ints()
    return rowset

def solve():
    set1 = get_candidate()
    set2 = get_candidate()
    set3 = set1 & set2

    if len(set3) == 1:
        return set3.pop()
    elif len(set3) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
