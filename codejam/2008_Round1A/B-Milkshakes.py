#!/usr/bin/env python
# Contest: Google Code Jam - 2008 Round 1A
# Problem: B. Milkshakes
# URL: https://code.google.com/codejam/contest/dashboard?c=32016#s=p1
# Author: Masatoshi Ohta
# Strategy:
#  どれを unmalted にするかは考えなくてもよい。
#  どれを malted にしなきゃいけないかを考える。
#  unmalted と malted のリストを保持したものをレシピ (recipe) とする。
#  1. まずは全部 unmalted でレシピを作る
#  2. 全員満足させられるならそれが答え
#  3. 満足させられない人がいたら:
#     a. 好きな malted があるなら、それを malted にしたレシピを作って 2 へ戻る
#     b. 好きな malted がないなら、IMPOSSIBLE
import sys
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

UNMALTED = 0
MALTED = 1

def find_unsaticefied(recipe, likes):
    """
    Find an unsaticefied customer index (0-based).
    Returns -1 if all customers can be saticefied.
    """
    for i,like in enumerate(likes):
        for x in like:
            if recipe[x[0]-1] == x[1]:
                break
        else:
            return i
    return -1

def find_favorite_malted(customer_index, likes):
    """
    Find a user's favorite malted index (0-based).
    Returns -1 if there is no favorite malted.
    """
    for like in likes[customer_index]:
        if like[1] == MALTED:
            return like[0] - 1
    return -1

def solve():
    # Read a problem
    num_flavors = read_int()
    num_customers = read_int()

    # Parse users' likes
    likes = []
    for i in range(num_customers):
        arr = read_ints()
        vals = []
        for j in range(1, len(arr), 2):
            vals.append((arr[j], arr[j+1]))
        likes.append(vals)

    # Result list
    recipe = [UNMALTED] * num_flavors

    while (True):
        # find a unsaticefied customer.
        customer_index = find_unsaticefied(recipe, likes)
        if customer_index == -1:
            # All users have been saticefied
            return ' '.join(map(str, recipe))

        malted_index = find_favorite_malted(customer_index, likes)
        if malted_index == -1:
            # The customer cannot be saticefied
            return 'IMPOSSIBLE'
        else:
            # Change the recipe and try again
            recipe[malted_index] = MALTED

    # Should not reach here
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print('Case #{}: {}'.format(i+1, solve()))
