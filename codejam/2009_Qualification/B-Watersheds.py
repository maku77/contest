#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2009 Qualification Round
# Problem: B. Watersheds
# URL: https://code.google.com/codejam/contest/90101/dashboard#s=p1
# Author: Masatoshi Ohta
# Strategy:
#   左上のセルから順番に sink を見つけていく。
#   新しい sink に辿り着いたら、そこに新しいラベルをつける。
#   既知の sink に辿り着いたら、その sink と同じラベルをつける。
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def read_table(h): return [read_ints() for _ in range(h)]

def scan(h, w):
    for y in range(h):
        for x in range(w):
            yield x, y

def neighbors(x, y, w, h):
    if 0 <= y-1: yield x, y-1
    if 0 <= x-1: yield x-1, y
    if x+1 < w: yield x+1, y
    if y+1 < h: yield x, y+1

def get_flow(altitudes, x, y, w, h):
    min_val, min_x, min_y = altitudes[y][x], x, y
    for x2, y2 in neighbors(x, y, w, h):
        val = altitudes[y2][x2]
        if val < min_val:
            min_val, min_x, min_y = val, x2, y2
    return min_x, min_y

def find_sink(altitudes, pos, w, h):
    prev = (-1, -1)
    while prev != pos:
        prev = pos
        pos = get_flow(altitudes, pos[0], pos[1], w, h)
    return pos

def solve():
    H, W = read_ints()
    altitudes = read_table(H)

    result = {}
    label = 'a'
    for pos in scan(H, W):
        sink = find_sink(altitudes, pos, W, H)
        # If a new sink was found, set a new label
        if sink not in result:
            result[sink] = label
            label = chr(ord(label)+1)
        # Label is the same as of the sink
        result[pos] = result[sink]

    print_result(result, W, H)

def print_result(result, w, h):
    for y in range(h):
        arr = [result[(x,y)] for x in range(w)]
        print(' '.join(arr))

if __name__ == '__main__':
    T = read_int()
    for t in range(1, T+1):
        print('Case #{}:'.format(t))
        solve()
