#!/usr/local/bin/python3.3
# Contest: AtCoder - ***** [2014-08-31]
# Problem: ***** - *****
# Author: Masatoshi Ohta
import sys
def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def arr2d(y,x,init=0): return [[init] * x for _ in range(y)]  # => arr[y][x]

def read_problem():
    A = read_int()
    B = read_int()
    return (A, B)

def solve(A, B):
    print(A, B)

if __name__ == '__main__':
    solve(*read_problem())
