#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
# Contest: Google Code Jam - 2014 Round 1C
# Problem: B. Reordering Train Cars
# URL: https://code.google.com/codejam/contest/3004486/dashboard#s=p1
# Author: Masatoshi Ohta
# Strategy:
#  permutatable_count()
#    aaa, a, abba のように先頭と末尾が同じ文字の car が n 個以上出てくる場合は、
#    それぞれの順番は入れ替えが可能なので、n! だけパターン数が倍増する（順列）。
#    （abba が出た時点で NG だが、ここでは気にしない（最後にまとめて弾く））
#
#  create_trains()
#    それぞれの車両 (car) をつなげて、結合された列車 (train) を作っていく。
#    任意の car を 1 つ取りだし、後ろにつなげられるだけ繋げていけばよい。
#    ただし、aaa のような、先頭と末尾が同じ car は中間に入れたいので優先的に繋げる。
#    同様に、前にも繋げられるだけ繋げていく。
#    これを全車両に適用すれば、列車 (train) のリスト trains ができあがる。
#
#  is_valid_trains()
#    この trains の組み合わせに、不整合がないかをチェック。
#      (a) 1 つの列車内で分断された character が存在しないか
#          （例: abba, abbacc, abbcbb はすべて NG）
#      (b) 1 つの文字が複数の列車にまたがって配置されていないか
#
#  この列車の順番は入れ替えが可能なので、結合された列車数が n だとすると、
#  最終的な組み合わせの数は、n! 倍に増加する。これが答え。
import sys
import math
def read_int(): return int(sys.stdin.readline())
def read_strs(): return sys.stdin.readline().split()
MOD = 1000000007

def solve(cars):
    # 位置入れ替え可能（先頭と末尾が終わり）によるパターン数
    count = permutatable_count(cars)
    # 車両を繋げられるだけ繋いだできた列車のリストを作る
    trains = create_trains(cars)
    # その列車リストが条件を満たしていればパターン数を計算
    if is_valid_trains(trains):
        return count * math.factorial(len(trains)) % MOD
    # 正しい列車リストは作れない
    return 0

def permutatable_count(cars):
    used = {}
    for t in cars:
        if t[0] == t[-1]:
            used[t[0]] = used.get(t[0], 0) + 1
    count = 1
    for val in used.values():
        count *= math.factorial(val)
    return count % MOD

def create_trains(cars):
    trains = []
    while cars:
        con = [cars.pop()]  # 起点は適当に選ぶ
        while connect_backward(con, cars): pass
        while connect_forward(con, cars): pass
        trains.append(''.join(con))  # ここで一連の文字列にしとく
    return trains

def connect_backward(con, cars):
    last_char = con[-1][-1]
    candidate = -1
    for i in range(len(cars)):
        if cars[i][0] == last_char:
            candidate = i
            if cars[i][0] == cars[i][-1]:
                break
    if candidate >= 0:
        con.append(cars[candidate])
        del cars[candidate]
        return True
    return False

def connect_forward(con, cars):
    first_char = con[0][0]
    candidate = -1
    for i in range(len(cars)):
        if cars[i][-1] == first_char:
            candidate = i
            if cars[i][0] == cars[i][-1]:
                break
    if candidate >= 0:
        con.insert(0, cars[candidate])
        del cars[candidate]
        return True
    return False

def is_valid_trains(trains):
    used = set()
    for t in trains:
        if t[0] in used:  # 別の列車で使われている
            return False
        used.add(t[0])
        for i in range(1, len(t)):
            if t[i-1] != t[i]:
                if t[i] in used:
                    return False
                used.add(t[i])
    return True

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        N = read_int()
        cars = read_strs()
        print('Case #{}: {}'.format(i+1, solve(cars)))
