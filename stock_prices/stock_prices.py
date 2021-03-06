#!/usr/bin/python

import argparse

# bubble sort solution


def find_max_profit(prices):
    result = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            temp = prices[j] - prices[i]
            print(prices[i], prices[j], temp)
            result.append(temp)
    return max(result)


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
