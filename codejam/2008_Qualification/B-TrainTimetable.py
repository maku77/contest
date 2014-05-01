#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2008 Qualification
# Problem: B. Train Timetable
# URL: https://code.google.com/codejam/contest/32013/dashboard#s=p1
# Author: Masatoshi Ohta
# Strategy:
#   貪欲法 (Greedy Algorithm) で地道に実装するだけ。
#   出発時間の早い順番に列車を出発させていく。
#   このとき、その駅に利用可能な電車がある場合は、その電車を再利用できるため、
#   その駅からの出発カウントはインクリメントしない。
#   列車を出発させたら、到着先の駅に、利用可能な列車としてキューイングしておく。
import sys
import heapq
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]
def read_strs(): return sys.stdin.readline().split()

def calc_minutes(hhmm):
    """Convert 'HH:MM' to minutes"""
    return int(hhmm[:2]) * 60 + int(hhmm[3:])

def solve():
    # Read a problem
    turnaround_time = read_int()
    NA, NB = read_ints()

    table = []
    for i in range(NA):
        a = read_strs()
        table.append([calc_minutes(a[0]), calc_minutes(a[1]), 0])
    for i in range(NB):
        a = read_strs()
        table.append([calc_minutes(a[0]), calc_minutes(a[1]), 1])
    table.sort()

    start_count = [0, 0]  # Result
    available = [[], []]  # [ready at A, ready at B]
    for next_train in table:
        pos = next_train[2]
        if available[pos] and available[pos][0] <= next_train[0]:
            # Train is ready
            heapq.heappop(available[pos])
        else:
            # Need to start a new train
            start_count[pos] += 1
        # Modify available trains
        heapq.heappush(available[1-pos], next_train[1] + turnaround_time)

    return start_count

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: '.format(i+1) + ' '.join(map(str, solve())))
