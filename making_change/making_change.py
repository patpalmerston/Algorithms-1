#!/usr/bin/python

import sys


def making_change(amount, denominations=[1, 5, 10, 25, 50]):
    # base case
    if amount <= 2:
        return 1
    # starting a cache equal to the size of the amount, plus an initial default of 1 for index of zero

    cache = [1] + [0] * amount

    # loop through the coins in our list
    for coin in denominations:
        # loop through the range of the outer loop coin and our amount + 1
        # first outer loop iteration starts at index of 1, then 5, then 10, then 25, then 50, as our index starts in the range dictated by the value of our denominations outer loop.
        for i in range(coin, amount + 1):
            # print('coin:', coin, f'amount: {amount} + 1 = ', amount +1)
            # print("i: ", i, "i - coin = ", i-coin)

            # inner loop index starts from the index equal to the value of coin and will iterate however many times that that index can be subtracted from 'amount + 1'. Our Cache indexes will be given a value every time the current index(1-11)  minus the coin value from the denominations list, is less than our original amount of '10'. Each iteration of the outer loop will start our inner loop at the index equal to the value of the the outer loop coin.
            cache[i] += cache[i - coin]
            # default value of cache[0] = 1
            # then we cycle through cache[1]-cache[11] subtracting the coin value of "1 cent", from the current loop index
            # giving each loop that is able complete this task a value of 1 in the cache index
            # when we hit cache[11] and minus the coin of '1', we return the value of amount and restart the loop

            print(cache, cache[amount])
            # print('cache amount', cache[amount])

    # this counts how many times the loop was able to generate the value of amount
    return cache[amount]


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
