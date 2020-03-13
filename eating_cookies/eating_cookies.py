#!/usr/bin/python

# import functools
import sys
# from functools import lru_cache
# @lru_cache(maxsize=1000)

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# reference material for recursion https://dev.to/teosoft7/how-to-implement-fibonacci-sequence-with-python-4cfo


def eating_cookies(n, cache={}):
  # the test case of three has 4 options, 0,1,2,3 which gives us our answer of 4. So any value of 0 needs to be 1
    if n <= 0:
        n = 0
        return n + 1
  # any value of one is returned as one, less than one returned as one
    if n <= 2:
        return n

    if n not in cache:
        cache[n] = eating_cookies(
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
