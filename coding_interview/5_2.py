#!/usr/bin/env python3
def solve(n):
    frac = 0.5
    result = '0.'

    while n > 0:
        if n >= frac:
            result += '1'
            n -= frac
        else:
            result += '0'
        frac /= 2
        if len(result) >= 32:
            return 'ERROR'

    return result

import random
def make_problem():
    bits = [0.5 ** i for i in range(1, 31)]
    seeds = random.sample(bits, random.randint(0, len(bits)))
    return sum(seeds)

if __name__ == '__main__':
    for a in range(5):
        num = make_problem()
        print('{:.31f} = {}'.format(num, solve(num)))
